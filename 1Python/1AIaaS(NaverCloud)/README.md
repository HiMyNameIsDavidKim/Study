# AIaaS(Naver Cloud)

## `[Set-up]`
* JDK 11 설치, JDK 11 환경변수 설정
    * 한국의 인공지능은 JDK 11이 표준이다.
* 아나콘다 설치, 아나콘다 환경변수 설정
    * 아나콘다는 데이터 사이언스 기술과 머신러닝의 방법들을 제공한다.
* 파이참 설치, 스튜던트 라이센스 발급
* 환경변수 참고
    * JAVA_HOME : C:\Program Files\jdk-11\bin
    * ANACONDA_HOME1 : C:\ProgramData\Anaconda3
    * ANACONDA_HOME2 : C:\ProgramData\Anaconda3\Scripts
    * ANACONDA_HOME3 : C:\ProgramData\Anaconda3\Library\bin
    * ANACONDA_HOME4 : C:\ProgramData\Anaconda3\Library\mingw-w64\bin<br><br>



## `[Advanced OOP]`

### [Static Method]
* 클래스 밖의 메서드를 클래스 안으로 집어넣을 수 있다.(=랩핑)
* 클래스 밖의 메서드는 스태틱 메서드라고 부른다. (클래스 안은 다이나믹 메서드)
* 화면에 구현할 것을 스태틱 메서드에 넣는다.
* (if문 main) 대신에 @staticmethod를 사용할 수 있다.
* 이때 @를 데코레이터라고 부른다.<br><br>

### [생성자와 소멸자]
* 생성자(constructor) : init 메서드, 객체 지향에서 객체의 초기화를 담당하는 서브루틴.
    * 생성자 괄호 안에 있는 것들이 property 이다.
* 소멸자(destructor) : del 메서드, 객체가 소멸될 때 자동으로 발생하는 서브루틴.
    * 생성되고 소멸이 안되면 메모리가 부족해진다. 반드시 죽여야한다.<br><br>

### [소프트웨어 디자인 패턴]
* 소프트웨어 설계의 특정 문맥에서 공통적인 문제에 대해 재사용 가능한 해결책.
* “바퀴를 다시 발명하지 마라.(Don’t reinvent the wheel.)”
* Gang of Four에 의하면, 23가지 패턴으로 모두 설명이 가능하다.
    * 생성 패턴 : 객체 생성에 관련된 패턴. 객체 생성, 변경이 프로그램 구조에 영향을 주지 않는 것을 추구한다.
        * 추상 팩토리, 빌더, 팩토리 메서드, 프로토타입, 싱글 턴
    * 구조 패턴 : 객체와 클래스를 더 큰 구조로 조립하는 패턴.  효율성 유지를 추구한다.
        * 어뎁터, 브릿지, 컴포지트, 데코레이터, 파사드, 플라이 웨이트, 프록시
    * 행위 패턴 : 알고리즘과 객체 간의 책임을 할당하는 패턴. 작업 분배를 추구한다.
        * 책임 연쇄, 커맨드, 인터프리터, 이터레이터, 중재자, 메멘토, 옵서버, 상태, 전략, 템플릿 메서드, 비지터
* 생성패턴은 인스턴스화에 대한 패턴, 구조패턴은 자료구조에 대한 패턴, 행위 패턴은 함수에 대한 패턴.
    * 책임 할당에서 책임은 반드시 리턴을 준다라는 뜻.<br><br>

### [디자인 패턴 상세 고찰]
* 팩토리 메서드 : 클래스의 프로퍼티를 변경하거나 확장해야 할 때 사용하는 패턴.
    * 모든 코드를 하나하나 수정할 필요가 없으며, factory 메서드를 사용하면 된다.
    * 또한, 2차원 형태의 데이터를 가져올 때, 한줄 한줄 읽는 것이 아니라 한번에 2차원을 읽는다. (ex. [ ][ ] = abc.Abc( ))
* 프로토타입 : 생성할 클래스들의 타입이 프로토타입인 인스턴스로 부터 결정되는 패턴.
    * 객체를 만들기 위해 자기 자신을 복제한다.
    * 모델링 과정에서는 (전처리 - 프로세스 - 테스트)를 계속 반복되는데, 이과정도 프로토타입 패턴이다.
    * 팩토리 패턴과 반대되는 개념. (모델링 = 프로토타입, 완성 후 배포 = 팩토리)
* 상태 : 객체 내부에 또 다른 객체를 만들고, 이를 상태 객체로 정의한다.
    * 메인 객체 = field, 서브 객체 = state
    * (ex. 파이썬의 클로저, SQL의 서브쿼리)<br><br>

### [객체지향의 기본 구조]
* constructor -> static -> information processing -> print
* 객체지향에서 값은 크게 property(포멧), information(처리 완료), data(처리 전) 3가지로 존재한다.
    * property = 컵, information = 커피, data = 커피콩
    * constructor = property, information processing = information, static = data<br><br>

### [CRUD]
* 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능.
* Create, Read, Update, Delete 4가지
    * Read는 2개로 나뉘고, 전체를 보여주는 경우 List(목록). 일부를 보여주는 경우 Search(검색).
* 엔진구조 : 소프트웨어에서 계속 반복해서 돌리다가 원할때 멈추는 구조를 엔진구조라고 한다.
* 스태틱 메인 메서드는 CRUD로 구성된 엔진구조로 설계한다.<br><br>

### [MTV 패턴 설계]
* 전체 프레임워크를 Model, Template, View로 나누는 설계.
* 진행 순서는 init파일 -> 데이터셋 -> 모델 -> 뷰 -> 템플릿
* Model : 모델 수립, (전처리 - 프로세스 - 테스트) 순서로 모델을 완성.
    * DB에 저장되는 데이터, 내부속성값, 클래스
* Template : 출력, 유저와 인터액션하는 인터페이스.
    * 유저에게 보여지는 화면, 스태틱메서드, html 파일
* View : 로직, 각 과정의 순서도만을 보관. 캡슐화.
    * 결과를 템플릿으로 렌더링만 함, 로직, 결과 리턴
    * 뷰가 로직이라고 해서 모델링에 대한 로직도 다 가진 것은 아니다.
* Dataset : 외부에 있는 데이터를 끌어와서 확률을 만들어주는 모듈.
    * 입출력 기능이 없고, 로직만 있는 구조.
    * 스탠다드 클래스와는 다른 데이터 클래스 구조이며, 데코레이터를 달아줘야 한다.
    * context : 파일이 저장된 경로
    * label : 답안지
 - [`작업 순서 메모`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/1Python/2NaverCloud(AIaaS)/2Flask)<br><br>

### [DDD 설계]
* 전체 프레임워크를 Domain Driven Design로 나누는 도메인 주도 설계.
* 데이터 중심 접근이 아니라, 도메인(모델과 로직)에 집중한다.
    * 도메인 자체의 복잡성을 줄이는 것이 특징.
* 엔터티와 VO를 기본 블록으로 사용한다.
    * VO : Value Object, 한개 이상의 속성들을 묶어서 특정 값을 나타내는 객체.
    * 엔터티의 특정 값들을 VO로 묶어서 포장할 수 있다.
    * 개체 : 특정 값을 나타내는 객체. VO는 곧 개체이다.<br><br>



## `[Advanced Python]`

### [Pythonic]
* 파이썬 스럽게 코딩하는 것. 파이써닉.
* 파이썬은 아름다운 하나의 답이 존재한다는 철학이 있다.
* 1.comprehesion 2.f-string 3.swap 4.str 메서드 5. args(*) 6.람다함수와 맵함수 7.kwargs(**) p.generator p.extended slice
    * comprehesion : 축약하기. 한줄 코딩.
        * for문의 Comp. (ex. [i for i in ls])
        * if문의 Comp. (ex. [i if i%2 == 0 else None])
    * 컴프리헨션된 자료는 반드시 자료구조 안에 담아야한다.
    * f-string : 직관적인 문자열. (ex. f”이게 f 스트링{print_fstring}이다.”)
    * swap : 스왑하는 논리. (ex. t = a, a = b, b = t)
    * 프린트 대신 str 메서드를 사용한다. (가독성을 높이기 위함)
    * args(*) : 리스트형 컨테이너 타입의 데이터, 가변 파라미터에 사용.
        * 가변 파라미터 : 들어오는 파라미터의 갯수를 몰라도 된다.
    * 람다 함수 : 파이써닉하게 연산하기 위해 사용하는 익명 함수.
        * 코드의 불필요한 부분을 제거할 수 있다.
        * 무거운 데이터를 순간적으로 사용하고 바로 폐기할 수 있다. (메모리 사용 안함)
        * 고차함수 : 함수의 인자로 전달되거나, 함수의 리턴값으로 사용된다.
    * 맵 함수 : 리스트의 요소를 하나씩 뽑아서 새로운 리스트에 저장하기 위해 사용.
        * map(함수, 리스트)로 인자를 받으며, 리스트에서 엘리먼트를 1개씩 꺼내 함수에 대입하고, 결과값으로 구성된 새로운 리스트를 생성.
    * kwargs(**) : 딕셔너리형 컨테이너 타입의 데이터, 가변 파라미터에 사용.<br><br>

### [Getter & Setter]
* 메서드를 선언할 때 데코레이터로 역할을 구분하는 것이 좋다.
* 게터 세터를 하는 이유는 모델 안에서 한번 설정한 값을 계속 반복해서 쓰기 위함이다.(심지어 파이썬 파일이 바뀌더라도 반복해서 쓸 수 있다.)
* getter : 프로퍼티를 가져오는 메서드, 반드시 리턴이 있다.
    * 데코레이터 '@property'를 사용한다.
* setter : 프로퍼티를 저장하는 메서드, 리턴이 없다.
    * 데코레이터 '@변수.setter'를 사용한다.
* 더블 언더바 메서드(ex. init, str, main)는 내부에 암호화 된 것이다.<br><br>

### [Framework]
* 알고리즘(=솔루션)에 사용되는 구조. 일반인들이 말하는 시스템.
* 파이썬 웹 프레임워크 (Django, Flask, FastAPI)
    * Flask : 마이크로 웹 프레임워크. 단순하고 가볍다. 서버 유지비가 싸다.
    * Django : 빅데이터 전용 웹 프레임워크.
    * FastAPI : 고속 전용 웹 프레임워크.
* Directory : 리소스, 자원들(DB)이 들어있음. 풀었을때 기능이 상실되지 않는다.
* Package : 소스(소스코드), 코드들이 들어있음. 풀었을때 기능이 상실된다.
    * 디렉토리와 패키지 모두 파일을 래핑하는 용도.<br><br>



## `[AI 수학]`
* AI에서 데이터의 입력, 출력, AI모델 구성, 학습 모든 과정이 수학적으로 표현된다.
* 인공지능은 그 자체로 확률모델이며, 학습에는 미분 개념이 포함된 최적화 기법이 사용된다.<br><br>

### [AI에 사용되는 3개의 수학]
* 선형대수학 : 기본 표현. AI 데이터는 주로 숫자 배열(=자료구조)로 표현 하는데, 선대의 벡터나 행렬과 같은 개념이다.
* 통계학 : 구조 설계. 머신러닝은 추론 통계학의 확률 분포 모델이다. 모델의 구조는 확률 분포의 형태이며, 모델의 파라미터는 확률 분포의 세부값이다.
* 미적분 : 성능 향상. 데이터가 가지고 있는 태생적 노이즈를 제거할 수 있으며, 파라미터 변화량 vs 예측값의 변화량 사이의 관계를 계산할 수 있다.<br><br>

### [텐서]
* 인공지능에서 다차원 배열(multil dimensinal array).
* 수학에서는 듀얼 모델에 대하여 곱연산을 사용해 복합적으로 연결시킨 구조. 연산자 중 하나.
* 가우스 : 텐서 개념을 만들었다. 카테시안 좌표계를 무한차원으로 확장했다.
* 벡터는 스칼라를 가로로 늘린 것이고, 매트릭스는 벡터를 세로로 늘린 것이다.
    * (T0 = 스칼라, T1 = 벡터, T2 = 매트릭스, T3 = 큐브, T4 = T4)
    * (2D텐서 = 매트릭스, 3D텐서 = 큐브)
    * 튜플, 딕셔너리, 리스트는 T1이다.
    * T2 입장에서는 T1이 스칼라이다. (상대적인 개념)(특히나 커서는 고차원을 이해할 수 없다.)
* 캐스팅 : 차원의 이동이 일어나는 경우.
    * reduction : 차원축소, 고차원 -> 저차원 변환, (ex.cb[ ][ ][ ] : 큐브에서 스칼라로 내려감)
    * expansion : 차원확장, 저차원 -> 고차원 변환, (ex. cb mtx : T2에서 T4로 올라감)<br><br>

### [차원축소]
* 차원의 저주 : 데이터 수가 너무 많고, 노이즈가 많으면 ‘오버피팅’된다. 인지오류.
* 상관관계가 너무 높으면 알고리즘의 복잡성이 너무 높아져 오히려 안좋다.
* 차원 축소에는 feature 선택, feature 추출 2가지 방법이 있다.<br><br>

### [Convolution]
* 합성곱. 행렬 분해, 변환, 필터링 할 수 있다. (함수 f를 필터 g로 필터링)
* 수학에서는 f * g(t) = 적분f(T)g(t-T)dT로 나타낸다.
* 행렬 계산 예시는 아래와 같다.
* ![이미지 2022  11  7  오후 12 33](https://user-images.githubusercontent.com/112922638/200221427-807701c2-42bd-4149-aa2d-8e17d19f3193.jpg)<br><br>

### [미적분학의 의미]
* Gradient : 기울기, 특정 지점에서 스칼라의 변화율.(=편미분)
    * 물리적 의미 : 
* Divergence : 발산, 단위 부피당 공간 선속의 변화율.
    * 물리적 의미 : 벡터장의 flow(흐름) 근원 or 흡수원인 특정 점에서 얼마나 벡터가 나오는지.
* Curl : 회전, 단위 부피당 회전 성분의 변화율.
    * 물리적 의미 : 벡터장의 vortex(소용돌이) 근원 or 흡수원인 특정 점에서 얼마나 벡터가 회전하는지.
* Laplacian : 기울기의 발산, 그라디언트의 다이버전스.(=2차 편미분)
    * 물리적 의미 : <br><br>



## `[ML]`
* 경험을 통해 자동으로 개선하는 컴퓨터 알고리즘.
    * 알고리즘을 사용하여 데이터에서 패턴을 찾는다.
    * 간단하게 정의하면 머신 랭귀지로 러닝시키는 것.
* 인풋(데이터셋)을 주고, 익명의 함수(람다)를 사용하며, 아웃풋(정답지)를 알려준다.
* 종류 : 회귀(Regression) 분류(Classification) 트리(Tree) 비지도(Unsupervised)
    * 회귀(regression) : 연속성 결과, 시퀀셜 결과 (ex. 고객 별 연체 확률 예측, 상품 판매량 예측)
    * 분류(classification) : 이산성 결과, 카테고리컬 결과 (ex. 이중분류_라쿤인가?, 다중분류_어떤동물?)
* 분야 : 1.CV(이미지 분류, 스캔, 게임), 2.NLP(분류, 요약, 이해, 수익예측, 음성인식, 구매이력)<br><br>

### [기본 개념]
* 라이브러리로 사이킷런을 사용.
* 람다 함수 : 익명 함수, 고차함수, 클로저, 콜백과 같은 개념.
* 클로저 : 환경을 담아놓고, 호출 시 꺼내 사용하는 함수.
* 입력 변수(X) : 샘플 = row 1개 = 확률변수
* 출력 변수(y) : 클래스들 = 답안지 = 타깃 변수 = 종속 변수(dependent variable)
* 예측값(E) : 들어올 데이터에 대한 정확도. (y는 학습시킨 데이터에 대한 정확도.)
    * y = aX + b 에서 y가 출력변수, X가 입력변수
    * 지도학습은 입력변수와 출력변수의 값이 주어진 상태에서 러닝하는 것.
    * 비지도학습은 입력변수만 있는 상태에서 러닝하는 것.
* 모델링 : 시스템적 특성(=변수)을 수식화하는 과정.
    * 시스템의 변화 예측이 방정식으로 표현된다. (미분방정식 or 확률함수)<br><br>

### [클로저]
* 함수의 환경(지역변수 + 코드)을 계속 유지하면서, 호출 당할 경우 환경을 꺼내서 사용하는 함수.
    * 프로그램의 흐름을 변수에 저장할 수 있다.
    * 지역변수와 코드를 묶어서 사용할 수 있다. (=환경)
    * 지역변수를 함수 안에 인캡슐레이션할 수 있다.
* 함수형 프로그래밍의 꽃.
* 람다식과 함께 사용된다. (ex. return lambda x: a*x + b)
* 스코프 : 변수에 접근할 수 있는 범위. 리전같은 의미. (ex. 글로벌 스코프, 로컬 스코프)
* global, local, nonlocal 개념과 클로저의 nonlocal 활용
    * nonlocal은 가장 가까운 바깥 지역 변수를 찾는다.<br><br>



## `[DL]`
* 머신러닝의 한 종류로, 인공신경망을 수많은 계층 형태로 연결한 기법.<br><br>

### [기본 개념]
* 라이브러리로 텐서플로우를 사용.
* 필터 : 뉴런 갯수. 가중치의 집합.
* 커널 : 가중치 1개.
* 윈도우 : 필터의 생김새. (몇x몇) 인지를 나타냄.
* 특성맵 : 원래 행렬을 필터와 합성곱 계산한 결과물.
* 패딩 : 합성곱 계산을 위해 외곽 테두리에 0인 패딩을 채운다.<br><br>



## `[Flask]`
* 마이크로 웹 프레임워크. 단순하고 가볍다. 서버 유지비가 싸다.

### [Path parameter]
* path, string, int, float, uuid 5가지가 있다.
* path : ‘/< >’가 없는 디폴트값
* uuid : 세계 표준 고유 식별자
* ‘/A/< ~ >’를 DB에서 보면 A는 메타데이터 ~는 로우데이터<br><br>

### [RESTful API]
* 안전한 정보 교환을 위한 표준 인터페이스 API.
* Flask에서 methods = [‘’]안에 해당 메서드명을 적는다.
* 메서드 종류 : DELETE, GET, POST, PATCH, PUT
  * CRUD 기준 : GET(=READ), POST(=CREATE), PATCH(=부분 UPDATE), PUT(=전체 UPDATE)
* 해당 프로세스에 맞는 SQL 쿼리를 던져야한다.
  * SQL 기준 : GET(=SELECT), POST(=INSERT)<br><br>



## `[인사이트]`
* 데미스 허사비스 : 알파고의 아버지. 구글 딥마인드의 CEO이다.
* MSA : Micro Service Architecture, 작고 독립적으로 배포가능한 서비스로 구성된 프레임워크이다.
* Kaggle : 예측모델 및 분석 대회 플랫폼.
    * 데이터 사이언티스트들이 경쟁하는 공간으로 기업이 현상금을 걸고 문제를 낸다.
    * 기초적인 머신러닝 모델의 데이터셋을 구할 수 있다. (ex.타이타닉 ML)
* 데이콘 : 확률 알고리즘에서 프로그래머스 같은 사이트.
* 판다스 : 데이터 분석에 필요한 데이터 구조와 연산을 제공하는 라이브러리. 1차원 연산은 넘파이로, 2차원 연산은 판다스로 사용하는 편이다.
* 애자일 방법론 : 신속하게 거지같이 만들어서 깨지고 고친다.
* 오컴의 면도날 : 많은 것들을 필요없이 가정해서는 안된다. 더 적은 수의 논리로 설명이 가능하면 많은 수의 논리를 세우지 말라.
* SOLID : 코드 스멜을 제거하기 위한 원칙.
* 코드 스멜 : 쓰레기 냄새가 날때 사용(중복 코드, 억지 복잡성, 커다란 클래스, 투머치 매개변수,  등)
* OOP와 FP를 잘 섞어서 사용해야 한다. OOP는 정확하며, FP는 빠르다.
* 구글 맵스 플랫폼 API : GCP가 제공하는 구글지도 정보에 대한 API.<br><br>



## `[용어]`
* syntax(신택스) : NL의 grammer
* term(텀) : NL의 word
* 웹(브라우저) <-> 앱(스마트폰)
* component(컴포넌트) : 재사용이 가능한 각각의 독립된 모듈
* server(서버) : 서비스를 제공하는 프로그램
* service(서비스) : 서버가 제공하는 기능, 유저들 입장에서의 메서드 or 모듈
* client(클라이언트) : 서버와 반대되는 말, 고객
* Refactoring : 결과의 변경 없이 코드의 구조를 재조정하는 것.
* 클래스 다이어그램 : 프로그램의 설계 도면.
* API : 뷰(컨트롤러)가 만드는 객체
* NumPy(넘파이) : 기계어로 된 배열으로 선대 계산에 사용되며, 데이터를 빠르게 처리할 수 있다.
* 라이브러리 : 비휘발성 자원(코드, 서브루틴, 클래스, 자료형 등)의 모임.
* 스캐폴드 : 이미 만들어진 양식<br><br>