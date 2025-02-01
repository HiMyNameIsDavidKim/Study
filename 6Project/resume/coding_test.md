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
    * shaply value
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
* 11개 알고리즘 공부
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
* 
<br><br>


