# Computer Vision

## `[CV의 주요 개념]`
* 마하밴드, 콘볼루션, 로버츠 연산, 프리윗 연산, 소벨 연산
* 동시 대비 효과, 스무딩, 나이퀴스트 이론
* 샘플링(=표본화) : 해상도에 맞는 픽셀수에 맞게 변환(ex.무한개 -> 1920x1080개)
* 퀀타이제이션 : 샘플링된 각각의 픽셀에 값을 지정함.(ex. 1번 픽셀의 Gray Scale = 48) 
* 로우패스 필터, 바이리터럴 필터, 메디안 필터
* canny 엣지 디텍터 : 5단계(스무딩, 그라디언트, 억제, 트래킹)
* 가우시안 노이즈, 솔트앤페퍼 노이즈
* 적중 비적중 변환(이진 이미지 감지 연산), 세션화, 글로벌 쓰레숄드, 어댑티브 쓰레숄드
* 모폴로지 연산 : 침식, 팽창, 그라디언트, 탑햇, 블랙햇, 열림, 닫힘
* 영상처리 : HOG(Histogram of Oriented Gradiant), blob(영상 이진화 객체), LoG(Laplacian of Gaussian), DoG(Diffrence of Gaussian), SIFT(Scale-Invariant Feature Transform), 동차좌표, k-d 트리, RANSAC(RANdom SAmple Consensus), Feature Matching
* 정형 데이터 : 자료구조 내부에 있는 데이터. 구조화 되어 있다.
* 비정형 데이터 : 자료구조에 구조화되어 있지 않은 데이터.<br><br>



## `[Detector]`

### [Canny Edge Detector]
* 4단계를 진행하여 경계를 찾는다.(스무딩, 그라디언트, 억제, 트래킹)
    * 스무딩 : 노이즈 제거, 가우시안 필터 사용
    * 그라디언트 계산 : 미분해서 인텐시티가 급격하게 변하는 부분 찾기, 소벨 필터 사용
    * non-maximum 억제 : 그라디언트의 로컬 최대값만 남기고, 나머지는 0처리.
    * 엣지 트래킹 : 그라디언트에 최대 최소 바운더리를 부여해서 나머지 날림.
* (ref. flaskProject의 CVbasic 참고)<br><br>

## [Hough Line Detector]
* 3단계를 진행하여 선을 찾는다.(xy평면, ab평면 변환, 쓰레숄드와 비교)
    * 한점을 지나는 '모든' 직선은 y=ax+b 이다.
    * 이를 (a,b)평면으로 이동할 수 있다. 이때 직선 b=-ax+y 로 표현된다.
    * (x,y)평면에서 두 점을 지나는 직선은 (a,b)평면에서 두 직선의 교점이다.
        * 한점 = (a,b) 평면의 직선 1개, 두점 = (a,b) 평면의 직선 2개.
    * (a,b) 평면의 교점들을 하나하나 검사해서 쓰레숄드 이상일 경우 그 직선을 검출할 수 있다.
* (ref. flaskProject의 CVbasic 참고)<br><br>



## `[Classifier]`

### [Haar Casecard Classifier]
* 4단계를 진행하여 얼굴을 인식한다. 하르 피쳐 셀렉션이 사용된다.
    * Haar feature selection
    * 적분 이미지
    * adaboost training
    * casecade classifier
* 특징을 추출하고 얼굴 영역을 판단하는 윈도우(24x24)와 효율적인 비교 알고리즘을 활용.