# Widget
* reference : youtube coding apple
* Lint 끄기
    * analysis_options.yaml의 rules에 4줄 작성
    * prefer_typing_uninitialized_variables : false
    * prefer_const_constructors_in_immutables : false
    * prefer_const_constructors : false
    * avoid_print : false
<br><br>

## [기본 위젯]
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
    * Container() or SizedBox()
* Scaffold()
    * 앱을 상중하로 나눠준다.
    * 상단 = appBar, 중간 = body, 하단 = bottomNavigationBar
* Row(), Column()
    * 여러개의 위젯을 나란히 가로세로 배치 가능.
    * 리스트 형태로 입력.
* 위젯 안에 위젯을 넣을 수 있다.
* 기준설정을 위해 Center() 위젯은 필수 사용.
<br><br>