# NaverCloud(AIaaS)

## `[AI PC Set-up]`
* JDK 11 설치, JDK 11 환경변수 설정
    * 한국의 인공지능은 JDK 11이 표준이다.
* 아나콘다 설치, 아나콘다 환경변수 설정
    * 아나콘다는 데이터 사이언스 기술과 머신러닝의 방법들을 제공한다.
* 파이참 설치, 스튜던트 라이센스 발급<br><br>



## `[Advanced OOP]`

### [Static Method]
* 클래스 밖의 메서드를 클래스 안으로 집어넣을 수 있다.(=랩핑)
* 클래스 밖의 메서드는 스태틱 메서드라고 부른다. (클래스 안은 다이나믹 메서드)
* 화면에 구현할 것을 스태틱 메서드에 넣는다.
* (if문 main) 대신에 @staticmethod를 사용할 수 있다.
* 이때 @를 데코레이터라고 부른다.<br><br>

### [소프트웨어 디자인 패턴]
* 소프트웨어 설계의 특정 문맥에서 공통적인 문제에 대해 재사용 가능한 해결책.
* “바퀴를 다시 발명하지 마라.(Don’t reinvent the wheel.”
* Gang of Four에 의하면, 23가지 패턴으로 모두 설명이 가능하다.
    * 생성 패턴 : 추상 팩토리, 빌더, 팩토리 메서드, 프로토타입, 싱글 턴
    * 구조 패턴 : 어뎁터, 브릿지, 컴포지트, 데코레이터, 파사드, 플라이 웨이트, 프록시
    * 행위 패턴 : 책임 연쇄, 커맨드, 인터프리터, 반복자, 중재자, 메멘토, 옵서버, 상태, 전략, 템플릿 메서드, 비지터<br><br>

### [생성자와 소멸자]
* 생성자(constructor) : init 메서드, 객체 지향에서 객체의 초기화를 담당하는 서브루틴.
* 소멸자(destructor) : del 메서드, 객체가 소멸될 때 자동으로 발생하는 서브루틴.
    * 생성되고 소멸이 안되면 메모리가 부족해진다. 반드시 죽여야한다.<br><br>

### [객체지향의 기본 구조]
* constructor -> static -> information processing -> print
* 객체지향에서 값은 크게 property(포멧), information(처리 완료), data(처리 전) 3가지로 존재한다.
    * constructor = property, information processing = information, static = data<br><br>

### [Getter와 Setter]
* 메서드 이름을 적을때 앞글자에 get 이나 set을 적어주는게 좋다.
* getter : 프로퍼티를 가져오는 메서드, 반드시 리턴이 있다.
* setter : 프로퍼티를 저장하는 메서드, 리턴이 없다.<br><br>

### [Refactoring]
* 결과의 변경 없이 코드의 구조를 재조정하는 것.
* 마틴 파일러의 '리팩터링 패턴'<br><br>

### [데미스 허사비스]
* 알파고의 아버지
* <br><br>



## `[AI Architecture]`

### [CRUD]
* 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능.
* Create, Read, Update, Delete 4가지
    * Read는 2개로 나뉘고, 전체를 보여주는 경우 List(목록). 일부를 보여주는 경우 Search(검색).
* 엔진구조 : 소프트웨어에서 계속 반복해서 돌리다가 원할때 멈추는 구조를 엔진구조라고 한다.
* 스태틱 메인 메서드는 CRUD로 구성된 엔진구조로 설계한다.<br><br>



## `[AI Python]`

### [Pythonic]
* 파이썬 스럽게 코딩하는 것. 파이써닉.
* 파이썬은 아름다운 하나의 답이 존재한다는 철학이 있다.
* 1.comprehesion 2.f-string 3.swap 4.generator 5.extended slice 6.slots(yet) 7.kwards(yet)
    * comprehesion : 축약하기. 숏코딩. (ex. [i for i in ls])
    * 컴프리헨션된 자료는 반드시 자료구조 안에 담아야한다.
    * f-string : 직관적인 문자열. (ex. f”이게 f 스트링{print_fstring}이다.”)
    * swap : 스왑하는 논리. (ex. t = a, a = b, b = t)<br><br>

### [Framework]
* 알고리즘(=솔루션)에 사용되는 구조. 일반인들이 말하는 시스템.
* 파이썬 웹 프레임워크 (Django, Flask, FastAPI)
    * Flask : 마이크로 웹 프레임워크. 단순하고 가볍다. 서버 유지비가 싸다.
    * Django : 빅데이터 전용 웹 프레임워크.
    * FastAPI : 고속 전용 웹 프레임워크.<br><br>



## `[인사이트]`
* <br><br>



## `[용어]`
* syntax : NL의 grammer
* term : NL의 word
* 웹(브라우저) <-> 앱(스마트폰)<br><br>