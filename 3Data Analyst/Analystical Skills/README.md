# Analystical Skills(분석법)

## `[데이터 분석]`

### [기본 프로세스]
* 시나리오 읽기
* 데이터 분석 기획
    * 문제정의: 문제현상, 문제로 인한 영향 정의
    * 기대효과: 해결 시 문제로 인한 영향의 변화를 정량적으로 작성
    * 해결방안: 해결에 사용할 분석 타겟, 분석 유형, 타겟에 의한 의사결정
    * 성과측정: 솔루션의 as-is to-be 정량 지표 비교
    * 운영: 솔루션 운영 프로세스 설계, 주기 설정, 모델 업데이트, 오류 대비
* 데이터 전처리
* 데이터 EDA
* 모델링 or 인사이트
<br><br>

### [가설 수립 후 인사이트 추출]
* 전체 feature 확인
* 개인적으로 생각하는 계산된 feature 추출
* 타겟에 대한 가설 수립 후 증명
<br><br>

### [Rule-base 기반 예측]
* 카테고리컬 feature 모두 사용
* 각 feature에서 가장 y비율이 높은 feature 찾기
* 각 feature에 부등호(==) 걸기
* 몇개 제거 하면서 제일 좋은 rule 찾기
* y(가입률) 얻어내기
* 기준 y(Mass 마케팅 가입률)와 비교
<br><br>

### [ML 기반 예측]
* 프로세스
    * X(feature 데이터)와 Y(정답 데이터) 만들기
    * 트레이닝셋 트레인셋 분할
    * 모델 인스턴스, 하이퍼 파라미터 설정
    * 학습, 예측
    * 성능 평가
    * (필요 시) 하이퍼 파라미터 자동 튜닝
    * 모델 해석
    * 모델 저장
* 모델에 넣을때는 문자로된 데이터는 원핫 인코딩 or 레이블 인코딩
* y 데이터와 상관성이 너무 높아 제외해야하는 데이터는 삭제
* 마지막에 모델을 해석하는 작업까지 해줘야 한다.
    * (이 모델은 어떤 특성으로 예측을 한다고 설명)
<br><br>

### [모델 평가]
* 모델 평가 방법
    * (예측값 vs 실제값) 스캐터 플랏 분석
    * (예측값 vs 실제값) 리니어 플랏 분석
<br><br>

### [모델 해석]
* feature importance
    * 간단하게 예측에 대한 기여도를 계산한다.
    * 덜 중요한 변수를 제거해 모델 단순화할 수 있다.
    * 장점: 빠르고 간단하다.
    * 단점: 과도하게 단순화되어 있다.
* shapley value
    * feature를 조합해가며 기여도를 계산한다.
    * 상호작용을 반영하고 개별 예측에 대한 기여도를 볼 수 있다.
    * feature의 값이 양의 관계인지 음의 관계인지 알 수 있다.
    * 장점: 비선형성을 반영한다.
    * 단점: 느리다.
* rule extraction
    * (개념, 의도 작성)
<br><br>


### [대표 프로젝트 유형]
* 데이터 EDA 및 인사이트 (대부분)
* 분류, 회귀 모델
* 이상 탐지 모델
    * 정의한 이상 데이터 패턴들 분석
    * 룰베이스로 로직 만들기
    * 모델링도 좋지만 도메인 지식으로 로직 만드는게 좋을 때가 많다.
* segmentation
    * 군집 모델
    * 특정한 특성을 가진 카테고리를 그루핑하여 분석
    * RFM 분석으로 segmentation할 수 있다.
<br><br>



## `[Business Analysis]`

### [A/B 테스트]
* 
<br><br>

### [퍼널 분석]
* 
<br><br>

### [리텐션 분석]
* 
<br><br>

### [Coustomer LifeTime Value 분석]
* 
<br><br>

### [LTV 분석]
* 
<br><br>

### [AARRR 분석]
* 
<br><br>

### [RFM 분석]
* 고객을 점수화 해서 서비스 등급 구간(grade) 부여
* R: recency, 최근성, 얼마나 최근에 구매
* F: frequency, 빈도, 얼마나 자주 구매
* M: monetary, 금액, 구매 금액
* 그루핑을 통해 서비스 이용 수준 측정 가능
* 고객마다 RFM이 어떻게 변하는지 관찰
* R은 낮을수록 좋기 때문에 노멀라이즈 시 (1-R) 해주기
<br><br>

### [코호트 분석]
* 
<br><br>



## `[모델링]`
* 이론은 [`ML 트리 부분`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/4ML/ML&DL) 참고
<br><br>

### [LightGBM]
* 대규모 데이터에 적합하다.
* 속도가 빠르고, CPU만 사용한다.
* leaf-wise로 트리가 성장한다.
* 실전 팁
    * 다른 파라미터 다 조정하고 마지막에 에포크 조절한다.
    * 생각보다 판정 threshold 영향이 크다.
    * 랜덤포레스트랑 메서드 이름이 달라서 에러 터지니 주의한다.
<br><br>

### [XGBoost]
* 소규모 데이터에 적합하다.
* 속도가 느리고, GPU 가속을 지원한다.
* depth-wise로 트리가 성장한다.
* 실전 팁
    * 
<br><br>

### [TabNet]
* 딥러닝 어탠션 매커니즘 기반이다.
* 컬럼과 샘플이 엄청나게 많아야 효과가 좋다.
* 내장된 분석 메서드가 있다.
* 실전 팁
    * batch 늘리면 속도 빨라진다.
    * 파라미터가 매우 예민하다.
    * 얼리스탑을 잘 제어해야 한다.
<br><br>

### [deepSVDD]
* 비지도 학습 기반 이상 탐지 알고리즘이다.
* 레이블이 필요 없고 데이터가 많아도 사용할 수 있다.
* SVDD를 딥러닝 아키텍처와 결합했다.
* SVDD (Support Vector Data Description)
    * 대부분의 데이터를 포함하는 최소 크기의 구를 찾는 알고리즘.
* 실전 팁
    * 
<br><br>



## `[분석 코드 baseline]`

### [데이터 전처리 4단계]
* 데이터 형태 확인
    * df.shape
* 데이터 타입 확인
    * df.info()
    * 숫자로 보이는데 문자인 경우 확인
    * 문자로 보이는데 숫자인 경우 확인
    * object 타입(스트링) 확인
    * 인트 플롯 확인
* NULL 값 확인
    * df.isnull().sum()
* outlier 확인
    * df.describe()
    * 특히 min, max에 음수값 있는지 확인
    * 도메인 지식 기반으로 처리
<br><br>

### [EDA baseline]
* `categorical` -> `numerical` -> `total`
* 데이터 유형 분리
    * ```python
      cols_categorical = df.select_dtypes(include=object).columns
      cols_numerical = df.select_dtypes(exclude=object).columns
      ```
* Boolian 처리
    * ```python
      cols_bool = ['col1']
      for col in cols_bool:
          cols_numerical = cols_numerical.drop(col)
          cols_categorical = cols_categorical.append(pd.Index([col]))
      ```
* categorical
    * 다차원 바 플랏
        * y가 이산형
            * ```python 
              plt.style.use(['seaborn-v0_8'])
              for col in cols_categorical:
                  print(f'-'*50)
                  print(f'##### {col} Distribution #####')
                  ratio_1 = df[df["y"] == 1].groupby(col).size() / df.groupby(col).size() * 100
                  g = sns.catplot(x="y", hue="y", col=col, col_wrap=4, data=df,
                              kind="count", height=3.5, aspect=.8,  palette='deep', legend=False)
                  for ax in g.axes.flat:
                      cat = ax.get_title().split(" = ")[-1]
                      if cat in ratio_1:
                          ax.text(0.5, 0.94,
                                  f"y Rate: {ratio_1[cat]:.2f}%", 
                                  ha="center", va="bottom", transform=ax.transAxes, fontsize=10, color="blue")
                  plt.show()
                  print(f'-'*50)
              ```
        * y가 연속형
            * ```python 
              plt.style.use(['seaborn-v0_8'])
              for col in cols_categorical:
                  print(f'-'*50)
                  print(f'##### {col} Distribution #####')
                  sns.barplot(x=col, y="y", data=df, color="skyblue", edgecolor=".6", label="Sales")
                  plt.gcf().set_size_inches(25, 3)
                  plt.xticks(fontsize=16)
                  plt.legend()
                  plt.show()
                  print(f'-'*50)
              ```
* numerical
    * 상관계수 히트맵
        * ```python
          plt.style.use(['seaborn-v0_8'])
          sns.heatmap(df[cols_numerical].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
          plt.show()
          ```
    * 바이올린 플랏
        * ```python
          n_cols = 4
          n_rows = (len(cols_numerical) + n_cols - 1) // n_cols
          fig, axs = plt.subplots(n_rows, n_cols, figsize=(16, 4 * n_rows))
          axs = axs.flatten()
          plt.style.use(['seaborn-v0_8'])
          for i, col in enumerate(cols_numerical):
              sns.violinplot(x='y', y=col, data=df, hue='y', legend=False, 
                density_norm='width', inner='quartile', ax=axs[i], palette='deep')
              axs[i].set_title(f'Violin Plot of {col}', fontsize=14)
              axs[i].set_xlabel(col, fontsize=12)
          for j in range(i + 1, len(axs)):
                  axs[j].axis('off')
          plt.tight_layout()
          plt.show()
          ```
    * 산점도
        * y가 이산형
            * ```python
              plt.style.use(['seaborn-v0_8'])
              print(f'-'*50)
              print(f'##### Pair Plot #####')
              plt.style.use(['seaborn-v0_8'])
              df_temp = df.copy()
              df_temp = df_temp[cols_numerical[-5:]]

              # df_1 = df_temp[df_temp['y'] == 1]
              # df_1 = df_temp[df_temp['y'] == 1].sample(n=len(df_1)//10, random_state=42)
              # df_0 = df_temp[df_temp['y'] == 0].sample(n=len(df_1), random_state=42)
              # df_temp = pd.concat([df_1, df_0])

              plt.figure(figsize=(10, 8), dpi=80)
              sns.pairplot(df_temp, kind="scatter", hue="y", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
              plt.show()
              print(f'-'*50)
              ```
        * y가 연속형
            * ```python
              plt.style.use(['seaborn-v0_8'])
              for col in cols_numerical:
                  print(f'-'*50)
                  print(f'##### {col} Scatter Plot #####')
                  sns.scatterplot(x=col, y='y', data=df)
                  plt.show()
                  print(f'-'*50)
              ```
* 시계열
    * categorical
        * 라인 그래프 (카운트, y 집계)
            * ```python
              df['Date_1'] = df["Date"].dt.strftime("%Y-%m")
              plt.style.use(['seaborn-v0_8'])
              for col in cols_categorical:
                  print(f'-'*50)
                  print(f'##### {col} Line #####')
                  df_temp = pd.DataFrame(df.groupby([col, 'Date_1'], as_index=False)['UniqueID'].count())  # sum, mean
                  sns.lineplot(x='Date_1', y='UniqueID', hue=col, data = df_temp)
                  plt.xticks(rotation=90)
                  plt.show()
                  print(f'-'*50)
              ```
        * 히스토그램 (카운트, y 집계)
            * ```python
              df['Date_1'] = df["Date"].dt.strftime("%Y-%m")
              plt.style.use(['seaborn-v0_8'])
              for col in cols_categorical:
                  print(f'-'*50)
                  print(f'##### {col} Line #####')
                  df_temp = pd.DataFrame(df.groupby([col, 'Date_1'], as_index=False)['UniqueID'].count())  # sum, mean
                  sns.barplot(x='Date_1', y='UniqueID', hue=col, data = df_temp)
                  plt.xticks(rotation=90)
                  plt.show()
                  print(f'-'*50)
              ```
    * numerical
        * 라인 그래프 (값 그대로)
            * ```python
              df['Date_1'] = df["Date"].dt.strftime("%Y-%m")
              plt.style.use(['seaborn-v0_8'])
              for col in cols_numerical:
                  print(f'-'*50)
                  print(f'##### {col} Line #####')
                  plt.plot(df['Date_1'], df[col])
                  plt.xlabel('Date_1')
                  plt.ylabel(col)
                  plt.show()
                  print(f'-'*50)
              ```
        * 라인 그래프 (y랑 같이 보기)
            * ```python
              df['Date_1'] = df["Date"].dt.strftime("%Y-%m")
              plt.style.use(['seaborn-v0_8'])
              for col in cols_numerical:
                  print(f'-'*50)
                  print(f'##### {col} Line #####')
                  fig, ax1 = plt.subplots()
                  ax1.plot(df['Date'], df['y'], color='blue')
                  ax2 = ax1.twinx()
                  ax2.plot(df['Date'], df[col], color='red')
                  fig.legend()
                  plt.show()
                  print(f'-'*50)
              ```
    * 연별 월별 히스토그램
        * ```python
          df['Date_year'] = df["Date"].dt.strftime("%Y")
          df['Date_month'] = df["Date"].dt.strftime("%m")
          plt.style.use(['seaborn-v0_8'])
          df_temp = pd.DataFrame(df.groupby(['Date_year', 'Date_month'], as_index=False)['UniqueID'].count())
          sns.barplot(x='Date_month', y='UniqueID', hue='Date_year', data = df_temp)
          plt.show()
          ```
    * 히트맵
        * ```python
          df['Date_year'] = df["Date"].dt.strftime("%Y")
          df['Date_month'] = df["Date"].dt.strftime("%m")
          df_pivot = df.pivot_table(index='Date_month', columns='Date_year', values='CPI')
          sns.heatmap(df_pivot, cmap="Blues", cbar=True)
          plt.show()
          ```
<br><br>

### [군집추출 baseline]
* 
<br><br>

### [머신러닝 baseline]
* `모델링` -> `평가` -> `해석`
* 모델링
    * 분류
        * 랜덤 포레스트
        * ```python
          from sklearn.model_selection import train_test_split
          from sklearn.preprocessing import LabelEncoder
          from sklearn.ensemble import RandomForestClassifier


          df_temp = df.copy()
          X = df_temp.drop('y', axis=1)
          Y = df_temp['y']

          cols_drop = ['id']
          for col in cols_drop:
              X.drop(col, axis=1, inplace=True)

          cols_date = ['date_1', 'date_2']
          for col in cols_date:
              X[f'week_{col}'] = X[col].dt.dayofweek
              X[f'month_{col}'] = X[col].dt.month
              X[col] = pd.to_datetime(X[col]).astype(int) / 10**9

          for column in X.columns:
              if X[column].dtype == object:
                  le = LabelEncoder()
                  X[column] = le.fit_transform(X[column])

          x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
          model = RandomForestClassifier(random_state=42)
          model.fit(x_train, y_train)
          ```
        * LightGBM
        * ```python
          from sklearn.model_selection import train_test_split
          from sklearn.preprocessing import LabelEncoder
          from sklearn.ensemble import RandomForestClassifier


          LEARNING_RATE = 3e-2
          NUM_BOOST_ROUND = 500
          THRESHOLD = 0.3

          params = {
              "learning_rate": LEARNING_RATE,
              "num_leaves": 16,
              "max_depth": 6,
              "drop_rate": 0.3,
              "max_drop": 50,
              "feature_fraction": 0.5,
              "min_child_samples": 10,
              "min_child_weight": 0.01,
              "subsample": 0.9,
              "is_unbalance": False,
              "max_bin": 256,
              "verbosity": -1,
              "min_split_gain": 0,
              "boosting_type": 'gbdt',
              "objective": "binary",
              'metric': 'binary_logloss',
              "seed": 42,
              # "early_stopping_rounds": 200,
          }

          df_temp = df.copy()
          X = df_temp.drop('y', axis=1)
          Y = df_temp['y']

          cols_drop = ['id']
          for col in cols_drop:
              X.drop(col, axis=1, inplace=True)

          cols_date = ['date_1', 'date_2']
          for col in cols_date:
              X[f'week_{col}'] = X[col].dt.dayofweek
              X[f'month_{col}'] = X[col].dt.month
              X[col] = pd.to_datetime(X[col]).astype(int) / 10**9

          for column in X.columns:
              if X[column].dtype == object:
                  le = LabelEncoder()
                  X[column] = le.fit_transform(X[column])

          x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
          ds_train = lgb.Dataset (x_train, label = y_train)
          ds_test = lgb.Dataset (x_test, label = y_test)

          model = lgb.train(
              params,
              ds_train,
              NUM_BOOST_ROUND,
              # valid_sets=[ds_test],
              # valid_names=['test'],
          )
          ```
        * XGBoost
        * ```python
          from sklearn.model_selection import train_test_split
          from sklearn.preprocessing import LabelEncoder
          from sklearn.ensemble import RandomForestClassifier


          df_temp = df.copy()
          X = df_temp.drop('y', axis=1)
          Y = df_temp['y']

          cols_drop = ['id']
          for col in cols_drop:
              X.drop(col, axis=1, inplace=True)

          cols_date = ['date_1', 'date_2']
          for col in cols_date:
              X[f'week_{col}'] = X[col].dt.dayofweek
              X[f'month_{col}'] = X[col].dt.month
              X[col] = pd.to_datetime(X[col]).astype(int) / 10**9

          for column in X.columns:
              if X[column].dtype == object:
                  le = LabelEncoder()
                  X[column] = le.fit_transform(X[column])

          x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
          model = xgb.XGBClassifier(objective='multi:softmax', num_class=len(Y.unique()), random_state=42)
          model.fit(x_train, y_train)
          ```
        * TabNet
        * ```python
          !pip install -q pytorch-tabnet==3.1.1
          ```
        * ```python
          from sklearn.model_selection import train_test_split
          from sklearn.preprocessing import LabelEncoder
          from pytorch_tabnet.tab_model  import TabNetClassifier
          from pytorch_tabnet.metrics import Metric
          from sklearn.metrics import f1_score
          import torch


          device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
          print(f"Using device: {device}")
          
          CAT_EMB_DIM = 10  # cat_dim의 배수 추천
          N_A = 8
          N_D = 8
          LEARNING_RATE = 3e-2
          BATCH_SIZE = 2048
          EPOCH = 60
          PATIENCE = EPOCH
          NUM_WORKERS = 1

          df_temp = df.copy()
          X = df_temp.drop('y', axis=1)
          Y = df_temp['y']

          cols_drop = ['id']
          for col in cols_drop:
              X.drop(col, axis=1, inplace=True)

          cols_date = ['date_1', 'date_2']
          for col in cols_date:
              X[f'week_{col}'] = X[col].dt.dayofweek
              X[f'month_{col}'] = X[col].dt.month
              X[col] = pd.to_datetime(X[col]).astype(int) / 10**9

          cat_dims = []
          cat_idxs = []
          for column in X.columns:
              if X[column].dtype == object:
                  le = LabelEncoder()
                  X[column] = le.fit_transform(X[column])
                  cat_dims.append(len(le.classes_))
                  cat_idxs.append(X.columns.get_loc(column))

          x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
          
          x_train_tab = x_train.values
          y_train_tab = y_train.values
          x_test_tab = x_test.values
          y_test_tab = y_test.values

          class F1_Score(Metric):
              def __init__(self):
                  self._name = "F1_score"
                  self._maximize = True

              def __call__(self, y_true, y_score):
                  y_pred = np.argmax(y_score, axis=1)
                  score = f1_score(y_true, y_pred, average='macro')
                  return score


          model = TabNetClassifier(
            cat_idxs=cat_idxs,
            cat_dims=cat_dims,
            cat_emb_dim=CAT_EMB_DIM,
            n_a=N_A,
            n_d=N_D,
            optimizer_fn=torch.optim.Adam,
            optimizer_params=dict(lr=LEARNING_RATE),
            scheduler_fn=torch.optim.lr_scheduler.CosineAnnealingLR,
            scheduler_params={"T_max": EPOCH},
          )

          model.fit(
            X_train=x_train_tab, y_train=y_train_tab,
            eval_set=[(x_train_tab, y_train_tab), (x_test_tab, y_test_tab)],
            eval_name=['train', 'test'],
            eval_metric=['logloss','F1_score'],
            max_epochs=EPOCH , patience=PATIENCE,
            batch_size=BATCH_SIZE,
            virtual_batch_size=BATCH_SIZE,
            num_workers=NUM_WORKERS,
            drop_last=False,
          )
          ```
    * 회귀
        * ```python
          from sklearn.model_selection import train_test_split
          from sklearn.preprocessing import LabelEncoder
          from sklearn.ensemble import RandomForestClassifier


          df_temp = df.copy()
          X = df_temp.drop('y', axis=1)
          Y = df_temp['y']

          cols_drop = ['id']
          for col in cols_drop:
              X.drop(col, axis=1, inplace=True)

          cols_date = ['date_1', 'date_2']
          for col in cols_date:
              X[f'week_{col}'] = X[col].dt.dayofweek
              X[f'month_{col}'] = X[col].dt.month
              X[col] = pd.to_datetime(X[col]).astype(int) / 10**9

          for column in X.columns:
              if X[column].dtype == object:
                  le = LabelEncoder()
                  X[column] = le.fit_transform(X[column])

          x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
          model = RandomForestRegressor(n_estimators=500, max_depth=4, random_state=42)
          model.fit(x_train, y_train)
          ```
* 평가
    * 분류
        * acc
            * ```python
              from sklearn.metrics import accuracy_score


              y_pred_test = model.predict(x_test)
              accuracy = accuracy_score(y_test, y_pred_test)
              print(f"Accuracy: {accuracy*100:.2f}%")
              ```
        * report
            * 기본
            * ```python
              from sklearn.metrics import classification_report


              y_pred_train = model.predict(x_train)
              print(classification_report(y_train, y_pred_train))

              y_pred_test = model.predict(x_test)
              print(classification_report(y_test, y_pred_test))
              ```
            * LightGBM
            * ```python
              from sklearn.metrics import classification_report


              y_pred_train = model.predict(x_train)
              for i in range(0, len(y_pred_train)):
                  if y_pred_train[i] >=THRESHOLD:
                      y_pred_train[i] = 1
                  else:
                      y_pred_train[i] = 0
              print(classification_report(y_train, y_pred_train, digits=3))


              y_pred_test = model.predict(x_test)
              for i in range(0,len(y_pred_test)):
                  if y_pred_test[i] >=THRESHOLD:
                     y_pred_test[i] = 1
                  else:
                      y_pred_test[i] = 0
              print(classification_report(y_test, y_pred_test, digits=3))
              ```
            * TabNet
            * ```python
              from sklearn.metrics import classification_report

              
              y_train_pred_tab = model.predict(x_train_tab)
              print(classification_report(y_train_tab, y_train_pred_tab))

              y_test_pred_tab = model.predict(x_test_tab)
              print(classification_report(y_test_tab, y_test_pred_tab))
              ```
    * 회귀
        * r^2, mse
            * ```python
              from sklearn.metrics import r2_score, mean_squared_error


              y_pred_train = model.predict(x_train)
              y_pred_test = model.predict(x_test)

              r2_train = r2_score(y_train, y_pred_train)
              r2_test = r2_score(y_test, y_pred_test)
              print('r^2_score(train): ', r2_train)
              print('r^2_score(test): ', r2_test)
              print('')
              mae_train = mean_squared_error(y_train, y_pred_train)
              mae_test = mean_squared_error(y_test, y_pred_test)
              print('mae_train(train): ', mae_train)
              print('mae_test(test): ', mae_test)
              ```
* 해석
    * feature importance
        * 간단하게 예측에 대한 기여도를 계산한다.
        * ```python
          sns.set(style="darkgrid")
          palette = sns.color_palette("turbo", 20)[::-1]
          ftr_importances_values = model.feature_importances_  # LightGBM: model.feature_importance()
          ftr_importances = pd.Series(ftr_importances_values, index = x_train.columns)
          ftr_top20 = ftr_importances.sort_values(ascending=False)[:20]
          sns.barplot(x=ftr_top20, y=ftr_top20.index, palette=palette)
          plt.show()
          ```
    * ROC Curve (분류)
        * 모델의 전반적인 분류 성능이 좋다.
        * ```python
          from sklearn.metrics import roc_curve, auc
          from sklearn.preprocessing import label_binarize


          y_pred_proba = model.predict_proba(x_test)  # LightGBM: model.predict(X, output_margin=False)
          if Y_predict.ndim == 1:
              Y_predict = Y_predict.reshape(-1, 1)
          classes = model.classes_
          y_test_bin = label_binarize(y_test, classes=classes)
          n_classes = y_test_bin.shape[1]
          
          plt.style.use(['seaborn-v0_8'])
          plt.figure()
          for i in range(n_classes):
              fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_proba[:, i])
              roc_auc = auc(fpr, tpr)
              plt.plot(fpr, tpr, label=f'Class {classes[i]} (AUC = {roc_auc:.2f})')

          plt.plot([0, 1], [0, 1], 'k--', lw=1)
          plt.xlim([0.0, 1.0])
          plt.ylim([0.0, 1.05])
          plt.xlabel('False Positive Rate')
          plt.ylabel('True Positive Rate')
          plt.title('ROC Curve')
          plt.legend(loc="lower right")
          plt.show()
          ```
    * AUROC 만 (분류)
        * ```python
          from sklearn.metrics import roc_auc_score


          y_pred_proba = model.predict_proba(x_test)  # LightGBM: model.predict(X, output_margin=False)
          auroc_ovo = roc_auc_score(y_test, y_pred_proba, multi_class='ovo')
          print(f"AUROC (ovo): {auroc_ovo:.4f}")
          ```
    * Cumulative Gains Curve (분류)
        * 가장 잘 예측한 샘플들에서 실제로 많은 중요한 결과를 찾았다.
        * ```python
          y_test = y_test.to_numpy()
          y_pred_proba = model.predict_proba(x_test)  # LightGBM: model.predict(X, output_margin=False)
          sorted_indices = np.argsort(y_pred_proba)[::-1]
          sorted_y_test = y_test[sorted_indices]
          cumulative_gains = np.cumsum(sorted_y_test) / np.sum(sorted_y_test)

          plt.plot([0, len(y_test)], [0, 1], linestyle="--", label="Random Model")
          plt.plot(np.arange(1, len(y_test) + 1), cumulative_gains, label="LightGBM Model", color='blue')
          plt.title('Cumulative Gains Curve')
          plt.xlabel('Percentage of Samples (%)')
          plt.ylabel('Cumulative Gains (%)')
          plt.legend()
          plt.grid(True)
          plt.show()
          ```
    * shaply value
        * 비선형을 고려한 기여도를 계산하고 상관성의 부호를 확인한다.
        * ```python
          import shap


          explainer = shap.TreeExplainer(model)
          shap_values = explainer.shap_values(x_test)
          shap.summary_plot(shap_values, x_test, plot_type='bar')
          shap.summary_plot(shap_values, x_test)
          plt.show()
          ```
    * rule fit
        * top5 feature 로 다시 학습한 후 레시피를 도출한다.
        * ```python
          from rulefit import RuleFit


          features = ['input_top5_features']
          threshold = 0.2  # adjust

          x_train_rule = x_train[features]
          rulefit = RuleFit(tree_size=8, sample_fract='default', max_rules=300, random_state=42)
          rulefit.fit(x_train_rule.values, y_train.values.ravel(), x_train_rule.columns)
          y_pred = rulefit.predict(x_train_rule.values)
          y_pred_binary = (y_pred > threshold).astype(int)
          print(classification_report(y_train, y_pred_binary, digits=3))

          rules = rulefit.get_rules()
          rules = rules[rules.coef != 0]
          table_temp = rules.sort_values("importance", ascending=False).head(5)
          display(table_temp)
          print(f'########## Rule Extraction ##########')
          [print(i) for i in table_temp['rule']]
          ```
    * 시각화 (회귀)
        * ```python
          pd.options.display.float_format = '{:.2f}'.format
          result = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred_test})
          result['diff'] = result['Real Values'] - result['Predicted Values']

          sns.set(style="darkgrid")
          sns.scatterplot(x=result['Real Values'], y=result['Predicted Values'])
          lim_min = min(result['Real Values'].min(), result['Predicted Values'].min())
          lim_max = max(result['Real Values'].max(), result['Predicted Values'].max())
          plt.xlim(lim_min, lim_max)
          plt.ylim(lim_min, lim_max)
          x = [lim_min, lim_max]
          y = [lim_min, lim_max]
          plt.plot(x, y, color='red')
          plt.show()

          result = result.reset_index(drop=True)
          plt.plot(result.index, result['Real Values'], label='Real')
          plt.plot(result.index, result['Predicted Values'], label='Pred')
          plt.legend()
          plt.show()
          ```
    * confusion matrix (다중분류)
        * ```python
          from sklearn.metrics import confusion_matrix


          plt.style.use(['seaborn-v0_8'])
          cm = confusion_matrix(y_test, y_pred_test)
          plt.figure()
          sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
          plt.xlabel('Predicted Label')
          plt.ylabel('True Label')
          plt.title('Confusion Matrix')
          plt.show()
          ```
    * PCA 차원 축소
        * 높을수록 좋은 값
        * 낮은 경우 표준화, 정규화, 이상치 제거, 상관계수 높은 특성 제거
        * ```python
          from sklearn.decomposition import PCA
          from sklearn.preprocessing import StandardScaler

          N = 2
          scaler = StandardScaler()
          X_scaled = scaler.fit_transform(X)
          pca = PCA(n_components=N)

          X_pca = pca.fit_transform(X_scaled)
          for i in range(N):
              component_str = [f'{value:.2f}' for value in pca.components_[i]]
              ratio_str = f'{pca.explained_variance_ratio_[i]:.2f}'
              print(f'Comp {i+1} config: {component_str}')
              print(f'Comp {i+1} ratio: {ratio_str}')
          
          plt.style.use(['seaborn-v0_8'])
          plt.scatter(X_pca[:, 0], X_pca[:, 1])
          plt.xlabel('Principal Comp 1')
          plt.ylabel('Principal Comp 2')
          plt.show()
          ```
* 개선
    * 자동 튜닝
        * ```python
          from sklearn.model_selection import GridSearchCV


          param_grid = {
            'n_estimators': [100, 200, 300],  # 트리 개수
            'max_depth': [None, 10, 20],  # 트리의 최대 깊이
            'min_samples_split': [2, 5, 10],  # 노드를 분할하기 위한 최소 샘플 수
            'min_samples_leaf': [1, 2, 4],  # 리프 노드의 최소 샘플 수
          }

          grid_cv = GridSearchCV(model, param_grid, cv=3, n_jobs=-1, scoring='f1')
          grid_cv.fit(x_train, y_train)
          print(f'The best params: {grid_cv.best_params_}')
          print(f'The best score: {grid_cv.best_score_:.4f}')
          ```
<br><br>

### [collaborative 필터링 baseline]
* 추천 알고리즘 모델
* 
<br><br>

### [이상탐지 baseline]
* 
<br><br>



## `[개념 및 이론]`

### [개념 용어]
* 데이터 EDA
    * Exploratory Data Analysis, 탐색적 데이터 분석
    * 데이터를 이해하고 분석하기 위해 사용하는 초기 과정
    * 데이터의 패턴, 특성, 이상치(Outlier), 숨겨진 관계 등을 확인
* Data mart
    * feature 데이터를 모아둔 데이터베이스
* KPIs
    * Key Performance Indicators
    * 목표, 지표, 고과
* 증감률(%) vs 퍼센티지 포인트(%p)
    * 증감률
        * %, 이전 기간 대비 현재 기간의 값 변화
        * (현재 - 이전)/(이전) * 100
        * ex. 매출 성장률
    * 퍼센티지 포인트
        * %p, 퍼센트 자체의 증감을 나타내는 단위
        * (현재% - 이전%)
        * 마켓 쉐어 퍼센티지 증가
    * 증감률은 값을 기준으로 변화가 어떤지 볼 때 사용한다.
    * 퍼센티지 포인트는 퍼센트 자체의 변화를 표현하기 위해 사용한다.
* Adhoc 분석
    * 즉시 필요에 맞춰 수행하는 비정형 데이터 분석
    * 목적은 `원하는 인사이트`를 `빠르게` 도출하는 것이다.
    * 일시적이고 즉흥적으로 분석을 진행한다.
    * 예기치 못한 상황, 성능 즉시 확인, 경영진 질문 대응 등이 있다.
<br><br>

### [도메인 지식 메모]
* 콘텐츠에서 KPIs
    * MAU: monthly active users, 한달동안 앱에서 활동하는 순 유저 수
    * 월 트랜젝션 AMT: 트랜젝션으로 발생한 매출(amount) 양
* 광고 지표
    * CTR: click through rate, (광고 클릭수)/(광고 노출수) * 100
    * ROAS: return on ad spend, (광고로 인한 수익)/ (광고 비용)
    * Cost for Acquisition: ROAS와 같은 지표
* 웹,앱 지표
    * retention: 남아있는 유저 비율, (특정 기간 이후의 사용자 수)/(처음 서비스를 이용한 사용자 수) * 100
    * DAU: daily active users, 하루 기준 유니크 유저 수
    * click: 몇번 클릭 했는지
    * time spent: 시간을 얼마나 소요했는지
* 마케팅 지표
    * CAC: customer aquisition cost, (특정 기간동안 총 마케팅 비용)/(동기간 동안 획득한 새 고객 수)
    * CR: conversion rate, (구매 건수)/(방문자 수) * 100
    * CLTV: customer lifetime value, (고객 당 평균 수익) * (고객 관계 유지 평균 기간)
    * NPS: net romoter score, (추천 응답자 비율) - (비추천 응답자 비율)
* 금융 지표
    * ROI: return on investment, (투자로 얻은 수익 - 투자비)/(투자비) * 100
    * CAGR: compound annual growth rate, (말기 가치)/(초기 가치)^(1/기간) - 1
* 이커머스 지표
    * 객단가: 고객 1명이 평균적으로 얼마를 구입하는지, (주문빈도) * (건당주문금액)
    * ARPU: avg revenue per user, (매출) / (사용자 수)
    * ARPPU: avg revenue per paid user, (매출) / (구매자 수)
    * YTD 총계: 해당 연도 안에서 해당 월까지의 누적 매출, 연매출 목표까지 얼마나 달성했는지 보려는 의도
    * YTD 성장률: 올해 YTD 총계 vs 작년 YTD 총계
    * YoY: year of year, 전년 대비 비교
    * 연평균 성장률: 해당 기간동안 평균적으로 얼마나 성장 했는지에 대한 지표, 기하평균으로 계산
* 고객행동 지표
    * Funnel: 사용자의 방문부터 구매까지 과정을 단계별로 보는 방법
    * 단계별로 지표를 설계하고 분석해서 어떤 단계에 문제가 있는지 찾는다.
    * AARRR 프레임워크
        * Acquisition, 유입, 고객을 획득
            * DAU⭐️: 유입 지표, 일간 활성 유저
            * MAU: 유입 지표, 월간 활성 유저
        * Activation, 활성화, 고객이 주요 기능을 사용
            * 평균 PV: 고객이 본 평균 페이지 수
            * 평균 체류시간: (전체 세션 시간) / (활성 유저)
            * 회원가입 고객 수: 신규 가입 수
            * conversion rate⭐️: 전환률, (기능사용수) / (방문자수)
            * bounce rate: 이탈률, 아무 행동 없이 이탈한 비율
        * Retention, 유지, 고객이 꾸준히 이용
            * 코호트(동질 집단)을 기준으로 확인한다.
            * retention rate⭐️: 잔존율, (재방문고객) / (특정시점 방문고객)
            * stickness: 고착도, 얼마나 자주 방문, (DAU) / (MAU)
        * Referral, 추천, 고객이 자발적으로 서비스를 추천
            * 공유수, 리뷰수, 친구초대수
            * 바이럴 계수: 기존 고객이 만든 신규 고객 수
        * Revenue, 수익, 고객들로부터 수익 창출
            * GMV: 총 거래액
            * 구매전환율: (구매수) / (방문자수)
            * LTV: 고객 생애 가치, 한명의 고객에게 기대되는 수익
            * ARPU: avg revenue per user, (매출) / (사용자 수)
            * ARPPU: avg revenue per paid user, (매출) / (구매자 수)
* 유통 물류 용어
    * 구매 -> 재고 -> 판매 -> 출고
    * 재고: 입고량 - 판매량
    * 권장 판매가(list price) -> 할인 -> 실 판매가(net price)
    * SKU: stock keeping unit, 재고 관리를 위한 최소 단위 코드
    * Unit Quantity: 상품의 개수
    * PO: purchase order, 구매 및 발주, 입고를 위해 하는 process
    * SCM: supply chain management, 공급망 관리
    * 공급망 구성: 브랜드, 벤더, 운송업체, 물류창고
* 유통 물류 지표
    * DOC: day of coverage, 재고로 몇일 판매 가능한지, (재고량) / (하루 판매량)
    * DOC가 낮으면 빨리 소진 되니까 재고 전환율이 높은 것이다.
    * SKU grade: 잘팔리는 활성 재고를 상위 등급으로 부여한다.
<br><br>

### [통계 요약]
* 기술통계량
    * 데이터의 전반적인 특성을 이해
    * 분석의 방향성을 결정
    * 중심의 경향성: 평균, 중앙값, 최빈값
        * 평균, (장) 가장 대표, (단) outlier 영향 큼
        * 중앙값, (장) outlier 영향 적음, (단) 모수 크면 무의미
        * 최빈값, (장) 숫자가 아니어도 사용 가능
    * 퍼짐의 척도: 범위, 분산, 표준편차
        * 분산, (장) 가장 대표, (단) 제곱으로 직관성 저하
        * 표준편차, (장) 루트로 직관성 높음
    * 형태의 척도: skewness, kurtosis
        * skewness, 왜도, 좌우로 치우쳐진 정도
        * kurtosis, 첨도, 데이터가 얼마나 뾰족한지
    * 위치의 척도: 백분위수, 4분위수
        * 백분위수, 특정 백분율이 위치하는 값, 시그마
        * 4분위수, 25%, 50%, 75%가 위치하는 값
* 통계적 추론: 표본 데이터를 이용하여 모집단의 정보를 추론하는 과정
* 중심 극한 정리
    * 표본이 충분히 클 때 성립한다.
    * 여러 표본의 표본평균이 이루는 분포가 정규분포에 가까워 진다.
* 정규성 검정
    * 특정 데이터셋이 정규분포를 따르는지 검증하는 과정
    * 정규분포를 따라야 통계적 방법론이나 기법이 유효하게 작동한다.
    * 귀무가설: H0, 데이터셋이 정규분포를 따른다.
    * 대립가설: H1, 데이터셋이 정규분포를 따르지 않는다.
    * 다양한 검정 방법으로 귀무가설의 채택 여부를 결정한다.
    * 대부분 p-value가 0.05 이상이면 정규성을 가정한다.
    * [`ADsP 통계적 추정, 정규성 검정 부분`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/3Data%20Analyst/R) 참고
* 상관관계 분석
    * 연속형 변수 2개 간의 선형적 관계를 분석
    * a변수가 증가할때 b변수도 증가하는지 분석
    * 선형관계의 부호와 크기 파악
    * 얼마나 관계되었는지 상관계수 r로 표현한다.
    * 피어슨 상관계수
* 회귀 모델
    * 독립 변수 X와 종속 변수 Y 간의 관계, 선형 방정식을 모델링
    * 주어진 독립 변수에 대한 종속 변수의 값을 예측
    * metric으로 MSE, RMSE 사용
    * 선형 회귀, 다항 회귀, 릿지 회귀, 라쏘 회귀
    * [`ADsP 회귀 분석 부분`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/3Data%20Analyst/R) 참고
<br><br>



