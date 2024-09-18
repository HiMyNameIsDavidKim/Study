# Analystical Skills(분석법)

## `[데이터 분석]`

### [데이터 전처리 4단계]
* 데이터 형태 확인
* 데이터 타입 확인
* NULL 값 확인
* outlier 확인
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
    * fit
    * predict와 score 평가
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

### [개념 용어]
* 시나리오가 주어지면 4가지 작성 (문제정의, 기대효과, 해결방안, 성과측정)
* 데이터 EDA
    * Exploratory Data Analysis, 탐색적 데이터 분석
    * 데이터를 이해하고 분석하기 위해 사용하는 초기 과정
    * 데이터의 패턴, 특성, 이상치(Outlier), 숨겨진 관계 등을 확인
* Data mart
    * feature 데이터를 모아둔 데이터베이스
<br><br>



## `[유용한 코드]`

### [파이썬 판다스]
* 데이터프레임 기본 체크
    * df.head()
    * df.shape
    * df.info()
    * df.isnull().sum()
    * df.describe()
* numerical 데이터 확인
    * pd.DataFrame(df.describe())에서 마이너스 있는지 특히 잘 체크한다.
* 상관계수 뽑기
    * df.corr()
    * -1~1 범위
    * 절대값 1에 가까울 수록 상관관계가 높은 것을 의미
<br><br>

### [파이썬 씨본]
* categorical 데이터 확인
    * sns.catplot 하면 몇개의 카테고리인지 체크하고 분포 체크할 수 있다.
    * 카테고리컬은 다 catplot 해보는게 좋다.
    * for문으로 돌리기
* 스캐터 플랏
    * sns.scatterplot(x='Temp', y='Sales', data=df)
    * plt.gcf().set_size_inches(7, 7)
<br><br>

### [파이썬 사이킷런]
* 중요 변수 파악
    * 사이킷런 객체 model.feature_importances_ 확인
<br><br>

### [파이썬 기본 함수]
* 타입 확인
    * df.info()
    * 숫자로 보이는데 문자인 경우 체크
    * 문자로 보이는데 숫자인 경우 체크
    * 인트 플롯 체크
    * dtype 결과가 dtype('O')이면 'Object'라는 뜻으로 문자열이다.
<br><br>

### [데이터 변환]
* 화씨 섭씨 변환
    * df['Temp']= (df['Temp']-32) / 1.8
* 날짜 타입으로 변환
    * df['Date'] = pd.to_datetime(df['Date'])
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

### [Coustomer Lifetime value 분석]
* 
<br><br>

### [LTV 분석]
* 
<br><br>

### [AARRR 분석]
* 
<br><br>
