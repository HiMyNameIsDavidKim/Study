# CV 
###### 마하밴드
### 연산(Operation)
###### 합성곱(Convolution) 연산자
###### 프리윗 엣지 연산자
###### 소벨 엣지 연산자
### 효과(Effect)
###### 동시대비효과
###### 표본화(Sampling)
###### 양자화(Quantization)
###### 평활화(Smoothing)
###### 나이키스트-새넌의 표본화 정리
### 함수(Function)
###### 점 확산 함수(Point Spread Function)
### 필터(Filter)
###### 저역통과 필터(Low-pass Filter)
###### 쌍방 필터(Bilateral Filter)
###### 중간값 필터(Median Filter)
### 검출기
#### 엣지
###### 마르-힐드레스 엣지 검출기
###### 캐니 엣지 검출기
###### 1. 스무딩(블러): 가우시안 필터를 이용한 노이즈 제거한다
###### 2. 그레디언트: 소벨필터를 이용한 그래디언트의 크기(intensity)를 찾는다
###### 3. Non-maximum suppression을 적용하여 거짓 반응을 제거한다.
###### 4. 경계선으로써 가능성 있는 픽셀을 골라내기 위해 double threshold 방식을 적용한다.
###### 5. 앞서 double threshold 방식에서 maxVal을 넘은 부분을 strong edge, 
######    minVal과 maxVal 사이의 부분을 weak edge로 설정하여 strong edge와 연결되어 있는 weak edge를 edge로 판단하고 그렇지 않는 부분은 제거한다. (Hysteresis thresholding)
### 잡음(Noise)
###### 가우시안 잡음(Gaussian Noise)
###### 점 잡음(Salt-And-Pepper Noise)
### 수학적 형태학
###### 적중-비적중 변환
###### 세션화
### 구조화 요소
###### 침식
###### 팽창
###### 열기
###### 닫기
### 이진화
###### 전역 임계치 결정
###### 적응적 임계치 결정
### 영상처리
###### HoG(Histogram of Oriented Gradient) 서술자
###### blob(Binary Large Object)
###### LoG(Laplacian of Gaussian)
###### DoG(Difference of Gaussians)
###### SIFT(Scale-Invariant Feature Transform)
###### 동차좌표
###### k-d 트리
###### RANSAC(RANdom SAmple Consensus)





