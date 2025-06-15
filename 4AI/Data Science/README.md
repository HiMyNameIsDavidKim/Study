# Data Science

## `[examples]`
* [`Spaceship Titanic`]()
* [`T-검정, 상관분석`](https://github.com/HiMyNameIsDavidKim/DS_Example/blob/main/Data_Science/stat_exam.py)
* [`워드 클라우드(댓글)`](https://github.com/HiMyNameIsDavidKim/DS_Example/blob/main/Data_Science/comment_bts.py)
* [`워드 클라우드(연설문)`](https://github.com/HiMyNameIsDavidKim/DS_Example/blob/main/Data_Science/speech_moon.py)
* [`한국복지패널 공공데이터 분석`](https://github.com/HiMyNameIsDavidKim/DS_Example/blob/main/Data_Science/welfare.py)
<br><br>



## `[Data Science]`
* 다양한 종류의 데이터로부터 지식과 인사이트를 추출하는 융합분야.
* 과학적 방법론, 프로세스, 알고리즘, 시스템 등을 동원한다.
* 통계학, 데이터분석, 머신러닝, 패턴인식을 통합하는 개념으로 정의한다.
<br><br>

### [라이브러리]
* 넘파이 : array. 가공.
    * shape : (샘플 수, 특성 수) 보기
    * column_stack : 계산된 컬럼 추가
* 판다스 : DataFrame. 데이터 분석 및 가공.
    * 조회
        * pd.read_excel() : 엑셀 리딩, 시트 지정 필수, 행렬 지정 리딩 가능.
        * columns, head(), tail(), shape, info(), describe() : 정보 보기.
        * value_counts() : 각 컬럼에 몇개의 데이터가 있는지 확인.
        * loc[[행], [열]] : 행 or 열 or 요소 조회.
        * len(df.loc[df['name']==0]) : 원하는 값 개수 조회.
        * pd.isna() : null값 확인.
    * 연산
        * mean(), sum(), max(), min() : 집계함수
        * assign() : 계산된 컬럼 추가.
        * merge() : 가로 합치기.
        * concat() : 세로 합치기.
    * 수정
        * rename() : 컬럼명 바꾸기
        * np.where() : 조건에 맞는 데이터 수정.
        * query() : 조건에 맞는 데이터만 추출 가능(df 출력), 괄호에 조건문.
        * drop() : 특정 컬럼 제거.
        * pd.dropna() : 결측치 행 제거.
        * sort_values() : 특정 컬럼 정렬.
        * groupby() : 특정 컬럼 1개로 피벗테이블 작성 가능.
        * nlargest() : top n개 뽑아내기
* 씨본 : 그래프.
    * 생성자 매개변수
        * data = csv_name, x = 'x', y = 'y'
        * hue = '컬럼명' : 종류별로 색깔 설정.
        * ci = None : 신뢰구간 표시 제거.
    * 산점도
        * sns.scatterplot()
        * .set(xlim = (0,0), ylim = (0,0)) : 축 범위 설정.
    * 막대 그래프
        * sns.barplot()
        * .sort_values() : 크기순 정렬.
    * 선 그래프
        * sns.lineplot()
    * 박스 플랏
        * sns.boxplot()
    * 히스토그램
        * sns.histplot()
* 피클 : 자료형의 변환 없이 그대로 피클파일로 저장하는 라이브러리.
    * csv나 excel로 구동하는 것보다 속도가 매우 빠르다.
* pyplot : 시각화 및 그래프 생성에 주로 사용되는 라이브러리.
<br><br>

### [Data Base]
* 여러 사람이 공유하여 사용하는 데이터의 집합.
* 확장순서 : 데이터 -> 데이터 구조 -> 데이터 클래스 -> 데이터 프레임 -> 데이터 베이스 -> 데이터 웨어하우스 -> 데이터 센터
* 분야별 종사자 마다 부르는 명칭이 다르다. 눈치껏 알아듣자.
    * 컬럼 = 열 = 필드 = 속성 = 프로퍼티(속성값) = 변수 = 피쳐 = 팩터 = 인스턴스 변수 = 멤버 변수
    * 로우 = 행 = 튜플 = 레코드 = 케이스
* 스키마(=테이블 헤드) : 테이블을 디자인하기 위한 구조.(컬럼명의 집합)
* 인스턴스(=테이블 바디) : 테이블에 들어있는 데이터들. (행의 집합)
<br><br>

### [데이터의 종류]
* 메타 데이터 : 데이터에 관한 구조화된 데이터. 다른 데이터를 설명해주는 데이터.(=스키마)
* 정형 데이터 : 파일에 있는 데이터. 구조화 되어 있어서 바로 사용 가능.
* 비정형 데이터 : 파일이 아닌 데이터. 구조화 되어 있지 않아 바로 사용할 수 없음.
* 시계열 데이터 : 시간이 포함된 매트릭스 데이터.
<br><br>

### [ETL]
* Extraction Transform Load, 일반적인 데이터파이프라인 flow.
* 하나의 시스템에서 data를 추출 변환하여 DB에 적재하는 역할을 함.
<br><br>

### [프로젝트의 플로우차트]
* 1.문제제기
* 2.데이터 구하기
* 3.타깃 변수 설정
* 4.데이터 처리
    * ID 변수 확인
    * 타깃 변수 생성
* 5.EDA 및 시각화
    * 결측값 제거
    * 요약 통계 확인
    * 이상치 제거
    * 상관관계 확인
    * 시각화
* 6.머신러닝 모델 수립
* 7.머신러닝 모델 실행
* 8.데이터 후처리
    * 데이터 분할
    * 데이터 변환
    * 데이터 구간화
    * 모델 재실행
* 9.최적 모델 선정 및 활용
<br><br>



## `[데이터 처리]`

### [플로우 책(임선집)]
* ID 변수 설정 -> 데이터 병합 -> 타깃 변수 생성 -> 기타 변수 데이터 처리
* ID 변수 설정
    * 널 체크 : df['ID'].isnull().sum()
    * 중복 체크 : print(len(df['ID']), len(pd.unique(df['ID'])))
    * 숫자만 있는지 체크 : print(pd.to_numeric(df['ID'], errors='coerce').isna().sum())
* 데이터 병합
    * 설정된 ID 변수를 기존 df와 합쳐준다.
    * comb = pd.merge(df_id, df, how='inner', on='ID')
* 타깃 변수 생성
    * 결측치 제거.
    * 박스플랏 확인 -> 이상치 제거.
    * 분류일 경우 인덱싱.
* 기타 변수 데이터 처리
    * 변수명 뒤에 _x나 _y 등 수정.
    * 타깃변수, 불필요, 중복인 변수 제거.
    * 공통 처리
        * 널 체크, dtype 체크 : df.info()
        * 널 비율이 50% 이상이면 제거 : df.isnull().mean().sort_values(ascending=False)
        * (범주형인 경우 널이 20~30%인 케이스가 있고, 중요한 데이터일 가능성이 있다.)
        * numeric인 피쳐명으로 구성된 numeric_names 리스트 생성.
        * category인 피쳐명으로 구성된 category_names 리스트 생성.
    * numeric
        * 널 체크 : df[numeric_names].isnull().mean().sort_values(ascending=False)
        * 널 없는게 정상
        * 분포 확인 : df[numeric_names].describe(); pd.option.display.float_format = f'{:.2f}'
        * 상식선에서 음수값이나 이상치 제거.
        * df_numeric 따로 분리.
    * category
        * 널 체크 : df[category_names].isnull().mean().sort_values(ascending=False)
        * 널 값 대체(무응답을 뜻하는 임의값)
        * 분포 확인 : df[category_names].describe(); pd.option.display.float_format = f'{:.2f}'
        * df_category 따로 분리.
    * 병합 : pd.concat([df_numeric, df_category], axis=1)
    * csv 따로 저장.
<br><br>



## `[EDA 및 시각화]`
* EDA : Exploratory Data Analysis, 탐색적 자료 분석.
* 산점도
    * 산점도 그릴 피쳐명으로 구성된 scatter_names 리스트 생성.
    * g = sns.PairGrid(df[scatter_names])
    * g.map_diag(sns.histplot)
    * g.map_offdiag(sns.scatterplot)
    * plt.show()
* 히스토그램
    * 단일
    * sns.histplot(data=df, x='feature').set_title('title')
    * plt.show()
    * 오버랩
    * sns.histplot(data=df, x='feature', hue='feature').set_title('title')
    * plt.show()
* 박스플랏
    * 단일
    * sns.boxplot(data=df, x='feature').set_title('title')
    * plt.show()
    * 비교
    * sns.boxplot(data=df, x='feature', y='feature').set_title('title')
    * plt.show()
<br><br>



## `[용어]`
* Retention : 제품의 첫번째 사용 시점 이후, 일정 시간 뒤에 재사용 하는 사용자 비율
* 사일로 : 데이터 저장소, 곡식 벌크 저장고에서 유래됨
* outlier : 이상치<br><br>