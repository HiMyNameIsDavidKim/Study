# Widget
* reference : youtube coding apple
* Lint 끄기
    * analysis_options.yaml의 rules에 4줄 작성
    * prefer_typing_uninitialized_variables : false
    * prefer_const_constructors_in_immutables : false
    * prefer_const_constructors : false
    * avoid_print : false
* 레이아웃 짜는 순서
    * 디자인 초안
    * 모든 구성 요소를 네모박스로 치기.
    * 겉에 있는 박스를 우선해서 차례차례 만들기.
    * Row, Column, Image 표시.
    * 마무리 디자인 넣기(마진, 패딩, 색상, 정렬 등)
<br><br>

## `[기본 위젯]`
* MaterialApp()
    * 기본 스타일 제공.
    * 구글 스타일
    * 커스터마이징 가능
* Cupertino()
    * 애플 스타일
* 텍스트 위젯
    * Text()
* 이미지 위젯
    * Image.asset('링크')
    * assets 디렉토리 생성
    * pubspec.yaml의 flutter의 assets에 등록
* 아이콘 위젯
    * Icon(Icons.???)
* 박스 위젯
    * Container()
    * SizedBox()가 조금 더 가벼움.
    * Align()으로 감싸서 정렬 가능.
    * 외부 마진 margin 매개변수 설정.
    * 내부 패딩 padding 매개변수 설정.
* Scaffold()
    * 앱을 상중하로 나눠준다.
    * 상단 = appBar, 중간 = body, 하단 = bottomNavigationBar
* Row(), Column()
    * 여러개의 위젯을 나란히 가로세로 배치 가능.
    * 리스트 형태로 입력.
* ListView()
    * 스크롤이 필요할 정도로 길어지면 사용 추천.
    * 유저의 스크롤 위치 감시 가능.
    * 비동기식 위젯이라 메모리 절약 가능.
* 버튼 위젯
    * TextButton()
    * IconButton()
    * ElevatedButton()
    * child 매개변수에 내용 입력.
    * onPressed에 함수 작성.
* 위젯 안에 위젯을 넣을 수 있다.
* 기준설정을 위해 Center() 위젯은 필수 사용.
<br><br>

### [AppBar]
* scaffold() 위젯 사용 시 가장 상단 바.
* title 매개변수 : 제목
* leading 매개변수 : 좌측 위 아이콘 구현.
* action 매개변수 : 우측 위 아이콘 구현.
<br><br>

### [Flexible]
* 화면의 x%만큼 차지하도록 표현하고 싶을때 사용.
* flex의 비율대로 맞춰 x:x:x 비율 형성.
* Flexible()이 귀찮으면 Expanded()로 대체 가능. (flex=1)
<br><br>

### [이미지 추가]
* 프로젝트 파일에 images 폴더 추가
* pubspec.yaml 파일
    * flutter: 아래에 작성
    * (2칸)assets:
    * (4칸) - images/
* 패딩으로 감싸서 여백 주는 것을 추천.
<br><br>

## `[커스텀 위젯]`
* 클래스에 담기.
    * 메인앱 아래에 새 클래스 작성 (stless + Tab키)
    * 이름설정, return 이후에 출력값 작성.
* 변수나 함수에 담을 경우 에러주의.
* Drawer : 앱바 좌측에 항상 있는 것으로, 주로 메뉴를 탑재.
* Splash Screen : 대기화면. 화면 이동할 때 잠깐 보여주는 화면.
<br><br>

