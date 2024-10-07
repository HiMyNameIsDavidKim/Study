# Tableau

## `[태블로 개요]`

### [데이터 분석가의 주요 업무]
* 경영진 리포팅
* 실시간 모니터링 대시보드
* 분석 과제 수행
<br><br>

### [BI]
* Business Intelligence
* 비즈니스 의사결정에 데이터가 사용되는 방식
    * data-driven, 구체적 방향 도출
    * data-informed, 이전 성과에 대한 이해
    * data-inspired, 새로운 방향성
* 데이터가 중요한 것은 맞지만 복잡하고 다루기 힘들다.
* BI는 데이터가 비즈니스에 사용될 수 있게 지원하는 모든 활동이다.
* 데이터 시각화
    * 정보와 데이터를 그래프로 나타내는 것이다.
    * 접근하기 쉽게 시각적 요소로 나타낸다.
    * 막대한 양의 정보를 분석하고 의사결정을 내리는데 필수적이다.
<br><br>

### [BI Tools]
* 과제 -> 데이터셋 체크, 지표설계 -> 시각화 -> 인사이트
* BI 툴 3대장: Tableau, Looker studio, power BI
* 파이썬, SQL으로 집계 및 전처리
* 태블로, 루커 스튜디오로 시각화
* 추가로 결과를 바탕으로 어떤 일을 해야하는지 생각
<br><br>

### [태블로]
* 가장 대표적인 BI 툴
* 시각화 툴을 다루기 힘들어서 만든 툴
* 장점
    * 인터페이스가 직관적, 드래그 앤 드랍 방식
    * 다양한 시각화 지원, 차트 종류 다양
    * 다양한 데이터 소스 연동
* 태블로 데스크탑: 유료, 2주 체험, 학생 1년 무료
* 태블로 퍼블릭: 무료, 공개 데이터만 가능, 분석 자료 다운 불가
* 데스크탑으로 설치 (학생 1년 무료 구글링)
<br><br>

### [핵심 데이터]
* 도메인: 현업 도메인을 알아야 분석이 가능하다.
* 시장과 트렌드: 외부의 변화로 기업이 영향을 받는다.
* 경쟁사의 데이터: 경쟁사에 대한 대응이 필요하다.
<br><br>

### [대시보드 설계]
* 가장 먼저 대시보드를 왜 만들어야 하는지 의도를 파악해야 한다.
* (key question -> 지표) 형태로 변환한다.
* 보통 key question이 먼저 생기고, 데이터셋을 찾고, 지표 분석에 들어간다.
* 지표에 대한 시각화는 최소한의 개수로 준비한다.
<br><br>



## `[태블로 기초]`

### [태블로 인터페이스]
* 
<br><br>








## `[실습환경 준비]`

### [스프레드 시트 연동]
* 스프레드 시트
    * 구글 스프레드 시트에 올리면 태블로에 연결 가능
    * 파일 1개 안에 시트 여러개 사용해서 파일 1개에 다 넣기
* 태블로
    * 왼쪽 구글 드라이브 선택
    * 구글계정 로그인
    * 액세스 허용 버튼 클릭
    * 만들어 놓은 스프레드 시트 불러오기
    * 화면 위로 드래그 드랍
    * 데이터 원본의 메타데이터 확인 가능
    * 시트1 클릭
    * 작업 시작
* 파일 저장
    * 상단에 파일 클릭
    * 다른 이름으로 저장
    * 태블로 통합문서: 대시보드만 저장
    * 태블로 패키지 통합문서: 대시보드랑 데이터 같이 저장
<br><br>



## `[실습: 시장 동향 분석]`

### [이커머스 데이터셋]
* 통계청에 매월 발표하는 공식 `온라인쇼핑동향` 데이터셋
* 온라인쇼핑거래액
    * 단위는 백만원
    * 월단위로 데이터 제공
    * 상품군 23개 구분
    * 판매매체 구분: 모바일 쇼핑, 인터넷 쇼핑
    * 취급범위 구분: 종합몰, 전문몰
    * 운영형태 구분: 온라인매장, 온오프라인 복합
* 데이터셋 문제점
    * 이미 피벗된 상태
        * 구분 별로 총합집계와 중간집계가 있어서 지워줘야 한다.
        * 데이터가 일자별로 세로로 진행되야 하는데 가로로 진행된다.
    * 세부 상품군 존재
        * 한 상품군 안에 세부 상품군이 있어서 지워줘야 한다.
    * 데이터 양식 불일치
        * 월 컬럼 이름 양식이 자꾸 바뀐다.
        * 미래 추정치는 `p)`로 나타낸다.
<br><br>

### [데이터셋 재구조화]
* 파이썬 전처리 과정
* csv 전처리는 os 이용해서 for문으로 효율적으로 돌리기
* 한글 csv 인코딩 불러오기
    * df = pd.read_csv(path, encoding='cp949')
    * df = pd.read_csv(path, encoding='utf-8')
    * df = pd.read_csv(path, encoding='utf-8-sig')
* 한글 csv 인코딩 저장
    * df = pd.to_csv(path, encoding='cp949', index=False)
    * df = pd.to_csv(path, encoding='utf-8', index=False)
    * df = pd.to_csv(path, encoding='utf-8-sig', index=False)
* 피벗 테이블 해체
    * 가로 데이터 -> 세로 데이터
    * df.melt()
    * df.melt(id_vars='유지할 컬럼')
        * id_vars 파라미터
        * 유지할 컬럼은 그대로 가로로 유지, 나머지만 세로로 변환
        * 예를들어 구분인 3개 컬럼 유지, 날짜인 나머지 컬럼만 변환
        * df.melt(id_vars=df.columns[:3])
    * df.melt(id_vars=df.columns[:3], var_name='날짜', value_name='거래액')
        * var_name, value_name 파라미터
        * 변수의 이름과 값의 이름 지정
* 피벗 테이블
    * 세로 데이터 -> 가로 데이터
    * df.pivot()는 집계 능력이 없으므로 df.pivot_table() 사용
    * df.pivot_table()
    * df.pivot_table(index=['date'])
        * index 파라미터
        * 인덱스로(왼쪽으로) 보낼 컬럼 입력
    * df.pivot_table(index=['date'], columns=['menu'])
        * columns 파라미터
        * 컬럼으로(위로) 보낼 컬럼 입력
    * df.pivot_table(index=['date'], columns=['menu'], values=['count'])
    * df.pivot_table(index=['date'], columns=['menu'], values=['price'])
    * df.pivot_table(index=['date'], columns=['menu'], values=['count', 'price'])
        * values 파라미터
        * 넣을 값 선택
        * 한번에 여러개도 가능
    * df.pivot_table(index=['date'], aggfunc='sum')
    * df.pivot_table(index=['date'], values=['count', 'price'], aggfunc='sum')
    * df.pivot_table(index=['date'], values=['count', 'price'], aggfunc={'count':'sum', 'price':'mean'})
        * aggfunc 파라미터
        * 기본값은 mean이라 입력 안하면 평균으로 계산
        * 집계할 함수 선택
        * 값마다 집계함수 다르게 선택 가능
* 스트링 숫자로 변환
    * str2int 함수 하나 만들어서 데이터 보면서 알고리즘 작성
    * df['거래액'] = df['거래액'].apply(str2int)
    * 출력된 dtype 이 int 됐는지 확인
<br><br>












