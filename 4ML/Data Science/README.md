# Data Science

## `[Data Science]`
* 다양한 종류의 데이터로부터 지식과 인사이트를 추출하는 융합분야.
* 과학적 방법론, 프로세스, 알고리즘, 시스템 등을 동원한다.
* 통계학, 데이터분석, 머신러닝, 패턴인식을 통합하는 개념으로 정의한다.<br><br>

### [라이브러리]
* 넘파이 : array 가공 라이브러리.
    * shape : (샘플 수, 특성 수) 보기
    * column_stack : 계산된 컬럼 추가
* 판다스 : 데이터 분석 및 가공에 주로 사용되는 라이브러리.
    * columns, head(), tail(), shape, info(), describe() : 정보 보기
    * mean(), sum(), max(), min() : 집계함수
    * rename() : 컬럼명 바꾸기
    * value_counts(): 각 컬럼에 몇개의 데이터가 있는지 확인
    * query() : 조건에 맞는 데이터만 추출 가능(df 출력)
    * groupby() : 특정 컬럼 1개로 피벗테이블 작성 가능
    * nlargest() : top n개 뽑아내기
    * len(df.loc[df[]==0]) : 원하는 값 개수 조회
    * pd.read_excel : 엑셀 리딩, 시트 지정 필수, 행렬 지정 리딩 가능.
* 피클 : 자료형의 변환 없이 그대로 피클파일로 저장하는 라이브러리.
    * csv나 excel로 구동하는 것보다 속도가 매우 빠르다.
* pyplot : 시각화 및 그래프 생성에 주로 사용되는 라이브러리.<br><br>

### [Data Base]
* 여러 사람이 공유하여 사용하는 데이터의 집합.
* 확장순서 : 데이터 -> 데이터 구조 -> 데이터 클래스 -> 데이터 프레임 -> 데이터 베이스 -> 데이터 웨어하우스 -> 데이터 센터
* 분야별 종사자 마다 부르는 명칭이 다르다. 눈치껏 알아듣자.
    * 컬럼 = 열 = 필드 = 속성 = 프로퍼티(속성값) = 변수 = 피쳐 = 팩터 = 인스턴스 변수 = 멤버 변수
    * 로우 = 행 = 튜플 = 레코드 = 케이스
* 스키마(=테이블 헤드) : 테이블을 디자인하기 위한 구조.(컬럼명의 집합)
* 인스턴스(=테이블 바디) : 테이블에 들어있는 데이터들. (행의 집합)<br><br>

### [데이터의 종류]
* 메타 데이터 : 데이터에 관한 구조화된 데이터. 다른 데이터를 설명해주는 데이터.(=스키마)
* 정형 데이터 : 파일에 있는 데이터. 구조화 되어 있어서 바로 사용 가능.
* 비정형 데이터 : 파일이 아닌 데이터. 구조화 되어 있지 않아 바로 사용할 수 없음.
* 시계열 데이터 : 시간이 포함된 매트릭스 데이터.<br><br>

### [ETL]
* Extraction Transform Load, 일반적인 데이터파이프라인 flow.
* 하나의 시스템에서 data를 추출 변환하여 DB에 적재하는 역할을 함.<br><br>

### [프로젝트의 플로우차트]
* 1.문제제기
* 2.데이터 구하기
* 3.타깃 변수 설정
* 4.데이터 처리 (ID 변수 확인, 타깃 변수 생성)
* 5.탐색적 자료 분석 및 시각화(결측값 제거, 요약 통계 확인, 이상치 제거, 상관관계 확인, 시각화)
* 6.머신러닝 모델 수립
* 7.머신러닝 모델 실행(결정 트리, 로지스틱 회귀, 신경망, KNN)
* 8.데이터 후처리(데이터 분할, 데이터 변환, 데이터 구간화, 모델 재실행)
* 9.최적 모델 선정 및 활용<br><br>


## `[용어]`
* Retention : 제품의 첫번째 사용 시점 이후, 일정 시간 뒤에 재사용 하는 사용자 비율
* 사일로 : 데이터 저장소, 곡식 벌크 저장고에서 유래됨
* outlier : 이상치<br><br>