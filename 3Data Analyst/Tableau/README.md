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
* 작업 화면
    * 태블로 작업 시 메인 화면
    * 왼쪽 위 태블로 로고 클릭 -> 데이터 연결 클릭
* 사이드바
    * 가장 왼쪽에 위치
    * 데이터셋 표시
    * 데이터 탭과 분석 탭이 있다.
    * 컬럼을 데이터 필드라고 부른다.
    * 각 컬럼이 어떤 데이터 타입인지 아이콘으로 표시
    * Abc(스트링), #(숫자), 달력(날짜), 등
* 마크 카드
    * 시각화 관련 툴 모음
    * 현재 작업중인 데이터 필드를 수정할 수 있다.
    * 새 데이터 필드를 여기에 드래그 앤 드랍해서 사용해도 된다.
* 선반
    * 가운데 위에 '행' 부분과 '열' 부분
    * 사이드바에서 데이터를 올리는 부분
* 뷰
    * 선반 바로 아래 위치
    * 선반에 올린 데이터가 시각화되어 표현되는 부분
* 표현 방식
    * 오른쪽 상단에 위치
    * 태블로가 제공 기본 차트를 결정할 수 있다.
<br><br>

### [차원과 측정값]
* 차원
    * 사이드바 데이터 탭에 회색선 위
    * 정성적인 값 (ex. 이름, 날짜)
* 측정값
    * 사이드바 데이터 탭에 회색선 아래
    * 정량적인 수치 값 (ex. 집계값)
* 예시
    * 차원을 기준으로 측정값을 집계하여 시각화
    * 상품 카테고리별 매출: 상품(차원), 매출(측정값)
    * 성별에 따른 평균 키: 성별(차원), 키(측정값)
* 차원을 먼저 클릭하면 표 형태로 나온다.
* 측정값을 먼저 클릭하면 바 그래프로 나온다.
* 측정값 이름
    * 차원과 측정값 밑에 따로 표시되어 있다.
    * 측정값만 따로 모아둔 것이다.
* 차원 <-> 측정값
    * 차원 데이터 필드 선택 -> 오른쪽 아래 삼각형 -> 측정값으로 변환
    * 드래그 앤 드랍으로 회색선 기준 아래로 내려도 된다.
    * 반대로 측정값을 차원으로 바꾸는 것도 가능하다.
    * 목적에 의해 측정값을 기준으로 차원을 나타낼 때 유용하다.
<br><br>

### [연속형과 불연속형]
* 연속형
    * 녹색으로 표시
    * 통계학적으로 연속된 값
    * 시각화를 그라데이션으로 해준다.
* 불연속형
    * 파란색으로 표시
    * 통계학적으로 불연속된 값
    * 시각화를 전혀 다른 색으로 해준다.
* 선반에 올려놓으면 박스 색깔로 보인다.
* 사이드바에서도 아이콘의 색깔로 보인다.
* 주로 차원은 불연속형 측정값은 연속형인 경우가 많다.
    * 하지만 반드시는 아니고 반대일 경우도 있다.
<br><br>

### [관계와 조인]
* 태블로에서도 SQL의 조인을 할 수 있다.
* 쿼리를 안짜고 설정만 해줘도 가능하다.
* 추가적으로 관계를 통해서 조인보다 더 쉽게 가능하다.
* 태블로에서는 조인보다 관계를 추천
* 태블로에서 조인 적용
    * 데이터 원본 시트
    * 네모난 데이터 박스 더블클릭
    * 여기에 드래그 앤 드랍으로 다른 데이터 넣기
    * 결합방식 클릭해서 조인 방식 선택
    * 바로 그 아래에 각각의 컬럼 선택해서 조인키 설정
    * 처음 데이터보다 데이터 행 수가 늘어나는지 꼭 확인!!
* 태블로에서 관계 적용
    * 데이터 원본 시트
    * 네모난 데이터 박스 더블클릭
    * 여기에 드래그 앤 드랍으로 다른 데이터 넣기
    * 연결선으로 이어진 경우 관계가 사용된 것
    * 에러 표시 더블클릭
    * 각각의 컬럼 선택해서 관계에 사용할 키 설정
    * 여러 컬럼 선택해서 다 관계짓기 가능
    * 한 시트에 여러 시트를 관계짓기 가능
<br><br>



## `[태블로 심화]`

### [매개변수 개요]
* 동적으로 상호작용할 수 있게 해주는 변수
* 매개변수를 바꿔서 전체 대시보드를 토글할 수 있다.
* 매개변수 만들기
    * 데이터 패널에서 우클릭 -> 매개변수 만들기
    * 매개변수(p_) 표시하여 이름 수정, 데이터 유형은 정수
    * 허용 가능한 값을 목록으로 수정, 목록 작성
    * 확인 클릭
    * 데이터 패널 아래 매개변수 우클릭 -> 매개변수 표시
    * 매개변수의 값을 선택할 수 있다.
    * 계산된 필드 만들어서 사용하면 된다.
    * ex. 달러 * p_통화(KRW)
* 매개변수에 따른 그래프 토글
    * 쿼리문 작성
    * case [p_지표선택]
        when 'New Ord Amt' then sum([New Ord Amt])
        when 'Ord Cnt' then sum([Ord Cnt])
        when 'Prd Cnt' then sum([Prd Cnt])
    end
    * 선반의 기존 측정값을 매개변수로 변경
    * 매개변수 선택에 따라 그래프가 바뀐다.
* 대시보드 전체에 적용
    * 상단탭 대시보드 -> 동작추가 -> 매개변수 변경 -> 원본필드 설정 -> 확인
    * 특정 시트의 값 클릭 = 매개변수 변경 = 대시보드의 모든 시트 토글
<br><br>

### [IF와 IIF]
* 원하는 조건에서 다른 색으로 표시하는 함수
* 계산된 필드 만들기
    * 코드 입력
    * if avg([Cust Cnt]) >= 200 then '200명 이상'
    else '200명 미만'
    end
    * 조건이 하나라면 iif가 코드가 더 간결하다.
    * iif(avg([Cust Cnt]) >= 200, '200명 이상', '200명 미만')
* 마크 카드의 색상에 계산된 필드 올리기
* 상호작용을 하고 싶다면 매개변수와 연계
    * 0~500 사이를 스텝사이즈 50으로 움직이는 매개변수 만들기
    * 계산된 필드 만들기 (avg([Cust Cnt]) >= [p_기준])
    * 색상으로 적용
<br><br>



## `[시각화]`

### [하이라이트 테이블]
* 엑셀을 선호할 시 좋은 테이블
* 일종의 히트맵 그래프 이다.
* 차원 하나 먼저 선택
* 측정값 하나 선택
* 마크 카드 색상에 측정값 드래그 앤 드랍
* 마크 카드 자동을 사각형으로 변경
* 측정값 컬럼 윗부분 마우스 갖다대고 뜨는거 클릭 -> 내림차순 변경
* 사이드바 분석탭 총계 더블클릭
* 비율 그래프
    * 마크 카드 -> 레이블 우측 삼각형 클릭 -> 퀵테이블 계산 -> 구성비율
* 2개 이상의 컬럼
    * 차원 하나 선택
    * '측정값 이름' 선택
    * 2개 이상의 컬럼 구성하기
    * 측정값을 합계, 평균, 최소, 최대 등 수정 가능
    * 컬럼명 커스텀하게 변경
<br><br>

### [바 그래프]
* 눈으로 한눈에 보기 좋은 그래프
* 측정값 하나 먼저 선택
* 차원 하나 선택
* 툴바에서 그래프 가로세로 변경 가능
* 툴바에서 표준 클릭 -> 전체 보기로 변경
* 마크 카드 레이블에 측정값 드래그 앤 드랍해서 값 표시
* 커맨드 + 선반에서 차원 or 측정값 드래그 -> 마크 카드에 색상에 드랍
* 마크 카드 색상 클릭 -> 색상 편집 -> 색상 표 수정 가능
* 사이드바 분석 탭 -> 평균선 추가 가능
* 마크 카드 측정값 레이블 우클릭 -> 서식
    * 맞춤 -> 가운데 정렬
    * 폰트 사이즈 키우기
* 마크 카드에 레이블 클릭 -> 점 3개 -> 서식 커스텀 가능
<br><br>

### [누적 바 그래프]
* 1개의 측정값에 대하여 2개 이상의 차원을 사용하는 경우
* 카테고리 수가 적은 차원을 마크 카드 색상에 넣기
* 카테고리 내부의 비중만 보고싶을 경우
    * 선반에 측정값 오른쪽 삼각형 -> 다음을 사용하여 계산 -> 카테고리 차원
    * 마크 카드 레이블에 측정값 드래그 앤 드랍해서 값 표시
    * 레이블도 오른쪽 삼각형  -> 다음을 사용하여 계산 -> 카테고리 차원
<br><br>

### [파이 차트]
* 비중을 나타내는 대표적인 그래프
* 차원의 수가 적을 때 유리하다.
* 측정값 하나 먼저 선택
* 차원 하나 선택
* 우측 상단 표현 방식 -> 파이 차트 선택
* 툴바에서 표준 -> 전체 보기로 수정
* 툴바에서 내림차순 정렬
* 측정값이랑 차원 마크 카드 레이블에 넣기
* 측정값 퀵테이블 계산 -> 구성 비율
<br><br>

### [트리맵 차트]
* 차원의 수가 많을 때 사용하는 비중 그래프
* 미국주식 등락률 그래프가 대표적이다.
* 측정값 하나 먼저 선택
* 차원 하나 선택
* 우측 상단 표현 방식 -> 트리맵 차트 선택
* 측정값 마크 카드 레이블에 넣기
* 측정값 퀵테이블 계산 -> 구성 비율
<br><br>

### [라인 그래프]
* 가장 대표적이고 유용한 그래프
* 주로 시계열 데이터에서 많이 사용한다.
* DATEPARSE
    * 날짜가 문자열일 경우 변환이 필요하다.
    * 태블로 날짜 규칙 확인
    * 사이드바 데이터 탭에서 우클릭 -> 계산된 필드 만들기
    * 데이터 필드 명칭 입력 -> 함수 입력
    * 컴퓨터 설정의 언어가 영어인지 확인 (파일 -> 통합문서 로켈)
    * DATEPARSE('MMM.yy', [Date])와 같이 입력
* 측정값 하나 먼저 선택
* 시계열 같은 차원 선택
* 선반에 년 왼쪽에 + 클릭 -> 분기 + 클릭 -> 분기 날리기
* 측정값을 마크 카드 레이블에 넣기 -> 레이블 클릭 -> 최대/최소만 표시
* 사이드바 분석 탭에서 연도별 평균선 긋기 가능
* 필요하면 평균선 클릭해서 편집 -> 레이블에서 값도 표시
* 축 레이블 클릭 -> 날짜에서 숫자로 변경 가능
* 선반에서 차원 클릭 -> 위에 말고 밑에 년월 클릭 -> 연속형으로 변경 가능
<br><br>

### [영역 차트]
* 시간에 따라 비중의 변화를 볼 때 사용하는 그래프
* 선반에서 측정값 -> 퀵테이블 계산 -> 구성 비율
* 마크 카드에서 측정값 -> 퀵테이블 계산 -> 구성 비율
* 선반에서 측정값 -> 다음을 사용하여 계산 -> 테이블 아래로
* 마크 카드에서 측정값 -> 다음을 사용하여 계산 -> 테이블 아래로
* 라인 그래프를 그리고 마크 카드에서 영역으로 변경
* 시간에 따른 비중을 보고싶은 차원을 드래그 해서 색상에 드랍
<br><br>

### [응용 라인 그래프]
* 측정값 하나 먼저 선택
* 시계열 같은 차원 선택
* 선반에서 커맨드 + 측정값 바로 옆으로 드래그 앤 드랍
* 이중축
    * 아래 차트 측정값 -> 퀵테이블 계산 -> 누계로 변경
    * 아래 차트 측정값 -> 이중축 선택
* 선 위에 포인트 주기
    * 선반에서 아래 차트 측정값 클릭
    * 마크 카드에서 선을 원으로 변경
    * 아래 차트 측정값 -> 이중축 선택 
    * 축 우클릭 -> 축 동기화
    * 축 우클릭 -> 머리글 표시 해제
<br><br>

### [도넛 차트]
* 파이차트 가독성 개선
* 도넛 구멍에 값 작성 가능
* 선반 열에 0 입력 -> 측정값 평균으로 변경
* 선반에서 커맨드 + 측정값 바로 옆으로 드래그 앤 드랍
* 마크 카드에서 전체를 파이차트로 변경
* 첫번째 파이
    * 마크 카드에서 각도에 측정값 드래그 앤 드랍
    * 마크 카드에서 크기 키우기
    * 마크 카드에서 레이블에 측정값 드래그 앤 드랍 -> 퀵 -> 구성비율로 변경
    * 마크 카드에서 색상에 차원 드래그 앤 드랍
* 두번째 파이
    * 도넛 중앙에 적고싶은 값을 마크 카드 레이블에 넣기
    * 크기 적당히 조절
    * 색상 흰색으로 변경
    * 선반에서 측정값 우클릭 -> 이중축 선택
* 합쳐진 테이블에서 위아래 머릿글 모두 해제
* 도넛 바깥 우클릭 -> 서식 -> 라인 -> 격자선 없음, 영기준선 없음
<br><br>

### [변형 바 그래프]
* 측정값 하나 먼저 선택
* 차원 선택
* 가로로 변경
* 바 두께 적당히 늘리기
* 선반 열에 1 입력 -> 측정값 평균으로 변경
* 메인 바 그래프에 측정값을 레이블 추가, 구성비율로 변경
* 1로된 측정값 이중축
* 메인 바 그래프의 축 우클릭 -> 맨 앞으로 마크 이동
* 1로된 측정값 우클릭 -> 축 동기화, 머릿글 해제
* 1로된 마크 카드 색상 -> 테두리 검은색, 불투명도 100%
<br><br>



## `[대시보드 설계]`

### [대시보드 정의]
* 여러 차트를 한 페이지에 나타내는 것
* 핵심 포인트
    * 대시보드를 만드는 목적
    * 대시보드의 사용자
    * 대시보드의 콘텐츠
* 기본에 충실하고 너무 꾸밀 필요 없다.
    * 정보가 모두 있는지 체크
    * 불필요한 내용은 없는지 체크
    * 시각적 요소가 일반적인지 체크
    * 간결하고 바로 알아차릴 수 있도록 강조하기
* 일반적인 대시보드 설계
    * 상단에 스코어 카드(숫자로 구성된 표)
    * 그 밑에 2~3개 차트
    * 최상단에 대시보드의 타이틀
<br><br>

### [대시보드 만들기]
* 하단에 시트 만들기 옆에 대시보드 만들기 클릭
* 사이드바 크기
    * 일반 데스크톱 사이즈
    * 회사마다 다르니 맞게 설정
* 사이드바 시트
    * 앞에서 만든 시트들 추가 가능
    * 드래그 앤 드랍 가능
* 사이드바 개체
    * 텍스트나 이미지 추가 가능
<br><br>

### [대시보드 필터]
* 원하는 값만 필터링하는 기능
* 마크 카드 바로 위에 필터 있음
* 여기에 필터링할 차원 넣기
* 차원의 삼각형 클릭 -> 필터 표시
* 우측에 필터창 사용 가능
* 모든 데이터에 적용 가능
    * 필터창 삼각형 클릭 -> 워크시트에 적용 -> 이 데이터 원본을 사용하는 모든 항목
    * 대시보드를 만든다면 모든 시트에 일괄 적용된다.
* 한개만 체크 가능한 단일값 모드
    * 대시보드의 필터창 대면 뜨는 삼각형 (기타 옵션) -> 단일값 목록 선택
<br><br>

### [대시보드 하이라이트]
* 원하는 값 외에는 흐리게 보여주는 기능
* 마크 카드에 차원의 삼각형 클릭 -> 하이라이터 표시
* 우측에 하이라이터 사용 가능
* 하이라이터에서 원하는 카테고리 선택하면 하이라이트 적용
<br><br>

### [인터랙티브 대시보드]
* 대시보드에서 상호작용이 가능
* 사용자의 클릭에 따라 대시보드가 변하게 된다.
* 필터나 하이라이트가 적용되게 변한다.
* 필터
    * 상단바 -> 대시보드 -> 동작 클릭
    * 동작 추가 -> 필터 -> 필터 이름 작성
    * 원본시트 대상시트 설정
    * 원본시트: 클릭할 시트 / 대상시트: 변화할 시트
    * 동작 실행 조건 -> 선택으로 변경
    * 선택을 해제할 경우의 효과 -> 모든 값 표시로 변경
    * 확인 -> 확인
* 하이라이트
    * 상단바 -> 대시보드 -> 동작 클릭
    * 동작 추가 -> 하이라이트 -> 하이라이트 이름 작성
    * 원본시트 대상시트 설정
    * 동작 실행 조건 -> 선택으로 변경
    * 대상 하이라이트 -> 선택한 필드로 변경 -> 값 체크
    * 확인 -> 확인
<br><br>

### [대시보드 레이아웃]
* 대시보드 -> 왼쪽 아래, 개체 -> 부동으로 넣으면 겹치거나 플로팅 가능
* 가로 세로 컨테이너를 사용하면 깔끔하게 레이아웃을 짤 수 있다.
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
    * 화면 위로 드래그 앤 드랍
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



## `[실전 팁]`
* 레이블 추가할 때 선반이랑 통일시키는 방법
    * 선반에 있는 측정값 CMD 누르고 드래그 앤 드랍
* 테이블 계산값 어떻게 구하는지 시각화해서 편집
    * 마크 카드에 측정값 아래 삼각형 -> 테이블 계산 편집
* 이동평균선 시각화
    * 측정값 아래 삼각형 -> 퀵테이블 계산 -> 이동평균선
* 연평균 성장률
    * 해당 기간동안 평균적으로 얼마나 성장 했는지에 대한 지표
    * 태블로에서는 통합성장률(CAGR) 사용하면 된다.
    * 산술평균이 아니라 기하평균으로 계산한다.
* 선반에 있는 측정값 바로 바꾸기
    * 원하는 측정값을 해당 측정값 위에 드래그 앤 드랍
<br><br>







