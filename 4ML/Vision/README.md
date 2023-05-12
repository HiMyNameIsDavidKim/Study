# Computer Vision

## `[Details & Examples]`
* [`Patch-based transformation 구현`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/patch_trans.py)
* [`ViT GAP 버전 구현`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/vit_GAP.py)
* [`ViT 논문 구현`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/vit_paper.py)
* [`UNet 논문 구현`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/unet_paper.py)
* [`ResNet 논문 구현`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/resnet_paper.py)
* [`VGGNet 논문 구현`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/vggnet_paper.py)
* [`디노이징 오토 인코더_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/auto_encoder.py)
* [`MNIST GAN_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/mnist_gan.py)
* [`셀럽 얼굴 딥페이크 합성 GAN_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/celeba.py)
* [`고흐 사진 합성 Style Transfer_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/style_transfer.py)
* [`패션 MNIST DNN_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/fashion_torch.py)
* [`숫자 MNIST CNN_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/number_torch.py)
* [`숫자 MNIST DNN_TF`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/number.py)
* [`패션 MNIST DNN_TF`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/fashion.py)
* [`사과 분류 CNN_TF`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/fruit.py)
* [`엣지, 직선, 얼굴 검출`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/CV/lenna.py)
<br><br>



## `[CNN]`
* (NxN, 32) : NxN 커널 사이즈의 필터가 32개 있다.
    * 필터 사이즈라고는 안하고 커널 사이즈라고 한다.
    * 필터 : 합성곱할 NxN크기 행렬 1개. 가중치의 집합 1개.
    * 파라미터 : 필터 속에 가중치 1개. (ex. 3x3 = 9개 파라미터)
    * 커널 : 파라미터와 동의어.
* Tensor size 계산
    * O = (I - K + 2P)/S + 1
    * (1 더하기 전에 소수점 발생 시 버림!!)
    * O : output 크기(너비)
    * I : input 크기(너비)
    * K : kernel 크기(너비)
    * P : padding 크기
    * S : stride
* 파라미터 수 계산
    * P = (커널사이즈 x 채널 x 필터 수) + 바이어스 수
    * P = (K^2 x C x N) + N
    * P : 파라미터 수
    * K : kernel 크기(너비)
    * C : 채널 개수
    * N : 필터 개수
* FLOPs 계산
    * FLOPs = (2i - 1) * o
    * i : 인풋 레이어의 필터 수
    * o : 아웃풋 레이어의 필터 수
<br><br>

### [CNN 아키텍쳐 구현]
* 1000줄 언더 코딩.
* CPU, GPU 도합 500만원 정도 장비.
* 일주일 정도 학습 예상.
<br><br>

### [inductive bias]
* 새로운 데이터에도 적용될 수 있는 일반적인 규칙을 학습하는 편향.
* 선형 회귀 모델 : 입력 특성과 출력 사이의 선형 관계를 가정하는 inductive bias.
* CNN : CV inductive bias가 높다.
* RNN : NLP inductive bias가 높다.
* 딥러닝에서 inductive bias는 아키텍처, 활성화 함수, 손실 함수 등에 내재된다.
<br><br>

### [many supervised]
* self-supervised
    * 레이블이 없는 데이터를 사용하여 모델을 학습.
    * 모델이 스스로 데이터에서 의미있는 패턴을 추출.
    * 이미지 특징 추출 능력을 향상.
* semi-supervised
    * 레이블이 있는 데이터와 없는 데이터를 함께 사용하여 모델을 학습.
    * unsupervised와 self-supervised의 중간.
<br><br>

### [Convolution Operation]
* input의 채널 수 = 필터의 채널 수
* 필터의 개수 = output의 채널 수
<br><br>



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
* 비정형 데이터 : 자료구조에 구조화되어 있지 않은 데이터.
<br><br>

### [Classic CV Algorithm]
* 엣지 검출 : Canny, Laplacian of Gaussian
* 피쳐 추출 : SIFT, SURF, ORB, BRISK
* 객체 검출 : HOG, Haar Cascades
* 이미지 분할 : Watershed, Mean Shift, GrabCut
* 노이즈 제거 : Gaussian Blur, Median Filter
<br><br>



## `[Detector]`

### [Canny Edge Detector]
* 4단계를 진행하여 경계를 찾는다.(스무딩, 그라디언트, 억제, 트래킹)
    * 스무딩 : 노이즈 제거, 가우시안 필터 사용
    * 그라디언트 계산 : 미분해서 인텐시티가 급격하게 변하는 부분 찾기, 소벨 필터 사용
    * non-maximum 억제 : 그라디언트의 로컬 최대값만 남기고, 나머지는 0처리.
    * 엣지 트래킹 : 그라디언트에 최대 최소 바운더리를 부여해서 나머지 날림.
* (ref. flaskProject의 CVbasic 참고)
<br><br>

## [Hough Line Detector]
* 3단계를 진행하여 선을 찾는다.(xy평면, ab평면 변환, 쓰레숄드와 비교)
    * 한점을 지나는 '모든' 직선은 y=ax+b 이다.
    * 이를 (a,b)평면으로 이동할 수 있다. 이때 직선 b=-ax+y 로 표현된다.
    * (x,y)평면에서 두 점을 지나는 직선은 (a,b)평면에서 두 직선의 교점이다.
        * 한점 = (a,b) 평면의 직선 1개, 두점 = (a,b) 평면의 직선 2개.
    * (a,b) 평면의 교점들을 하나하나 검사해서 쓰레숄드 이상일 경우 그 직선을 검출할 수 있다.
* (ref. flaskProject의 CVbasic 참고)
<br><br>



## `[Classifier]`

### [Haar Casecard Classifier]
* 4단계를 진행하여 얼굴을 인식한다. 하르 피쳐 셀렉션이 사용된다.
    * Haar feature selection
    * 적분 이미지
    * adaboost training
    * casecade classifier
* 특징을 추출하고 얼굴 영역을 판단하는 윈도우(24x24)와 효율적인 비교 알고리즘을 활용.
<br><br>



## `[GPU 가속 설정]`
* 파이토치와 텐서플로우 사용하기 위해서는 GPU 가속이 필수적이다.
    * NVIDIA는 GPU, 애플 실리콘은 MPS.
<br><br>

### [CUDA]
* NVIDIA가 만든 병렬 컴퓨팅 API 모델
* CUDA 설정 (윈도우 : https://parksrazor.tistory.com/786)
<br><br>

### [MPS]
* Metal Performance Shaders, 딥러닝 시 GPU 가속에 사용된다.
* 설치
    * conda install pytorch torchvision torchaudio -c pytorch-nightly
* 가상환경
    * conda create -n gpu --clone base
    * conda activate gpu
    * pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
* 가속여부 확인
    * import torch
    * print(torch.__version__)
    * print(torch.backends.mps.is_available()) # True
    * print(torch.backends.mps.is_built()) # True
* MPS 적용법
    * device = torch.device('mps') # device = torch.device("cpu")
* 추가 라이브러리
    * conda install -c apple tensorflow-deps
    * pip install tensorflow-macos
    * pip install tensorflow-metal
    * pip install transformers
    * pip install sentencepiece
    * pip install torchsummary
    * conda install icecream
    * pip install mysql-connector-python
    * pip install flask
    * pip install konlpy
    * pip install pandas
    * pip install numpy
    * pip install scikit-learn
    * pip install jupyter
    * pip install opencv-contrib-python
    * pip install mxnet
    * pip install gluonnlp
    * pip install pytorch_lightning
    * pip install --upgrade scipy
* GPU 사용여부 확인
    * import torch
    * import tensorflow as tf
    * import sklearn
    * device = torch.device('mps')
    * print('Torch device:', device)
    * print("TF GPUs Available: ", tf.config.experimental.list_physical_devices('GPU')
    * print('scikit-learn version : ', sklearn.__version__)
<br><br>



## `[Trouble Shooting]`

### [파이토치 M1 Error]
* DataLoader의 num_workers에 오류가 있음. 0으로 둬야함.
<br><br>



