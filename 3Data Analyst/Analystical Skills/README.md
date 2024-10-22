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
    * df.describe()
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
* [`파이썬 분석의 모델링 부분`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/1Python/2Analysis_zerobase) 참고
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
    * 월 conversion rate: 고객 전환율, (매출/고객수) 비율
* 광고 지표
    * CTR: click through rate, (광고 클릭수)/(광고 노출수) * 100
    * ROAS: return on ad spend, (광고로 인한 수익)/ (광고 비용)
    * Cost for Acquisition: ROAS와 같은 지표
* 웹,앱 지표
    * retention: 남아있는 유저 비율, (특정 기간 이후의 사용자 수)/(처음 서비스를 이용한 사용자 수) * 100
    * DAU: daily active users, 하루 기준 유니크 유저 수
    * click: 몇번 클릭 했는지
    * time spent: 시간을 얼마나 소요했는지
* 마켓팅 지표
    * CAC: customer aquisition cost, (특정 기간동안 총 마케팅 비용)/(동기간 동안 획득한 새 고객 수)
    * NPS: net romoter score, (추천 응답자 비율) - (비추천 응답자 비율)
    * CLTV: customer lifetime value, (고객 당 평균 수익) * (고객 관계 유지 평균 기간)
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
            * conversion rate⭐️: 전환률, 주요 기능을 한 고객의 비율
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
            * 구매전환율: (구매 횟수) / (상세 조회수)
            * LTV: 고객 생애 가치, 한명의 고객에게 기대되는 수익
            * ARPU: avg revenue per user, (매출) / (사용자 수)
            * ARPPU: avg revenue per paid user, (매출) / (구매자 수)
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
* [`파이썬 분석의 시각화 부분`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/1Python/2Analysis_zerobase) 참고
* categorical 데이터 확인
    * sns.catplot 하면 몇개의 카테고리인지 체크하고 분포 체크할 수 있다.
    * 카테고리컬은 다 catplot 해보는게 좋다.
    * for문으로 돌리기
    * for col in categorical_columns:
    *     sns.catplot(x=col, y="Sales", kind="bar", palette="pastel", edgecolor=".6",data=df)
    *     plt.gcf().set_size_inches(25, 3)
    *     plt.xticks(fontsize=16)
    *     plt.legend()
    *     plt.show()
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
* 테이블 그라데이션 표시
    * 플랏 말고 테이블 상태에서 overview 가능
    * df.style.background_gradient(cmap='Blues', subset=['col1'])
* GPS 데이터 시각화
    * 스캐터 플랏 사용하기
    * plt.scatter(df['Lon'], df['Lat'], s=1, alpha=0.5)
<br><br>

### [파이썬 사이킷런]
* 중요 변수 파악
    * 사이킷런 객체 model.feature_importances_ 확인
* 노멀라이즈
    * rfm['R'] = minmax_scale(rfm['R'], axis=0, copy=True)
<br><br>

### [데이터 변환]
* 커스텀 함수 사용해서 변환
    * 커스텀 함수 선언 후 사용
    * df['Date'].apply(remove_p)
    * 짧은 경우 람다 사용
    * df['Date'].apply(lambda x: x.replace(' p)', '')
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



## `[통계 요약 정리]`
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
