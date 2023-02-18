# PyTorch

### [Regularization]
* 제약조건을 걸어 오버피팅 방지.
* 옵티마이저 인스턴스 할 때, 'weight_decay=' 파라미터 추가.
* 손실함수의 종류에 따라 종류가 나뉜다. (L1정형화, L2정형화)
    * L1손실 : Mean Absolute Error, 실제값vs 예측값 차이의 절대값 합. 1/n * Σ|y-y_|
    * L2손실 : Mean Squared Error, 실제값vs 예측값 차이의 제곱 합. 1/n * Σ(y-y_)^2
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

### [웨이트 초기화]
* 
<br><br>

### [Learning rate 관리]
* 
<br><br>

### [입력 데이터 normalization]
* 
<br><br>

### [배치 normalization]
* 
<br><br>

### [변형 경사하강법]
* 
<br><br>