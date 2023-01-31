# Dart Basic
* reference : youtube code factory
<br><br>

## `[플러터 설치]`
* Flutter SDK 다운
    * 플러터 홈페이지에서 zip파일 받기
    * Users/davidkim에 설치
    * dart —version
* 환경변수
    * vim ~/.zshrc
    * export PATH="$PATH:/Users/davidkim/flutter/bin"
* 닥터 실행
    * flutter doctor
* Xcode
    * 앱스토어에서 다운
    * sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
    * sudo xcodebuild -runFirstLaunch
    * sudo gem install cocoapods
    * flutter doctor
* 안드로이드 스튜디오
    * 홈페이지에서 설치
    * 안드로이드 스튜디오 실행
    * Preferences -> system settings -> Android SDK -> Edit 눌러서 설치
    * Preferences -> Plugins -> flutter 검색, 설치
    * flutter doctor --android-licenses
* 프로젝트 생성
    * New Flutter Project 클릭
    * Flutter SDK 위치 잡아주기
    * 이름 = 작성, 프로젝트 타입 = Application, Organization = kr.scalar, 완료
    * 오른쪽 위 버튼 중에 Device Manager
    * Create virtual device
    * Phone -> pixel2 -> 다음 -> API 33 다운 -> 선택 -> 다음 -> Emulator 띄우기 -> 런
<br><br>



## `[Grammar]`

### [enum]
* 상태를 열거해 묶어서 정의한다.
<br><br>

### [arrow function]
* 간소화 표현.
* => 뒤에 return을 바로 작성한다.
<br><br>

### [typedef]
* 여러 종류의 함수를 담을 수 있다.
* 내부는 arrow function 으로 작성한다.
* 실제 사용 시 파이썬의 람다와 유사하게 사용된다.
<br><br>



## `[OOP]`
* reference : youtube code factory
<br><br>

### [Constructor]
* 클래스 선언 시 매개변수의 자료형과 이름부터 선언.
* this.매개변수를 사용해서 생성자에 직접 작성.
* final
    * 매개변수 선언 시 앞에 final 붙여서 사용.
    * 런타임 도중에 매개변수 수정 불가.
* const
    * 생성자 앞에 const 붙여서 사용.
    * final로 변수를 선언해야만 사용 가능.
    * 빌드 타임에 반드시 값을 알아야 한다.
    * 따로 생성했더라도 매개변수의 구성이 같으면 동일 인스턴스로 취급.
* this는 파이썬의 self와 같은 개념.
* 다트의 특이한 점은 파이썬과 다르게 클래스 내에서 this.을 생략해도 된다.
<br><br>

### [게터와 세터]
* getter
    * void가 아닌 get으로 선언.
    * 입력은 없고 출력만 있다.
* setter
    * void가 아닌 set으로 선언.
    * 반드시 1개의 값만 입력.
    * 출력은 없고 입력만 있다.
<br><br>

### [private]
* 변수나 클래스 앞에 _를 붙여서 사용.
* 다른 파일에서 해당 변수나 클래스를 사용하거나 들여다볼 수 없다.
<br><br>

### [상속]
* 클래스 선언 시 (extends 부모클래스)를 뒤에 이어 작성해 사용.
* 생성자 작성 시 super를 통해 부모의 생성자 호출하여 작성.
* 부모의 매개변수를 건드릴 때에는 this.이 아니라 super. 사용.
* override
    * @override를 메서드 위에 데코레이터 붙여서 사용.
    * 부모의 메서드를 오버라이딩.
<br><br>

### [static]
* 매개변수 선언 시 앞에 static 붙여서 사용.
* static으로 선언한 매개변수는 인스턴스에 귀속되지 않고 클래스에 귀속된다.
<br><br>

### [interface]
* interface 선언 시 별도 키워드가 아닌 class를 사용한다.
    * 추상화가 필요할 경우 abstract를 앞에 작성.
* class 선언 시 (implements 인터페이스)를 뒤에 이어 작성해 사용.
* 다른 클래스를 만들 때 인터페이스에서 선언한 형태를 반드시 지키도록 강제한다.
* 인터페이스에서 선언한 모든 것들을 해당 클래스에서도 선언해야 한다.
<br><br>

### [generic]
* 클래스 선언 시 매개변수의 type도 외부에서 지정하게 만든다.
* 클래스 선언 시 이름 뒤에 <>를 붙여 사용.
<br><br>