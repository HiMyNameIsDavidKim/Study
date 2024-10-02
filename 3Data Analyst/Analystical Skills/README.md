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
* 데이터 EDA
* 모델링 or 인사이트
<br><br>

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
    * df.discribe()
    * 특히 min, max에 음수값 있는지 확인
    * 도메인 지식 기반으로 처리
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
* 
* 프로세스
    * X(feature 데이터)와 Y(정답 데이터) 만들기
    * 트레이닝셋 트레인셋 분할
    * 모델 인스턴스, 하이퍼 파라미터 설정
    * 학습, 예측
    * 성능 평가
    * (필요 시) 하이퍼 파라미터 자동 튜닝
    * 중요 변수 파악
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

### [프로젝트 유형]
* 데이터 EDA 및 인사이트 (대부분)
* 분류, 회귀 모델
* 그외 분석 모델
    * segmentation
        * 특정한 특성을 가진 카테고리를 그루핑하여 분석
        * RFM 분석으로 segmentation할 수 있다.
    * 이상 탐지
        * 정의한 이상 데이터 패턴들 분석
        * 룰베이스로 로직 만들기
        * 모델링도 좋지만 도메인 지식으로 로직 만드는게 좋을 때가 많다.
<br><br>

### [개념 용어]
* 시나리오가 주어지면 4가지 작성 (문제정의, 기대효과, 해결방안, 성과측정)
* 데이터 EDA
    * Exploratory Data Analysis, 탐색적 데이터 분석
    * 데이터를 이해하고 분석하기 위해 사용하는 초기 과정
    * 데이터의 패턴, 특성, 이상치(Outlier), 숨겨진 관계 등을 확인
* Data mart
    * feature 데이터를 모아둔 데이터베이스
* KPIs
    * Key Performance Indicators
    * 목표, 지표, 고과
<br><br>

### [도메인 지식 메모]
* 콘텐츠에서 KPIs
    * MAU: monthly active users, 한달동안 앱에서 활동하는 순 유저 수
    * 월 트랜젝션 AMT: 트랜젝션으로 발생한 매출(amount) 양
    * 월 conversion rate: 고객 전환율, (매출/고객수) 비율
<br><br>




## `[유용한 코드]`

### [파이썬 판다스]
* 데이터프레임 기본 체크
    * 불러오고 헤드 출력 해보기
        * df.head()
    * 전처리 4단계
        * df.shape
        * df.info()
        * df.isnull().sum()
        * df.describe()
* 타입 확인
    * df.info()
    * dtype 결과가 dtype('O')이면 'Object'라는 뜻으로 문자열이다.
* numerical 데이터 확인
    * df.describe()에서 마이너스 있는지 특히 잘 체크한다.
* 상관계수 뽑기
    * df.corr()
    * -1~1 범위
    * 절대값 1에 가까울 수록 상관관계가 높은 것을 의미
* 고유값 세기
    * df['col'].nunique()
* 제이슨 파일 불러오는 코드
    * 따로 함수 선언 필요
    * 처리할 컬럼 알고 있어야 함
<br><br>

### [파이썬 씨본]
* [파이썬 분석의 시각화 부분](https://github.com/HiMyNameIsDavidKim/Study/tree/main/1Python/2Analysis_zerobase) 참고
* categorical 데이터 확인
    * sns.catplot 하면 몇개의 카테고리인지 체크하고 분포 체크할 수 있다.
    * 카테고리컬은 다 catplot 해보는게 좋다.
    * for문으로 돌리기
* 스캐터 플랏
    * 산점도 분포 확인
    * sns.scatterplot(x='Temp', y='Sales', data=df)
    * plt.gcf().set_size_inches(7, 7)
* 박스 플랏
    * 카테고리별 분포 확인, 기초통계값 확인
    * sns.boxplot(x='killsCategories', y='winPlacePerc', data=kills)
* 피벗 플랏
    * 년도별 카테고리별 점유율 변화에 유용
    * ax = df.plot(kind='barh', stacked=True, title="years amt", rot=0)
    * for p in ax.patches:
    *   left, bottom, width, height = p.get_bbox().bounds
    *   ax.annotate("%.1f"%(width*100), xy=(left+width/2, bottom+height/2), ha='center', va='center', color='black')
<br><br>

### [파이썬 사이킷런]
* 중요 변수 파악
    * 사이킷런 객체 model.feature_importances_ 확인
* 노멀라이즈
    * rfm['R'] = minmax_scale(rfm['R'], axis=0, copy=True)
<br><br>

### [데이터 변환]
* 화씨 섭씨 변환
    * df['Temp']= (df['Temp']-32) / 1.8
* 날짜 변환
    * 스트링에서 데이트 타입으로 변환
        * df['Date'] = pd.to_datetime(df['Date'])
    * 날짜 + 시간 합쳐서 데이트 타입으로 변환
        * df_core_store['Date_merge'] = df['date'].astype(str) + ' ' + df['time'].astype(str)
        * df_core_store['Date_merge'] = pd.to_datetime(df_core_store['Date_merge'])
    * 년 월 분할
        * df_core_store['year'] = df_core_store['Date_merge'].dt.year
        * df_core_store['month'] = df_core_store['Date_merge'].dt.month
    * 월데이터 보기 힘들때 변환
        * df = df.replace({'January' : '01.January',
            'February' : '02.February',
            'March' : '03.March',
            'April' : '04.April',
            'May' : '05.May',
            'June' : '06.June',
            'July' : '07.July',
            'August' : '08.August',
            'September' : '09.September',
            'October' : '10.October',
            'November' : '11.November',
            'December' : '12.December'})
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

### [RFM 분석]
* 고객을 점수화 해서 서비스 등급 구간(grade) 부여
* R: recency, 최근성, 얼마나 최근에 구매
* F: frequency, 빈도, 얼마나 자주 구매
* M: monetary, 금액, 구매 금액
* 그루핑을 통해 서비스 이용 수준 측정 가능
* 고객마다 RFM이 어떻게 변하는지 관찰
* R은 낮을수록 좋기 때문에 노멀라이즈 시 (1-R) 해주기
<br><br>
