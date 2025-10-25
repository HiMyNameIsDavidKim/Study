# 코딩 테스트

## 📋 Contents
### 🎯 ML baseline
### 🐍 Python algorithm
### 📊 SQL query
<br><br>



## `[🎯 ML baseline]`
* 불러오기
* 데이터 전처리
* EDA
    * 유형 분리, 유형 수정
    * categorical, numerical
* 모델링
    * 학습
    * 평가 (report or matric)
    * 해석 (fi, shap, ROC or 시각화)
<br><br>

### [불러오기]
* import pandas as pd
* import numpy as np
* import matplotlib.pyplot as plt
* import seaborn as sns
* plt.style.use(['seaborn-v0_8'])
* sns.set(style="darkgrid")
* df = pd.read_csv('train.csv')
* df.head(10)
<br><br>

### [데이터 전처리]
* df.shape
* df.info()
    * 시계열 변경: df['date'] = pd.to_datetime(df['date'])
* df.isnull().sum()
    * 채우기: df = df.fillna('Null')
    * 행기준 제거: df = df.dropna()
    * 열기준 제거: df = df.dropna(axis=1)
* df.describe()
<br><br>

### [EDA]
* 데이터 유형 분리
    * ```python
      cols_categorical = df.select_dtypes(include=object).columns
      cols_numerical = df.select_dtypes(exclude=object).columns
      print(f'##### categorical #####')
      [print(f'{col}: {df[col].nunique()}') for col in cols_categorical]
      print(f'##### numerical #####')
      [print(f'{col}: {df[col].nunique()}') for col in cols_numerical]
      ```
* 유형 수정
    * ```python
      cols = ['col1', 'col2']
      for col in cols:
          cols_numerical = cols_numerical.drop(col)
          cols_categorical = cols_categorical.append(pd.Index([col]))
      ```
* categorical
    * y가 이산형
        * ```python
          for i, col in enumerate(cols_categorical):
              plt.subplot(len(cols_categorical)//3, 3, i+1)
              sns.countplot(data=df, x=col, hue='y', legend=False)
              plt.title(f'{col} Count Plot')
          plt.tight_layout()
          plt.show()
          ```
    * y가 연속형
        * ```python
          for i, col in enumerate(cols_categorical):
              plt.subplot(len(cols_categorical)//3, 3, i+1)
              sns.violinplot(data=df, x=col, hue=col, y='y', inner='quartile', legend=False)
              plt.title(f'{col} Violin Plot')
          plt.tight_layout()
          plt.show()
          ```
* numerical
    * 상관계수 히트맵
        * ```python
          sns.heatmap(df[cols_numerical].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths='0.5')
          plt.title(f'Corr Heatmap')
          plt.tight_layout()
          plt.show()
          ```
    * y가 이산형
        * ```python
          for i, col in enumerate(cols_numerical):
              plt.subplot(len(cols_numerical)//3, 3, i+1)
              sns.violinplot(data=df, x='y', hue='y', y=col, inner='quartile', legend=False)
              plt.title(f'{col} Violin Plot')
          plt.tight_layout()
          plt.show()
          ```
    * y가 연속형
        * ```python
          df_temp = df.copy()
          df_temp = df_temp[cols_numerical]
          # df_temp = df_temp.sample(n=len(df_temp)//100, random_state=42)
          sns.pairplot(df_temp, kind="scatter", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
          plt.title(f'Scatter Plot')
          plt.tight_layout()
          plt.show()
          ```
<br><br>



### [모델링]
* 학습
    * ```python
      from sklearn.model_selection import train_test_split
      from sklearn.preprocessing import LabelEncoder
      import lightgbm as lgb


      LEARNING_RATE = 3e-2
      N_ESTIMATORS = 500
      THRESHOLD = 0.3

      params = {
          "learning_rate": LEARNING_RATE,
          "n_estimators": N_ESTIMATORS,
          "num_leaves": 16,
          "max_depth": 6,
          "drop_rate": 0.3,
          "seed": 42,
      }

      df_temp = df.copy()
      X = df_temp.drop('y', axis=1)
      Y = df_temp['y']

      cols_drop = ['id']
      for col in cols_drop:
          X.drop(col, axis=1, inplace=True)

      for column in X.columns:
          if X[column].dtype == object:
              le = LabelEncoder()
              X[column] = le.fit_transform(X[column])

      x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
      # x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)  # reg
      model = lgb.LGBMClassifier(**params, objective='binary', metric='binary_logloss')
      # model = lgb.LGBMClassifier(**params, objective='multiclass', metric='multi_logloss')  # multi
      # model = lgb.LGBMRegressor(**params, objective='regression', metric='mse')  # reg
      model.fit(x_train, y_train)
      ```
* 평가
    * 분류
        * ```python
          from sklearn.metrics import classification_report


          y_proba_train = model.predict(x_train)
          y_pred_train = (y_proba_train > THRESHOLD).astype(int)
          print(classification_report(y_train, y_pred_train, digits=3))

          y_proba_test = model.predict(x_test)
          y_pred_test = (y_proba_test > THRESHOLD).astype(int)
          print(classification_report(y_test, y_pred_test, digits=3))
          ```
    * 회귀
        * ```python
          from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


          y_pred_train = model.predict(x_train)
          y_pred_test = model.predict(x_test)

          print("[Train]")
          print(f'-' * 50)
          print('r^2_score: ', r2_score(y_train, y_pred_train))
          print('RMSE:', np.sqrt(mean_squared_error(y_train, y_pred_train)))
          print('MAE:', mean_absolute_error(y_train, y_pred_train))
          print('MSE:', mean_squared_error(y_train, y_pred_train))
          print(f'-' * 50)
          print("[Test]")
          print(f'-' * 50)
          print('r^2_score: ', r2_score(y_test, y_pred_test))
          print('RMSE:', np.sqrt(mean_squared_error(y_test, y_pred_test)))
          print('MAE:', mean_absolute_error(y_test, y_pred_test))
          print('MSE:', mean_squared_error(y_test, y_pred_test))
          print(f'-' * 50)
          ```
* 해석
    * feature importance
        * ```python
          palette = sns.color_palette("turbo", 20)[::-1]
          f_imp = pd.Series(model.feature_importances_, index = x_train.columns)
          f_top20 = ftr_importances.sort_values(ascending=False)[:20]
          sns.barplot(x=f_top20, y=f_top20.index, palette=palette)
          plt.show()
          ```
    * shapley value
        * ```python
          import shap


          explainer = shap.TreeExplainer(model)
          shap_values = explainer.shap_values(x_test)
          shap.summary_plot(shap_values, x_test, plot_type='bar')
          shap.summary_plot(shap_values, x_test)
          plt.show()
          ```
    * ROC Curve (bin, multi)
        * ```python
          from sklearn.metrics import roc_curve, auc
          from sklearn.preprocessing import label_binarize


          y_pred_proba = model.predict_proba(x_test)
          if y_pred_proba.ndim == 1:
              y_pred_proba = y_pred_proba.reshape(-1, 1)
          classes = model.classes_
          y_test_bin = label_binarize(y_test, classes=classes)
          n_classes = y_test_bin.shape[1]
          
          for i in range(n_classes):
              fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_proba[:, i])
              roc_auc = auc(fpr, tpr)
              plt.plot(fpr, tpr, label=f'Class {classes[i]} (AUC = {roc_auc:.2f})')

          plt.plot([0, 1], [0, 1], 'k--', lw=1)
          plt.xlabel('False Positive Rate')
          plt.ylabel('True Positive Rate')
          plt.title('ROC Curve')
          plt.legend()
          plt.show()
          ```
    * 시각화 (reg)
        * ```python
          result = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred_test})

          sns.scatterplot(x=result['Real Values'], y=result['Predicted Values'])
          lim_min = min(result['Real Values'].min(), result['Predicted Values'].min())
          lim_max = max(result['Real Values'].max(), result['Predicted Values'].max())
          plt.xlim(lim_min, lim_max)
          plt.ylim(lim_min, lim_max)
          x = [lim_min, lim_max]
          y = [lim_min, lim_max]
          plt.plot(x, y, color='red')
          plt.show()
          ```
<br><br>



## `[🐍 Python algorithm]`

### [알고리즘 코딩 테스트]
* 시험 구성: 2 ~ 5시간, 2 ~ 7문제
* 보통 모든 문제를 다 맞춰야 통과된다.
* 최다 빈출 유형: 그리디, 구현, DFS, BFS
* 푸는 순서
    * 지문 정독, 요구사항과 출제자 의도 분석
    * 구체적으로 주석 적기 (아이디어, 시간복잡도, 변수)
    * 코딩
    * 제너럴 케이스, 엣지 케이스 대입
    * 시간 복잡도, 계산 복잡도 계산
    * 제출
<br><br>

### [준비 방법]
* 알고리즘 공부
    * 그리디, 구현(=시뮬레이션)
    * DFS, BFS
    * 정렬 (선택, 삽입, 퀵, 계수)
    * 이진탐색, DP
    * 최단경로 (다익스트라, 플로이드)
    * 기타 그래프 (MST)
    * 백트래킹 (?)
    * 투포인터 (?)
* 대표 유형 풀이
* 코드 암기
* 변형 문제 풀이
    * 1시간 내로 못풀면 답안지 확인
    * 1시간 내로 풀었어도 답안지 공부
    * 한달이 지나기 전에 같은 문제 풀이
    * 15분 내로 풀 수 있을 때까지 반복
* 하루에 4개 알고리즘씩 반복 연습
* (프로그래머스, 오답노트, 스터디)
<br><br>

### [시간 제한]
* 시간 제한은 보통 1 ~ 5초
* 1초 기준 N 범위, 시간 복잡도
    * N=500, O(N^3)
    * N=2000, O(N^2)
    * N=100K, O(NlogN)
    * N=10M, O(N)
* 파이썬 1초에 20M 번 계산 가능
* 알고리즘 별 시간 복잡도 일람
    * 
<br><br>

### [유형별 대표 용도]
* 그리디: 모든 경우 확인 (ex. 거스름돈, 1이 될 때까지)
* 구현: 생각을 코드로 (ex. 게임 구현, 문자열 처리)
* DFS: 모든 경로 탐색 (ex. 연결 요소 찾기)
* BFS: 최단 거리 찾기 (ex. 미로, 최소 간선 수로)
<br><br>

### [유형1: 그리디]
* 현재 상황에서 지금 당장 좋은 것만 고른다.
* 문제를 풀기 위한 최소한의 아이디어를 요구한다.
* 그리디를 쓰면 되는지에 대한 정당성 분석이 중요하다.
    * 진짜 최적의 해가 나오는가?
    * 최소한의 아이디어 도출 -> 정당한지 검토
* [예제](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>

### [유형2: 구현]
* 일반적으로: 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정.
* 코테에서는: 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제.
* 구현이라고 부르는 문제들
    * 알고리즘은 간단한데 코드가 지나치게 긴 문제
    * 실수 연산을 다루고 특정 소수점 자리까지 출력하는 문제
    * 문자열 처리 문제, 적절한 라이브러리 사용 문제
    * (=시뮬레이션, 완전탐색)
* 행렬 문제 팁
    * ```Python
      # 행렬 형태 (가상)
      # (0, 0), (0, 1), (0, 2)
      # (1, 0), (1, 1), (1, 2)
      # (2, 0), (2, 1), (2, 2)
      
      # 동, 북, 서, 남
      dx = [0, -1, 0, 1]
      dy = [1, 0, -1, 0]

      # 현재 위치
      x, y = 2, 2
      
      # 현재 위치를 동쪽 이동
      nx = x + dx[0]
      ny = y + dy[0]
      print(nx, ny)  # 현재 위치 출력
      ```
* 보드 문제 팁
    * ```Python
      # 보드 형태
      board = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
      ]
      
      # 동, 북, 서, 남
      dx = [0, -1, 0, 1]
      dy = [1, 0, -1, 0]

      # 현재 위치
      x, y = 0, 0

      # 말을 동쪽으로 이동
      nx = x + dx[0]
      ny = y + dy[0]
      board[x][y] = 0  # 현재 위치를 0으로
      board[nx][ny] = 1  # 새 위치를 1로
      print(board)  # 말의 위치 출력
      ```
* [예제](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>

### [유형3 & 4: DFS & BFS]
* 대표적인 그래프 탐색 알고리즘으로 DFS와 BFS가 있다.
* 탐색은 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정이다.
* 스택
    * 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조 (선입후출)
    * 입구와 출구가 동일한 형태
    * 파이썬의 기본 리스트가 스택, append와 pop 사용.
    * 데이터가 오른쪽으로 들어와서 쌓이다가 오른쪽에서 나간다.
    * ```Python
      stack = []

      # 삽입 5, 삽입 2, 삽입 3, 삽입 7, 삭제, 삽입 1, 삽입 4, 삭제
      stack.append(5)
      stack.append(2)
      stack.append(3)
      stack.append(7)
      stack.pop()
      stack.append(1)
      stack.append(4)
      stack.pop()

      print(stack[::-1])  # 최상단 원소부터 [1, 3, 2, 5]
      print(stack)  # 최하단 원소부터 [5, 2, 3, 1]
      ```
* 큐
    * 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조 (선입선출)
    * 입구와 출구가 모두 뚫려있는 터널 형태
    * 파이썬의 deque가 큐, append와 popleft 사용.
    * 데이터가 오른쪽으로 들어와서 왼쪽으로 나간다.
    * ```Python
      # 임포트 및 객체 선언 필수
      from collections import deque
      queue = deque()

      # 삽입 5, 삽입 2, 삽입 3, 삽입 7, 삭제, 삽입 1, 삽입 4, 삭제
      queue.append(5)
      queue.append(2)
      queue.append(3)
      queue.append(7)
      queue.popleft()
      queue.append(1)
      queue.append(4)
      queue.popleft()

      print(queue)  # 먼저 들어온 순서대로 출력 [3, 7, 1, 4]
      queue.reverse()
      print(queue)  # 역순 출력 [4, 1, 7, 3]
      ```
* 재귀 함수
    * 자기 자신을 다시 호출하는 함수
    * DFS나 BFS를 구현할 때 주로 사용한다.
    * 재귀 함수의 종료 조건을 반드시 명시한다.
    * ```Python
      def recursive_func(i):
          # 100번째 호출을 했을때 종료
          if i == 100:
              return
          print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출.')
          recursive_func(i+1)
          print(i, '번째 재귀함수를 종료합니다.')
      recursive_func(1)
      ```
    * 팩토리얼도 재귀함수로 구할 수 있으나 주의해야한다.
    * 팩토리얼과 유사하게 `점화식`을 공식 그대로 구현할 수 있다.
    * ```Python
      # 유클리드 호제법, 최대공약수 구하기
      def gcd(a, b):
          if a % b == 0:
              return b
          else:
              return gcd(b, a % b)
      print(gcd(192, 162))
      ```
* DFS
    * Depth-First Search, 깊은 부분을 우선적으로 탐색한다.
    * 스택 or 재귀함수를 이용하여 구현한다.
    * 수도 코드
        * 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
        * 스택의 최상단 노드에 방문하지 않은 노드가 하나라도 있다면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
        * 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
    * ```Python
      # 노드의 연결 정보를 표현
      graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
      ]

      # 노드의 방문 정보를 표현
      visited = [False] * 9

      # 메서드 정의
      def dfs(graph, v, visited):
          # 현재 노드를 방문 처리
          visited[v] = True
          print(f'{v} ')
          # 현재 노드와 연결된 다른 노드 재귀 방문
          for i in graph[v]:
              if not visited[i]:
                  dfs(graph, i, visited)  # 재귀가 핵심
      

      # DFS 호출
      dfs(graph, 1, visited)  # 1 2 7 6 8 3 4 5
      ```
* BFS
    * Breadth-First Search, 너비 부분을 우선적으로 탐색한다.
    * 큐를 이용하여 구현한다.
    * 수도 코드
        * 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
        * 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리 한다.
        * 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
    * ```Python
      # 노드의 연결 정보를 표현
      graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
      ]

      # 노드의 방문 정보를 표현
      visited = [False] * 9

      # 메서드 정의
      from collections import deque

      def bfs(graph, v, visited):
          # 큐를 사용하기 위해 덱 라이브러리 사용
          queue = deque()
          # 큐에 초기값 넣기
          queue.append(v)
          # 현재 노드를 방문 처리
          visited[v] = True
          # 큐가 없을 때까지 반복 (핵심)
          while queue:
              # 큐에서 한 원소 뽑아 출력
              v = queue.popleft()  # 안에서 리셋 (핵심)
              print(f'{v} ')
              # 아직 방문하지 않은 인접 원소 큐에 삽입, 방문처리
              for i in graph[v]:
                  if not visited[i]:
                      queue.append(i)
                      visited[i] = True
      

      # BFS 호출
      bfs(graph, 1, visited)  # 1 2 3 8 7 4 5 6
      ```
* [예제](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>



### [유형5: 정렬]
* 데이터를 특정 기준에 따라 순서대로 나열
* (ex. 크기가 작은 순서로 정렬 (=오름차순))
* 선택 정렬
    * 처리되지 않은 데이터 중 가장 작은 데이터를 `선택`한다.
    * 맨 앞에 있는 데이터와 선택 데이터를 바꾼다.
    * 시간 복잡도: O(N^2)
    * ```Python
      array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

      for i in range(len(array)):
          min_idx = i # 가장 작은 원소의 인덱스
          for j in range(i+1, len(array)):
              if array[min_idx] > array[j]:
                  min_idx = j
          # 스왑 연산
          array[i], array[min_idx] = array[min_idx], array[i]
      
      print(array) # 0 1 2 3 4 5 6 7 8 9
      ```
* 삽입 정렬
    * 처리되지 않은 데이터를 하나씩 골리 적절한 위치에 `삽입`한다.
    * 첫번째 데이터는 정렬된 것으로 판단하고 삽입할 위치를 고른다.
    * 시간 복잡도: O(N^2)
    * ```Python
      array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
      
      for i in range(1, len(array)):
          for j in range(i, 0, -1):  # i부터 0까지 마이너스 이동
              if array[j] < array[j-1]:  # 지금이 앞보다 작으면
                  # 스왑 연산
                  array[j], array[j-1] = array[j-1], array[j]
              else:  # 지금이 앞보다 크면 브레이크
                  break

      print(array) # 0 1 2 3 4 5 6 7 8 9
      ```
* 퀵 정렬
    * 기준 데이터를 정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
    * 퀵 정렬의 기본 값은 첫번째 데이터를 `기준(pivot)`으로 설정한다.
    * 왼쪽에서 출발하여 기준보다 큰 데이터를 선택한다.
    * 오른쪽에서 출발하여 기준보다 작은 데이터를 선택한다.
    * 두 데이터의 위치가 꼬이지 않은 경우 위치를 서로 변경한다.
    * 두 데이터의 위치가 엇갈리는 경우 `기준`과 작은 데이터를 서로 변경한다.
    * 이제 `기준`을 중심으로 좌우로 데이터 묶음이 분할 되었다.
    * 좌우의 데이터 묶음에 대하여 각각 퀵 정렬을 재귀적으로 실행한다.
    * 퀵 정렬은 표준으로 사용하는 정렬 알고리즘 이다.
    * 시간 복잡도: O(NlogN)
    * ```Python
      array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
      
      # 더 나은 구현
      def quick_sort(array):
          # 리스트가 하나 이하의 원소만 담고 있으면 종료
          if len(array) <= 1:
              return array
          pivot = array[0]  # 피벗 설정
          tail = array[1:]  # 피벗 제외 리스트

          left_side = [x for x in tail if x <= pivot]
          right_side = [x for x in tail if x > pivot]

          return quick_sort(left_side) + [pivot] + quick_sort(right_side)

      print(quick_sort(array))  # 0 1 2 3 4 5 6 7 8 9


      # 정석 구현
      def quick_sort(array, start, end):
          # 원소가 1개인 경우 종료
          if start >= end:
              return
          # 피벗은 첫 번째 원소
          pivot = start 
          left = start + 1
          right = end

          while(left <= right):
            
              # 피벗보다 큰 데이터를 찾을 때까지 반복
              while(left <= end and array[left] <= array[pivot]):
                  left += 1
            
              # 피벗보다 작은 데이터를 찾을 때까지 반복
              while(right > start and array[right] >= array[pivot]):
                  right -= 1
            
              # 엇갈렸다면 작은 데이터와 피벗을 교체
              if(left > right): 
                  array[right], array[pivot] = array[pivot], array[right]
            
              # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
              else: 
                  array [left], array[right] = array[right], array[left]
        
          # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
          quick_sort(array, start, right - 1)
          quick_sort(array, right + 1, end)

      quick_sort(array, 0, len(array) - 1)
      print(array)  # 0 1 2 3 4 5 6 7 8 9
      ```
* 계수 정렬
    * 데이터의 개수가 N, 데이터 중 최대 값이 K일 때 사용한다.
    * 특정한 조건이 만족해야 하지만 매우 빠르게 동작한다.
    * (조건: 동일한 값을 가지는 데이터가 여러 개 등장할 때)
    * 가장 작은 데이터 ~ 가장 큰 데이터 범위를 모두 담는 리스트를 생성한다.
    * 인덱스가 곧 값에 해당한다고 생각하고 몇번 등장하는지 `개수`를 센다.
    * 인덱스 별로 몇번 등장했는지에 대한 리스트가 생긴다.
    * 출력에서 리스트의 순서대로 인덱스를 값만큼 반복하여 출력한다.
    * ```Python
      # 든 원소의 값이 0보다 크거나 같다고 가정
      array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
      count = [0] * (max(array) + 1)

      # 각 데이터에 해당하는 인덱스의 값 카운팅
      for i in range(len(array)):
          count[array[i]] += 1

      # 등장한 횟수 만큼 인덱스 출력
      for i in range(len(count)):
         for j in range(count[i]):
              print(f'{i} ')
      ```
    * 시간 복잡도: O(N+K)
* [예제](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>










