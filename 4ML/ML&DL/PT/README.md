# PyTorch

### [Regularization]
* 제약조건을 걸어 오버피팅 방지.
    * 기존 손실함수에 이 규제 텀을 더해준다.
    * 모델은 규제 텀이 커지지 않게 하려고 가중치의 크기를 작게 만든다.
* 옵티마이저 인스턴스 할 때, 'weight_decay=' 파라미터 추가.
* 패널티의 종류에 따라 종류가 나뉜다.
    * L1 : lasso, 가중치의 절대값 합을 패널티로 부과. 모델에 중요하지 않은 특성의 가중치를 0으로 만들어 희소성을 유지.
    * L2 : ridge, 가중치의 제곱 합을 패널티로 부과. 전체적인 특성의 가중치를 작은 값으로 만들어 과적합을 방지.
* 파이토치의 기본 정형화는 L2정형화.
<br><br>

### [Drop out]
* 특정 뉴런의 확률 p를 0으로 바꿔 오버피팅 방지.
* nn.Dropout2d(0.5) 레이어 추가.
* 주로 마지막 fc_layer에서 사용.
<br><br>

### [데이터 증강]
* 이미지를 돌리거나 뒤집어 데이터 수를 늘리는 방법.
* 가우시안 노이즈 이미지 추가, 일래스틱 디포메이션 변형 이미지 추가도 가능.
* transforms.Compose()로 데이터셋 다시 불러오기.
    * transforms.Resize()
    * transforms.CenterCrop()
    * transforms.RandomHorizontalFlip()
    * transforms.Lambda(lambda x: x.rotate(90))
    * 등등 구글링
<br><br>

### [weight Initialization]
* 레이어들의 weight 값을 평균이 0이고 표준편차가 작은 무작위 값으로 설정.
* 기울기 소실 현상 방지, 손실함수 공간을 최적화가 쉬운 형태로 변형.
    * 기울기 소실 : vanishing gradients, back propagation 과정에서 출력층에서 멀어질 수록 gradient 값이 매우 작아지는 현상.
    * 근본적인 원인은 활성화 함수의 미분값의 크기가 작기 때문.
    * 반대인 기울기 폭주 exploding gradients 도 있다.
* 예시 : Xavier Glorot 초기화, Kaiming He 초기화.
* 트랜스포머의 pre-training
    * fine-tuning의 initialization로 간주할 수 있다.
    * 비슷한 작업을 수행하며 weight를 최대한 적절한 곳으로 배치(=초기화) 하는 것.
<br><br>

### [Learning rate 관리]
* 학습률에 따라 모델의 학습이 달라질 수 있다.
* 대표적인 전략은 학습률 부식.
    * 비교적 높은 학습률로 시작해서 점차 학습률을 낮추는 전략.
    * (ex. 0.1 -> 0.0001), (TF 기본 학습률이 0.001)
    * StepLR, ExponentialLR, MultiStepLR 라이브러리 사용.
* ![스크린샷 2023-02-27 오전 11 01 33](https://user-images.githubusercontent.com/112922638/221454931-8c81fa83-50cd-4e44-bdb8-1bcc624201d2.png)
<br><br>

### [입력 데이터 normalization]
* 트레이닝셋 피쳐들의 분포가 일정하도록 정규화.
* 트랜스폼 내에서 transforms.Normalize 사용.
* 사이킷런의 StandardScaler, MinMaxScaler 클래스 사용.
* 예시
    * 트레이닝셋 내에서 분포가 일정하지 않으면 손실함수 계산 시 문제 발생.
    * 트레이닝셋과 테스트셋의 분포가 다르면 예측 불가.
* 각 값에 평균을 빼고 표준편차로 나눈다. -> 평균은 0, 분산은 1인 분포가 된다.
* MinMax 방법을 쓰면 이상치가 있을때 모델이 망가질 수 있다.
<br><br>

### [배치 normalization]
* 트레이닝셋 전체가 아니라 입력되는 배치마다 정규화.
* 모델의 내부에서 층마다 피쳐들의 분포가 달라질 수 있는데, 이걸로 해결.
<br><br>

### [변형 경사하강법]
* SGD 보다 효율적으로 최적화.
* torch.optim.Adam 클래스 사용.
* 종류
    * Adam : 기울기의 평균과 분산을 계산해 변수를 업데이트.
    * AdaGrad : 기존에 기울기가 적게 변한 변수는 크게, 많이 변한 변수는 적게 업데이트.
    * AdaDelta : 지정한 비율로 기울기를 부식시켜 업데이트.
<br><br>

### [모델 정보 불러오기]
* summary(model, input_size=(3, 224, 224))
* dir(model)
* help(model)