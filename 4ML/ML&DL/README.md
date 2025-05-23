# ML & DL
* 혼공머신 + 제로베이스 강의
* Machine Learning, 경험을 통해 자동으로 개선하는 컴퓨터 알고리즘.
* Deep Learning, ML + ANN.
* 빅데이터로 x와 y를 준비하고, y = ax + b의 a,b를 구하는 작업.
* x: 확률변수, y: 타깃, a: 웨이트, b: 바이어스
<br><br>



### [라이브러리별 추가 메모]
* [`TensorFlow`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/4ML/ML&DL/TF)
* [`PyTorch`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/4ML/ML&DL/PT)
<br><br>



## `[데이터 전처리]`
* ML, DL 시 데이터를 사전 가공하는 메서드 정리.
* 맷플릿롭은 feature 간 스케일 차이를 이해하지 못한다.
* 시그마와 평균에 맞게 표준점수화(z-score) 시켜주는게 좋다.
    * (자동)
    * 사이킷런의 StandardScaler() 클래스.
    * ss.fit()
    * ss.transform()
    * (수동)
    * mean = np.mean(train_input, axis=0)
    * std = np.std(train_input, axis=0)
    * test_scaled = (test_input - mean) / std
* 트레이닝셋과 테스트셋을 나누어 평가한다. (8:2)
    * train_test_split() 메서드.
* 트레이닝셋에서 검증셋을 분리해 중간 평가를 반영한다. (6:2:2)
    * train_test_split() 메서드 한번 더 사용.
<br><br>



## `[ML]`
* 경험을 통해 자동으로 개선하는 컴퓨터 알고리즘.
    * 알고리즘을 사용하여 데이터에서 패턴을 찾는다.
    * 간단하게 정의하면 머신 랭귀지로 러닝시키는 것.
* 인풋(데이터셋)을 주고, 익명의 함수(람다)를 사용하며, 아웃풋(정답지)를 알려준다.
* 기본 : 회귀(Regression), 분류(Classification)
    * 회귀(regression) : 임의의 숫자를 예측. 연속성 결과, 시퀀셜 결과. (ex. 고객 별 연체 확률 예측, 상품 판매량 예측)
    * 분류(classification) : 클래스 중 하나로 분류. 이산성 결과, 카테고리컬 결과. (ex. 이중분류_라쿤인가?, 다중분류_어떤동물?)
* 응용 : 트리(Tree), 비지도(Unsupervised)
* 분야 : 1.CV(이미지 분류, 스캔, 게임), 2.NLP(분류, 요약, 이해, 수익예측, 음성인식, 구매이력)
<br><br>

### [기본 개념]
* 라이브러리로 사이킷런을 사용.
* 람다 함수 : 익명 함수, 고차함수, 클로저, 콜백과 같은 개념.
* 클로저 : 환경을 담아놓고, 호출 시 꺼내 사용하는 함수.
* 입력 변수(X) : 샘플 = row 1개 = 확률 변수
* 출력 변수(y) : 클래스들 = 답안지 = 타깃 변수 = 기댓값
* 예측값(E) : 들어올 새로운 데이터에 대한 정확도. (y는 학습시킨 데이터에 대한 정확도.)
    * y = aX + b 에서 y가 출력변수, X가 입력변수.
    * 편의상 여기서 a를 계수나 웨이트, b를 절편이나 바이어스라고 부른다.
* Error: variance + bias
    * 추정값에 대한 흩어진 정도 + 추청값과 참값 사이의 거리
    * (ex. 과녁에서 화살들이 모여있다 + 화살들이 중앙에 가깝다)
    * (+noise) 추가로 노이즈의 영향도 받는다.
* 모델링 : 시스템적 특성을 수식화하는 과정.
    * 시스템의 변화 예측이 방정식으로 표현된다. (미분방정식 or 확률함수)
* 지도 학습 : 훈련 데이터로부터 하나의 함수를 유추해내는 학습법.
    * 지도 학습은 입력변수와 출력변수의 값이 주어진 상태에서 러닝하는 것.
    * (ex. Regression, Classification)
* 비지도 학습 : 입력값에 대한 정답 없이 데이터 구성을 알아내는 학습법.
    * 비지도 학습은 입력변수만 있는 상태에서 러닝하는 것.
* 강화 학습 : 현재 상태에서 어떤 행동이 최적인지 보상을 통해 알아내는 학습법.
    * 강화 학습은 입력변수와 보상이 있는 상태에서 러닝하는 것.
* overfitting : train set에서 점수가 좋았으나 test set에서 점수가 아주 나쁜 경우.
* underfitting : train set에서 점수 보다 test set에서 점수가 더 높은 경우.
* appropriate: 언더도 오버도 아닌 적당한 피팅.
* regularization : 규제, train set을 너무 과도하게 overfit하지 않도록 방해하는 작업.
    * 릿지 회귀와 랏쏘 회귀에서 사용된다.
    * alpha로 규제하는 양을 조절 가능하다.
    * alpha의 적절값 : train 과 test의 R^2가 가장 가까운 경우.
* epoch : 트레이닝 셋을 총 사용한 횟수.
* max_iter : epoch와 동일한 용어.
* mini batch : 트레이닝 셋을 조각냈을 때 하나의 조각.
* batch size : 미니 배치가 갖는 데이터의 수.
* 점진적 학습 : 앞서 훈련한 모델을 쓰면서 새로운 데이터를 조금씩 추가로 훈련하는 방법. 경사 하강법으로 구현 가능.
* partial_fit : 에포크 1회 추가 학습.(점진적 학습)
* early stopping : 과대적합 전에 미리 훈련을 멈추는 방법.
<br><br>



## `[회귀 알고리즘]`
* Regression, 연속성 결과를 예측하는 알고리즘.
* MSE를 주로 사용한다.
    * mean squared error
    * 제곱을 하는 이유?
    * 해를 찾을 때 미분하고 변곡점을 찾는다.
    * 제곱을 안한 상수는 미분 불가, 제곱한 경우 미분 가능.
* R^2 : 결정계수, 회귀 알고리즘을 평가할 때 사용. 정확한 숫자를 맞출 수 없기 때문에 사용함.
    * 사이킷런의 score() 메서드.
    * R^2 = 1 - (∑ (타깃 - 예측)^2 / ∑ (타깃 - 평균)^2)
    * 저절로 노멀라이제이션 되는 특징이 있다. (무조건 0~1 사이 값)
    * 이상적으로 64%가 넘어야 유의미 -> 현업에서는 25%만 넘어도 유의미
* 종류 : k-최근접이웃 회귀, 선형 회귀, 다항 회귀, 다중 회귀, 릿지 회귀, 라쏘 회귀
<br><br>
    
### [회귀 알고리즘의 종류]
* feature selection : 상관성이 높은 feature를 하나씩 순차적으로 선택하는 알고리즘.
    * forward selection : 앞에서부터 하나하나 선택.
    * bacward elimination : 뒤에서부터 하나씩 제거.
    * stepwise selection : 앞에서부터 선택하다가 중간에 한두개 빼기.
    * 한계 : 가성비가 안나온다. 매우 오래걸리고 계산도 복잡하다.
* k-최근접이웃 회귀 : 근처 위치에 있는 데이터 k개 값을 기준으로 연속성 결과를 유추하는 알고리즘.
    * 사이킷런 KNeighborsRegressor() 클래스.
    * 한계 : train set의 range를 넘어서는 데이터가 들어오면 유추 불가.
* 선형 회귀 : 특성과 관련된 직선형 방정식(1차 방정식)을 학습하는 알고리즘.
    * 사이킷런 LinearRegression() 클래스.
    * 한계 : 직선 형태로만 설명이 가능하다. (곡선 불가)
* 다항 회귀 : 특성과 관련된 곡선형 방정식(다항 1차 방정식)을 학습하는 알고리즘.
    * 선형 회귀 + np.column_stack 메서드를 활용.
* 다중 회귀 : 여러개의 특성과 관련된 방정식(n차 방정식)을 학습하는 알고리즘.
    * 직선을 넘어 평면이나 큐브 형태의 답을 얻을 수 있다.
    * feature engineering : 기존의 특성으로 새로운 평면을 정의해 활용.
    * 사이킷런 PolynomialFeatures() 클래스로 feature 늘리기.
    * 이걸 그대로 사이킷런 LinearRegression() 클래스에 넣기.
    * 한계 : feature 수 증량을 많이 할수록 overfitting될 수 있음.
* 릿지 회귀 : 다중 회귀에 regularization 기법을 사용한 알고리즘.
    * 사이킷런 Ridge() 클래스.
    * L2 norm, L2 regularization
    * 패널티 텀이 제곱 형태이고 미분할 수 있다.
    * 규제에 의한 계수를 0으로 만들지는 않는다. (랏쏘와 차이)
    * 변수 간 상관관계가 높은 상황에서 좋은 성능.
* 랏쏘 회귀 : 다중 회귀에 regularization 기법을 사용한 알고리즘.
    * 사이킷런 Lasso() 클래스.
    * L1 norm, L1 regularization
    * 패널티 텀이 절대값 형태이고 미분할 수 없다.
    * 규제에 의한 계수를 0으로 만들 수 있다. (릿지와 차이)
    * 변수간 상관관계가 적고 독립적인 상황에서 좋은 성능.
<br><br>



## `[분류 알고리즘]`
* Classifier, 이산성 결과를 예측하는 알고리즘.
* CE를 주로 사용한다.
    * cross entropy, 무질서한 정도를 수치화한 지표.
* 각 클래스별 확률 예측 결과 : predict_proba() 메서드.
* 종류 : k-최근접이웃 분류, 로지스틱 회귀, SGD 분류.
<br><br>

### [분류 알고리즘의 종류]
* k-최근접이웃 분류 : 근처 위치에 있는 데이터 k개 값을 기준으로 다중 분류 결과를 유추하는 알고리즘.
    * 사이킷런 KNeighborsClassifier() 클래스.
* 로지스틱 회귀 : 직선형 방정식(1차 방정식)을 학습하고 로지스틱 함수로 다중 분류 결과를 유추하는 알고리즘.
    * 회귀모델로 각 클래스의 선형 방정식을 구하고 Logistic 함수에 넣는다.
    * 이진분류의 경우 0.5를 기준으로 하고, 다중분류의 경우 소프트맥스를 통과시켜 클래스별 확률 도출.
    * 사이킷런 LogisticRegression() 클래스.
* SGD 분류 : 확률적 경사 하강법을 사용한 분류 알고리즘.
    * 사이킷런 SGDClassifier() 클래스.
    * 앞 모델들과 다르게 점진적 학습이 가능하다.
    * 모델을 새로 만들지 않고 추가로 점진적 학습할 때는 partial_fit() 메서드를 사용.
<br><br>



## `[트리 알고리즘]`
* Tree, 순차적인 조건을 나무처럼 엮은 알고리즘.
* 회귀와 분류가 모두 가능하다.
* 표준화 전처리(StandardScaler)를 할 필요 없다.
* 불순도 : 여러 개의 클래스가 섞여 있는 정도를 표현하는 척도.
    * criterion : 표준, 표준화할 방식을 결정.
    * 지니계수 : 공평하게 섞여 있는지 나타내는 지표.
    * 크로스 엔트로피 : 무질서한 정도를 수치화한 지표.
    * 지니계수는 2차방정식 기반이고 크로스 엔트로피는 로그함수 기반. 곡률이 미세하게 다르지만 퍼포먼스에는 크게 차이가 없다.
    * <img width="425" alt="스크린샷 2022-12-28 오후 12 19 19" src="https://user-images.githubusercontent.com/112922638/209752094-d60957b2-cb91-45e6-bab5-541f328b1f86.png">
* 정보이득 : information gain, 부모와 자식 노드 사이의 불순도 차이.
* 종류 : 결정 트리, 랜덤 포레스트, 엑스트라 트리, 그라디언트 부스팅, 히스토그램 기반 그라디언트 부스팅(=XGBoost =LightGBM).
<br><br>

### [트리 알고리즘의 종류]
* 결정 트리 : 연속적인 질문(조건)을 이어가며 학습하는 알고리즘.
    * 사이킷런의 DecisionTreeClassifier() 클래스.
    * plot_tree() 함수로 시각화 가능.
    * 부모노드와 자식노드의 불순도 차이가 최대가 되도록 성장함.
    * 특성의 중요도 추출 가능. feature_importances_ 속성.
* 랜덤 포레스트 : 결정 트리의 앙상블 학습 알고리즘.
    * 사이킷런의 RandomForestClassifier() 클래스.
    * 앙상블 학습 중에 배깅 방식.
    * 100개의 결정트리를 사용.
    * 랜덤하게 데이터 샘플링하여 n개의 데이터셋 생성.
    * 노드 분할 시 최대의 정보이득인 경우를 선택.
* 엑스트라 트리 : 랜덤 포레스트와 유사한 알고리즘.
    * 사이킷런의 ExtraTreeClassifier() 클래스.
    * 앙상블 학습 중에 배깅의 변형 방식.
    * 전체 데이터셋을 사용.
    * 노드 분할 시 랜덤한 경우를 선택.
* 그라디언트 부스팅 : 깊이가 얕은 이진 결정 트리의 앙상블 학습 알고리즘.
    * 사이킷런의 GradientBoostingClassifier() 클래스.
    * 깊이 3의 결정트리를 사용. -> 일반화에 유리하다.
    * 결정트리를 계속 추가하며 경사하강법을 사용.
* 히스토그램 기반 그라디언트 부스팅 : 히스토그램 기법이 추가로 적용.
    * 트레이닝셋의 각 피쳐 컬럼으로 히스토그램을 그려 256개 구간으로 나누고 피쳐값을 255개의 구간 인덱스로 취급해버린다.
    * 그라디언트 계산이 간단해져 노드를 분할하는 속도가 빨라진다.
    * 머리로는 이해가 안되겠지만... 실제 계산해보면 (부모 - 왼쪽 자식 = 오른쪽 자식)이 성립한다...!
    * 정형 데이터 분석의 최강 알고리즘.
    * 사이킷런의 HistGradientBoostingClassifier() 클래스.
    * 타 라이브러리 XGBoost, LightGBM도 사용 가능.
<br><br>

### [교차검증]
* cross validation, 트레이닝셋에서 검증셋을 분리할 때 k개로 나눈 뒤 k번의 검증을 하는 검증법.
* 트레이닝셋에 과대 적합되어 일반화된 평가에서 약점이 생기는 것을 방지한다.
* cross_validate() 함수.

### [하이퍼파라미터 튜닝]
* 하이퍼파라미터 미세 변화에 따라 정확도가 달라진다. -> 마찬가지로 교차검증 대상
* grid search
    * 모든 파라미터를 조금씩 고치며 완전탐색 알고리즘으로 확인.
    * GridSearchCV() 클래스.
* random search
    * 파라미터 조건이 너무 많을 경우 확률 분포를 활용해 서치.
    * RandomSearchCV() 클래스.
<br><br>

### [앙상블 학습]
* ensemble learning
* 여러개의 클래시파이어를 생성하고 조합하여 더 정확한 예측을 하는 학습법.
* 배깅에서 집계 종류 : merge voting, weighted voting 등등
* 배깅에 트리를 더하면 랜덤포레스트 이다.
* 단순 보팅
    * voting 
    * 각 모델의 결과로 투표를 통해 최종 예측 결과를 결정
    * 가장 단순한 방법
    * 다른 유형의 알고리즘
    * 같은 통합 데이터셋
* 배깅
    * Bootstrap AGGregatING
    * 데이터 샘플링(bootstrap)을 통해 모델을 학습
    * 결과를 집계(Aggregating)
    * 같은 유형의 알고리즘
    * 다른 쪼개진 데이터셋
    * variance를 낮춰준다.
* 스태킹
    * stacking 
    * 데이터셋 샘플링 모델 학습 -> 결과 집계
    * 배깅과 같지만 `서로 다른 알고리즘 여러개` 사용해 학습
    * 다른 유형의 알고리즘
    * 다른 쪼개진 데이터셋
    * variance를 낮춰준다.
* 부스팅
    * Boosting
    * 여러개의 디시전 트리를 순차적으로 학습
    * 이전 알고리즘이 다음 알고리즘에게 가중치를 전달
    * 같은 유형의 알고리즘
    * 같은 통합 데이터셋
    * bias를 낮춰준다.
    * 가장 정확하지만 가장 느리다.
<br><br>

### [랜덤 포레스트 심화]
* 랜덤 디시전 트리 + 배깅 앙상블
* 2가지 방법으로 앙상블의 다양성 증가
    * 데이터 중 일부만 추출
    * 컬럼 중 일부만 사용
    * 배깅된 각 데이터셋의 다양성이 매우 높아진다.
* 트리는 깊이 성장할수록 train set에 오버피팅 된다.
* 만약 train set에 노이즈가 있다면, 트리는 노이즈까지 민감하게 학습한다.
* 트리들 간에 상관성(corr)이 낮다면 노이즈 영향이 줄어든다.
* 배깅을 통해 서로 다른 데이터셋을 만들고 훈련하면 트리들 간에 상관성이 낮다.
* 따라서 노이즈의 영향이 적은 (variance가 작은) 예측이 가능하다.
* OOB
    * out of bag
    * 랜덤 포레스트 추출 시 64%만 선택하고 36.8%는 선택하지 않는다.
    * 이 36.8%를 그대로 val set으로 사용하면 된다.
    * feature importance
        * OOB를 사용해서 feature importance 측정이 가능하다.
        * OOB의 피쳐 하나의 데이터 순서를 무작위로 섞는다.
        * 원래보다 error가 몇 % 떨어지는지 관찰한다.
* 요즘에는 배깅 보다는 부스팅을 더 많이 사용한다.
* 부스팅: AdaBoost, GBM, NGBoost, LightGBM, CatBoost, NoBoost
<br><br>

### [파라미터 최적화]
* Grid Search: 가능한 모든 조합을 탐색.
* Random Search: 레인지 안에서 무작위로 값을 선택하여 탐색.
* Bayesian Optim: 이전 시도 결과를 바탕으로 최적 값을 예측하며 탐색.
* Optuna
    * 여러 알고리즘을 지원하는 프레임워크.
    * 베이지안을 변형한 TPE를 주로 사용한다.
<br><br>



## `[비지도 학습]`
* Unsupervised learning, 타깃이 없을 때 사용하는 알고리즘.
* clustering : 군집, 비슷한 샘플끼리 그룹으로 모으는 작업.
* cluster : 모여진 그룹 중의 하나.
* centroid : 클러스터 중심, k-means에 의해 계산된 평균값.
* 최적의 클러스터 개수(k) 찾기
    * inertia : 센트로이드와 각 샘플 사이 거리의 제곱 합.
    * elbow : 클러스터 개수를 늘려가며 이너셔 변화율이 급격히 떨어지는 지점 선정. 
    * shihoutte : 군집 내 데이터들이 다른 군집과 비교해 얼마나 거리가 가까운지 계산하여 수치적으로 선정. 1에 가까울 수록 좋으며 일반적으로 0.5도 넘기 힘들다.
* 차원 : 차원축소에서 차원은 1차원 배열에서 각 feature들을 말한다.
    * (ex. (1,5) 배열 = 1차원 배열 = 5차원 벡터)
* 차원축소 : 데이터를 잘 나타내는 feature를 선택하여 모델 성능 향상.
* 종류 : 군집(K-means, K-medians, Mean-Shift, DBSCAN), 차원축소(PCA), 이상 탐지
<br><br>

### [비지도 학습의 종류]
* K-means : 랜덤으로 클러스터 중심을 정하고 '클러스터에 속한 샘플의 평균값'으로 중심을 변경하며 최적 군집을 찾는 알고리즘.
    * 사이킷런의 KMeans() 클래스.
    * 군집 개수 k를 지정해야 한다. (n_clusters='')
    * inertia_ 속성값을 보고 k 결정. (elbow method)
    * cluster_centers_ 속성값으로 센트로이드를 불러낼 수 있다.
    * transform() 메서드로 각 센트로이드까지의 거리 측정 가능.
* Mean-Shift : 랜덤으로 클러스터 중심을 정하고 '샘플의 밀도가 가장 높은 곳'으로 중심을 이동하며 최적 군집을 찾는 알고리즘.
    * 사이킷런의 MeanShift() 클래스.
    * 군집 갯수를 지정할 필요 없다. 대신 대역폭의 영향이 크다. (bandwidth='')
    * estimate_bandwidth() 메서드로 최적 대역폭 탐색.
* DBSCAN : 최근접이웃과 유사한 방식으로 코어 샘플을 기준으로 반경 e 이내에 m개 이상의 샘플이 있을 경우 이들을 한 군집으로 취급하는 알고리즘.
    * 사이킷런의 DBSCAN() 클래스.
    * 반경 e와 최소 이웃점 개수 m을 설정.
* PCA : 주성분 분석, 데이터의 분산이 큰 방향을 주성분 벡터라고 정의하고, 주성분 직선 위로 프로젝션하는 방식으로 차원을 축소하는 알고리즘.
    * 사이킷런의 PCA() 클래스.
    * 차원이 기존성분 x개에서 주성분 n개로 줄어든다.
    * 주성분의 개수를 지정할 수 있으며, 각 주성분이 내포하는 '설명된 분산'을 출력해볼 수 있다.
    * 주로 다른 머신러닝 알고리즘과 섞어서 사용한다. (feature 개수만 줄이고 타 알고리즘으로 fit())
* SVM
    * Support Vector Machine
    * 두 클래스 간의 경계를 찾는 알고리즘.
    * hyperplane: 두 클래스를 나누는 초평면
    * margin: 두 클래스 사이의 여유공간
    * 마진을 최대화하는 초평면을 찾는 것이 objective 이다.
    * 비선형일 경우
        * soft magin SVM: 오차를 허용하는 슬랙 변수를 추가
        * kernel trick: 고차원 공간으로 매핑 후 SVM
* OCSVM
    * One Class SVM
    * 정상 데이터만 사용해 비지도학습을 하는 이상탐지 알고리즘.
    * 모두 포함하는 최소 부피 초평면을 찾는 것이 objective 이다.
* SVDD
    * Support Vector Data Description
    * 대부분의 데이터를 포함하는 최소 크기의 구를 찾는 알고리즘.
    * 구의 경계 밖은 모두 이상치로 판단한다.
    * 구의 중심과 구의 반경을 찾는 것이 objective 이다.
<br><br>



## `[DL]`
* 머신러닝(ML)의 한 종류로, 신경망(NN, Neural Network)을 수많은 계층 형태로 연결한 기법.
* 종류 : DNN(Deep), CNN(Convolution), RNN(Recurrent), LSTM, GRU
* 응용 : Transfer, Auto Encoder, GAN
<br><br>

### [기본 개념]
* 라이브러리로 텐서플로우, 파이토치를 사용.
    * 텐서플로우 : 구글의 DL 라이브러리.
    * 케라스를 인수합병 했다.
    * TensorFlow.js와 TensorFlow Lite가 있어서 모바일에도 적용 가능.
    * 파이토치 : 페이스북의 DL 라이브러리.
    * 더 파이써닉한 접근방식으로 람다를 적극 활용한다.
* 인공신경망 : ANN, Artificial Neural Network.
* compile 메서드 : (loss = 모델의 손실함수, metrics = 훈련 과정에서 계산할 측정값) 지정.
* fit 메서드 : (입력 데이터셋, 타깃, 학습 반복 횟수) 지정.
<br><br>

### [딥러닝 레이어]
* 활성화 함수 : activation function, 입력된 데이터의 가중 합을 출력 신호로 변환하는 함수.
    * ReLU : 입력값이 0보다 작으면 0, 크면 y=x로 출력. 은닉층에 사용.
    * Leaky ReLU : 0보다 작은 노드를 완전히 죽이는 오류를 개선. 은닉층에 사용.
    * Sigmoid : 0~1 범위의 기울어진 S자 형태의 곡선 함수. 이진분류 출력층에 사용. 
        * (실제 시그모이드 함수란 S자 형태를 말하는 것이고, 0~1 사이 값을 가지는 시그모이드 함수는 로지스틱 함수이다. 하지만 관용적으로 동의어로 취급)
    * Softmax : 0~1 범위의 익스포넨셜 형태의 함수. 정규화 되어 출력의 총합이 1인 특징. 다중분류 출력층에 사용.
* 손실 함수 : loss function, 1개 샘플에 대하여 예측값과 실제 정답의 차이를 비교하는 함수.
    * BCE : 바이너리 크로스 엔트로피, 이진분류에 사용.
    * CCE : 카테고리컬 크로스 엔트로피, 다중분류에 사용.
    * MSE : 평균 제곱 오차, 회귀에 사용.
    * 비용 함수 : cost function, 모든 샘플에 대하여 예측값과 실제 정답의 차이를 비교하는 함수. 각 샘플에 대한 로스의 총합 = 코스트.
* 옵티마이저 : 최소의 loss로 학습하는 방법을 찾는 최적화 알고리즘.
    * 손실함수가 가장 적은 지점이 최적값 즉 해이다. n차 함수 형태인 손실함수의 최솟값을 구하는 방법은 미분해서 0인 지점으로 다가가는 것.(미분 = 경사, 다가가는 것 = 하강법.)
    * SGD : 확률적 경사 하강법, 기존 샘플 1개와 새로운 데이터로 최대 그라디언트 계산하여 최대 속도로 학습.
    * RMSprop : 루트 민 스퀘어 예측법, 기울기에 따라 학습률을 조절해서 정확도 높임.
    * 모멘텀 : 경사 하강법에 관성 개념을 추가. 지역 최솟값에 갇히지 않도록 설계됨.
    * 아담 : RMSProp과 모멘텀의 하이브리드.
<br><br>



## `[DNN]`
* Deep Neural Network.
* 특징
    * 입력층 전체에 가중치 적용.
    * (f(x)= w1x1 + w2x2 + ... + b)
    * 구조 : 입력층 - (밀집층) * N - 출력층
* 입력층 : input layer, 입력되는 값 각 하나하나. (ex. 1920x1080개 픽셀)
* 출력층 : output layer, 출력되는 결과. (ex. 옷의 카테고리)
* 밀집층 : dense layer, 입력층에 가중치를 곱하는 층.
    * keras.layers.Dense(뉴런수, 활성함수, (입력크기))
    * 첫번째 층은 반드시 입력크기가 있어야 한다.
    * 지저분하다고 생각하면 Flatten() 클래스를 통해 2차원을 1차원으로 미리 변환.
* 은닉층 : hidden layer, 입력층과 출력층 사이의 모든 층.
    * 은닉층 마다 활성화 함수가 있다. (각 층의 비선형성 부여)
<br><br>



## `[CNN]`
* Convolution Neural Network.
* 특징
    * 이미지 데이터 처리 전용 신경망.
    * 입력층의 일부에 가중치 적용.
    * (f(x) * g(t))
    * 이미지를 변형없이 2차원 그대로 사용한다.
    * 반드시 깊이 차원이 있어야 한다. (RGB=3, Gray=1)
    * 구조 : 입력층 - (합성곱층 - 풀링층) * N - 출력층
* 개념
    * 필터 : 합성곱할 NxN크기 행렬의 갯수. 가중치의 집합. CNN의 뉴런.
    * 파라미터 : 필터 속에 가중치 1개. (ex. 3x3 = 9개 파라미터)
    * 커널 : 파라미터와 동의어.
    * 윈도우 : 필터의 생김새. (n, n) 인지를 나타냄.
    * 특성맵 : 원래 행렬을 필터와 합성곱 계산한 결과물.
    * 패딩 : 합성곱 계산을 위해 외곽 테두리에 0인 패딩을 채운다.
    * 스트라이드 : 커널의 이동 크기.
    * 풀링 : 특성맵의 가로세로 크기를 줄이는 역할. 최대 혹은 평균 사용.
    * FLOPs : 모델이 계산해야하는 양. 적으면 효율적이고 가벼운 모델.
* 합성곱층 : Convolution layer, 입력층에 합성곱을 진행하는 층.
    * keras.layers.Conv2D(필터수, 커널사이즈, 활성함수)
    * 정보에 편향이 생기지 않도록 padding='same'을 추가해주는 것을 추천.
* 풀링층 : Pooling layer, 특성맵의 가로세로 크기를 줄이는 층.
    * keras.layers.MaxPooling2D(풀링크기)
<br><br>



## `[RNN]`
* Recurrent Neural Network.
* 특징
    * 시계열 데이터 처리 전용 신경망. (텍스트, 주가예측 등)
    * 앞서 사용한 데이터를 버리지 않고 기억한다.
    * 구조 : 입력층 - (순환층) * N - 출력층
* 개념
    * 타임스텝 : 샘플을 처리하는 단계의 단위.
    * 셀 : RNN에서 층.
    * 은닉 상태 : RNN에서 셀의 출력.
    * tanh : 보편적인 셀의 활성화 함수.
    * 말뭉치 : corpus, NLP에서 트레이닝셋.
    * 토큰 : NLP에서 각각 분리된 단어 하나.
* 순환층 : Recurrent Layer, 순환 계산을 진행하는 층.
    * 같은 셀은 타임스텝이 지나더라도 같은 웨이트를 사용한다.
    * 각 타임스텝의 결과는 다음 타임스텝의 입력이다.
    * 한 뉴런의 계산 결과를 모든 뉴런이 받는다.
    * 즉 타임스텝 마다 각 뉴런들은 모든 뉴런들의 결과를 받는다.
* 원핫 인코딩 : 클래스들 중에 원하는 것만 1이고 나머지는 0인 벡터로 변환.
    * 토큰 수만큼 계산이 복잡해진다.
    * 0과 1로만 구성되므로 단어간 상호 연관성을 표현할 수 없다.
* 단어 임베딩 : 비교적 작은 크기의 실수 벡터로 변환.
    * 단어간 상호 연관성을 표현할 수 있다.
    * 성능이 뛰어남.
<br><br>



## `[LSTM]`
* Long Short Term Memory.
* 특징 
    * 시퀀스가 길어도 은닉상태의 정보가 희석되지 않고 균일하게 반영된다.
    * 기본 RNN의 은닉 상태는 숏 텀에 대하여 기억한다.
    * 셀 상태라는 개념을 도입해 롱 텀에 대하여 기억한다.
    * 3개의 게이트를 가진다.
    * 구조 : 입력층 - (LSTM층) * N - 출력층
* 개념
    * 셀 상태 : 은닉 상태처럼 다음 층에 전달되는 것이 아니라, 내부적으로 순환만 되는 출력.
    * 삭제 게이트 : 시그모이드 함수로 기억을 삭제.
    * 입력 게이트 : 은닉 상태와 셀 상태를 다음 셀 상태에 얼마나 반영할지 결정.
    * 출력 게이트 : 은닉 상태 출력.
    * 셀 상태 = 장기기억, 은닉 상태 = 단기기억
    * 셀 상태 업데이트 : (직전 셀 상태 * 삭제 게이트의 결과) + (입력 게이트의 결과)
    * 은닉 상태 업데이트 : (이번 셀 상태의 활성화(tanh)) * (출력 게이트의 결과)
<br><br>



## `[GRU 셀]`
* Gated Recurrent Unit.
* 특징
    * 시퀀스가 길어도 은닉상태의 정보가 희석되지 않고 균일하게 반영된다.
    * LSTM을 간소화한 버전. 2개의 게이트를 가지고 셀 상태가 없다.
    * 구조 : 입력층 - (GRU층) * N - 출력층
* 개념
    * 업데이트 게이트 : 이번에 들어온 입력과 직전의 은닉 상태를 얼마씩 반영할지 결정.
    * 리셋 게이트 : 직전의 은닉 상태의 정보를 얼마나 버려서 반영할지 결정.
    * 두 게이트 모두 다음 은닉 상태를 만들기 위해 동작한다.
<br><br>



## `[Transfer]`
* 전이학습. 특정 조건에서 얻어진 지식을 다른 상황에 맞게 전이해서 활용.
* 학습 데이터가 부족한 분야의 모델 구축을 위해 데이터가 풍부한 분야의 훈련된 모델을 재사용.
* 특징
    * 데이터가 부족해도 감안할 수 있다.
    * 학습에 걸리는 시간이 짧다.
    * 시뮬레이션에서 학습된 모델을 현실에 적용할 수 있다.
* 개념
    * Feature extractor : 이미지넷 같은 대용량 데이터셋으로 미리 학습된 부분. 미리 학습된 특성 추출법을 사용.
    * 이미 완성된 모델의 마지막 FC만 떼어놓고 가져와서 모델에 사용한다.
    * 스타일 : 다른 필터 리스폰스 간의 연관성. 대상에 적용할 스타일.
    * 콘텐츠 : 더 높은 레이어 내의 피쳐 리스폰스. 스타일을 적용할 대상.
    * 그람 행렬 : 스타일과 콘텐츠를 담는 자료구조. 픽셀을 일렬로 펼친 뒤, 자승 전치 행렬과 내적.
    * 총 손실 = 스타일 손실 * w1 + 콘텐츠 손실 * w2
<br><br>



## `[Auto Encoder]`
* 데이터에 대한 효율적인 압축을 신경망을 통해 자동으로 학습하는 모델.
* 디퓨전 모델의 어텐션에서 사용된다.
* 디노이징, 시맨틱 세그멘테이션 등에 활용.
* 특징
    * 입력 데이터가 곧 라벨이므로 비지도학습. 그 중에서 차원축소.
    * 입력 -> (인코더) -> (z) -> (디코더) -> 출력
* 개념
    * 인코더 : 입력을 압축시켜 더 낮은 차원인 잠재변수로 만든다.
    * 디코더 : 잠재변수를 복원해 입력으로 만든다.
    * 잠재변수 = 코드 = z
    * 위성사진을 지도앱 이미지로 만드는 것을 생각해보자. 입력에서 차원축소를 진행해 건물, 도로, 산, 크기, 경계 등으로 만들고 이를 다시 복원할 때 표현법을 알려주는 것.
<br><br>



## `[GAN]`
* Generative Adversarial Network, 생성적 적대 신경망.
* 대립하는 두 시스템의 경쟁을 통해 학습하는 방법론.
* 특징
    * 생성 네트워크와 구분 네트워크 간의 상반되는 목적함수를 갖는다.
    * 생성자 학습, 구분자 학습 둘 다 구현해야 한다.
    * 모드 붕괴 : 생성자가 구분자를 속일 수 있는 특정 데이터만 반복해서 만들어내는 현상.
    * 오실레이션 : 클래스가 여러개일 때, 생성자가 생성하는 클래스를 계속 바꾸는 특성.
* 개념
    * 생성자 : generator, 입력을 받아 가짜 데이터를 생성한다.
    * 구분자 : discriminator, 실제 데이터와 가짜 데이터를 받아 뭐가 실제인지 판단한다.
    * 생성자는 랜덤 노이즈를 받아 실제 데이터와 같은 형태의 데이터를 생성한다.
    * 구분자는 실제 데이터는 1, 가짜 데이터는 0에 가깝게 나오도록 학습한다.
* DCGAN : 합성곱 신경망이 적용된 GAN.
    * maxpooling과 같이 미분이 안되는 부분을 conv로 대체.
    * FC Layer 제거.
    * Batch Normalization 사용.
    * Conv층은 ReLU 사용. 출력층은 Tanh 사용.
    * 구분자는 Leaky ReLU 사용.
* 응용 사례
    * SRGAN : Super Resolution GAN.
        * Generator가 저해상도 이미지를 이용해 가짜 고해상도 이미지 생성.
        * Discriminator가 (가짜 고해상도 이미지 vs 답안 고해상도 이미지) 누가 답안인지 판단.
    * Text to image synthesis : 특정 문장을 벡터화한 뒤, GAN을 활용해 이미지 합성.
    * Pix2Pix : 이미지를 보여주고 GAN을 활용해 새로운 이미지 합성.
<br><br>




## `[함수 사용 순서 정리]`

### [Scikit-learn 함수 사용 순서_지도학습]
* 1.Classifier() or Regressor()
* 2.cross_validate()
* 3.fit()
* 4.scores()
* 5.save()
<br><br>

### [Scikit-learn 함수 사용 순서_비지도학습]
* 1.비지도학습 클래스()
* 2.fit()
* 3.predict()
* 4.save()
<br><br>

### [TensorFlow 함수 사용 순서]
* 1.model = keras.Sequential()
* 2.model.add(keras.layers.XXX())
* 3.compile()
* 4.fit()
* 5.evaluate()
* 6.save()

### [PyTorch 함수 사용 순서]
* 1.class DNNModel(nn.Module)
* 2.def forward
* 3.loss_func = , optimizer = 
* 4.2중 for문
* 5.model.eval() + for문
* 6.save()