# Power BI

## `[파워BI 개요]`
* 맥북 설치 불가 (ㅎㅁㅎ?)
<br><br>

### [작업 환경]
* 루커 스튜디오와 매우 유사하다.
* 시각화 탭
* 데이터 탭
* 좌측
    * 보고서 보기: 대시보드 보기
    * 데이터 보기: 테이블 미리보기
    * 모델 보기: ERD로 보기
<br><br>

### [데이터 가져오기]
* csv 가져오기
    * 상단 툴바 -> 데이터 가져오기 -> 텍스트.csv 클릭
    * 컬럼명이 망가져 있다.
    * 상단 툴바 -> 데이터 변환 -> 데이터 변환 클릭
    * 상단 툴바 -> 첫 행을 머리글로 사용 클릭
    * 닫기 및 적용
    * 상단 툴바 -> 데이터 변환 -> 데이터 변환 클릭
    * 컬럼 전체 선택 -> 상단 툴바 -> 변환 탭 -> 데이터 형식 검색
    * 닫기 및 적용
* MySQL 가져오기
    * 상단 툴바 -> 데이터 가져오기 -> mysql 검색 -> mysql 선택
    * 서버(localhost), 데이터베이스(HR) 입력
* MySQL로 가져오는게 더 편한다.
<br><br>

### [열 추가 탭]
* 상단 툴바 -> 데이터 변환 -> 데이터 변환 클릭 -> 상단 툴바의 '열 추가' 탭
* 계산된 컬럼 추가
    * 상단 툴바 -> 예제의 열 -> 선택 항목에서 -> 컬럼 선택, 함수 입력
* 조건 열 추가
    * 상단 툴바 -> 조건 열 -> 조건에 따른 알고리즘 만들기
* 열 병합
    * 여러 컬럼 선택 -> 상단 툴바 -> 열 병합 가능
<br><br>

### [변환 탭]
* 상단 툴바 -> 데이터 변환 -> 데이터 변환 클릭 -> 상단 툴바의 '변환' 탭
* 서식
    * 텍스트 컬럼 선택 -> 상단 툴바 -> 서식
    * 모두 소문자로 변경 가능, 접두사나 접미사 붙이기 가능
* 추출
    * 텍스트 컬럼 선택 -> 상단 툴바 -> 추출
    * 문자 길이 자르기 가능
* 통계
    * 숫자 컬럼 선택 -> 상단 툴바 -> 통계
    * 통계값 계산 가능
* 표준
    * 숫자 컬럼 선택 -> 상단 툴바 -> 표준
    * 사칙연산 및 백분율 가능
<br><br>



## `[Visualization]`

### [Bar 그래프]
* 시각화 탭 -> 꺾은 선형 및 묶은 세로 막대형 차트 클릭
* 데이터 탭에서 시각화 탭의 x축 y축으로 드래그 앤 드랍
* 열 y축 = Bar 그래프
* 선 y축 = line 그래프
* 두개 같이 표현 가능
<br><br>

### [Stacked bar 그래프]
* 시각화 탭 -> 누적 세로 막대형 차트
* 데이터 탭에서 시각화 탭의 x축 y축으로 드래그 앤 드랍
* 범례에 컬럼 추가하면 누적 그래프 표현 가능
<br><br>

### [다양한 bar 그래프]
* 완성된 그래프를 시각화 탭에서 변경 가능
* 묶은 세로 막대형 차트
* 100% 누적 막대형 차트
<br><br>

### [Pie 그래프]
* 원형 차트, 도넛형 차트
<br><br>

### [Table 시각화]
* 시각화 탭 -> 테이블
* 컬럼 추가하면 옆으로 계속 늘어난다.
* 아래 삼각형 누르면 집계함수 사용 가능
<br><br>

### [Matrix 시각화]
* 시각화 탭 -> 행렬
* 열에 있는 컬럼 행으로 다 넣기
* +/- 없앨 수 있다.
* 계단형을 펼칠 수 있다.
* 부분합 없앨 수 있다.
* 조건부 서식
    * 값의 컬럼 아래 삼각형 -> 조건부 서식 -> 배경색
    * 엑셀처럼 규칙 작성하면 원하는 경우만 배경색 설정 가능
    * 그라데이션도 줄 수 있다.
    * 데이터 막대도 그릴 수 있다.
* 테이블이랑 사실상 같은 데이터인데 모양만 다르다.
* 개인적으로는 행렬이 더 보기 좋은 듯 하다.
<br><br>

### [신규 테이블과 관계 생성]
* 신규 테이블 생성
    * 상단 툴바 -> 데이터 입력 -> 테이블 값 입력 -> 로드
    * 제일 우측 데이터 탭에 생겼다.
* 관계 설정
    * 좌측 -> 모델 보기 -> 키값 드래그 앤 드랍 방식
    * (신규 테이블 키 컬럼) 드래그, (원래 테이블 컬럼) 드랍
* 열 순서 변경
    * 신규 테이블은 원래 테이블 순서랑 바뀌는 경우가 많다.
    * 원래 테이블과 일치하게 만들기
    * 데이터 탭 -> 신규 테이블의 원하는 컬럼 클릭 -> 상단 툴바 -> 열 기준 정렬 -> 원래 테이블과 같은 컬럼 (=키)로 선택
<br><br>

### [DAX 식]
* 파워 BI에서 사용하는 식
* CALCULATE
    * 조건에 해당되는 경우만 집계하는 함수
    * CALCULATE(<expression>, <filter1>, <filter2> [, _])
    * expression은 sum, avg, min, max 등등 집계함수
    * filter는 조건, (ex. 테이블1의 col 값과 테이블2의 col 값이 같을 때)
* SUMX
    * 컬럼을 만들고 계산한 값을 저장하고 싶을때 사용하는 함수
    * col = SUMX(<table>, <expression>)
    * 데이터 탭에 calculation에서 저장된 것을 볼 수 있다.
* SWITCH
    * value 값을 바꾸면 컬럼의 결과도 바뀌는 함수
    * 지표를 선택할 때마다 그래프가 바뀌게 하고 싶을때 사용한다.
    * SWITCH(<expression>, <value1>, <result1>, <value2>, <result2>, ...)
* DATEDIFF
    * 날짜 두개 사이의 차이가 몇인지 출력하는 함수
    * DATEDIFF(<Date1>, <Date2>, <Interval>)
    * Interval에서 연월일시분초 등에서 뭘로 계산할지 고를 수 있다.
* CALENDAR
    * 첫 날짜부터 끝 날짜까지 쭉 나열하여 생성하는 함수
    * CALENDAR(<start_date>, <end_date>)
    * 조인해서 사용하는 편이다.
<br><br>

### [슬라이서 버튼]
* 원하는 항목만 필터링 해주는 버튼, 토글 버튼
* 시각화 탭 -> 슬라이서 클릭 -> 필드 값에 원하는 컬럼 추가
* 체크박스 말고 큰 타일 형태도 가능
* 슬라이서는 그래프 만들 때 생성하는 것
* 필터는 맨 처음 대시보드 만들 때 생성하는 것
* 기능은 사실상 같다.
<br><br>

### [Line 그래프]
* 시각화 탭 -> 꺾은 선형 차트 클릭
* 데이터 레이블 추가 가능
* 레이블 밀도 조절 가능
* 추세선 넣기 가능
* 범례에 컬럼 넣으면 각각의 라인 그릴 수 있다.
    * 축소 다중 항목 사용하면 각 라인을 분리할 수 있다.
    * 축을 공유하기 때문에 보기 편할 경우가 있다.
<br><br>

### [영역 그래프]
* 시각화 탭 -> 누적 영역형 차트 클릭
* 범례에 컬럼 넣으면 여러 영역 표현 가능하다.
<br><br>

### [Waterfall 그래프]
* 데이터에 비교대상이 어떤 이유로 gap이 발생하는지 표현하는 차트
* 주식 봉차트에서 꼬리 없는 것과 동일하게 생겼다.
* 시각화 탭 -> 폭포 차트 클릭
* 오름차순으로 선택하면 보기 좋다.
* 시각화 탭 -> 최대 분석 결과 -> 숫자를 늘리면 더 길게 볼 수 있다.
<br><br>

### [분해 트리]
* 단계적으로 컬럼 하나씩 어떻게 바뀌는지 보기 위한 트리 그래프
* 시각화 탭 -> 분해 트리
* 컬럼 넣기 -> 시각화된 곳에서 +버튼 -> 높은 값 선택 (반복)
<br><br>



