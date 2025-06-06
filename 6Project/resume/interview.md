# 면접
* 자신감과 진정성
<br><br>

## 🧐 사용 방법
* 질문에 대한 답변을 패드에 손으로 쓰며 외운다.
* 마크다운의 목차(Outline)를 클릭하여 펼친다.
* 질문만 보고 답변을 연습한다.
<br><br>



## 📋 Contents
### 딥러닝
### 머신러닝
### 통계학
### 데이터분석
### 알고리즘
### 자료구조
### 컴퓨터과학
### 필수
### 회사관심도
### 직무경험
### 프로젝트
### 압박
### 소프트스킬
<br><br>



## `[기술 면접]`
* 간결하고 쉽게 설명
<br><br>

### [딥러닝]
#### 딥러닝이란 무엇인가
* 머신러닝의 한 종류로 인공신경망을 기반으로 데이터에서 패턴을 학습하여 새로운 데이터에 대한 예측을 하는 알고리즘 입니다.
#### 딥러닝과 머신러닝의 차이를 설명하라
* 딥러닝은 모델이 특징 추출, 학습을 자동으로 수행합니다.
* 머신러닝은 사람이 특징을 설계하고 모델은 학습만 합니다.
#### 오버피팅과 언더피팅의 차이점
* 오버피팅은 학습 데이터를 외우는 것처럼 과하게 학습하여 일반화 성능이 낮습니다. 기술적으로 설명하면 특정 뉴런에 대한 의존도가 매우 높은 상태 입니다.
* 언더피팅은 아직 학습 데이터의 패턴을 제대로 학습하지 못한 상태입니다.
#### FC layer와 CNN layer의 차이점을 설명하라
* FC layer는 모든 뉴런이 연결되어 있고 입력 데이터를 고차원 공간에서 다른 차원으로 변환합니다.
* CNN layer는 필터를 사용해서 주변 데이터와의 관계와 지역적 패턴을 추출합니다.
#### 비선형이란 무엇이고 왜 필요한가
* 비선형은 직선 즉 선형 함수로 설명할 수 없는 복잡한 관계를 뜻합니다.
* 어려운 문제들은 비선형성을 추가해 복잡한 패턴을 학습해야 해결할 수 있습니다.
#### sigmoid 대신 relu를 사용하는 이유를 설명하라
* sigmoid는 S자 형태로 음수에서 0에 가까워지고 양수에서 1에 가까워집니다.
* relu는 음수에서 0이고 양수에서 입력값 그대로를 출력합니다.
* sigmoid는 상대적으로 gradient vanishing 문제에 더 취약합니다. relu의 경우 출력 값의 상단 제한이 없지만 sigmoid의 경우 출력값이 0과 1 사이로 제한되기 때문에 기울기가 매우 작아지는 gradient vanishing 문제를 초래합니다.
#### relu가 곡선 함수를 근사하는 방법을 설명하라
* relu는 여러 뉴런의 활성화 상태를 조합해 복잡한 비선형 함수를 근사할 수 있습니다. 각 뉴런의 활성화 여부를 on/off하면 곡선 함수를 근사할 수 있습니다.
#### gradient vanishing의 근본적인 원인을 설명하라
* 활성화 함수의 영향, 체인룰의 영향 두가지가 있습니다. 시그모이드의 경우 활성화 함수의 기울기가 0에 가까워져 결국 가중치를 업데이트하지 못합니다. 이를 방지하기 위해 relu를 사용하더라도 기울기가 0인 구간이 여전히 존재하기 때문에 chain rule에 의해 역전파 과정에서 낮은 층까지 도달하면 기울기가 0에 급격하게 가까워져 업데이트가 되지 않는 문제가 있습니다.
#### gradient descent의 개념을 설명하라
* 손실함수를 최소화하기 위해 가중치를 반복 업데이트하는 최적화 알고리즘입니다.
* 손실함수가 가장 작은 지점이 최적값 즉 해인데, n차 함수 형태인 손실함수의 최솟값을 구하는 방법은 미분해서 0인 지점으로 다가가는 것입니다. 여기서 미분이 gradient, 0으로 다가가는 것이 descent 입니다.
#### 경사하강법 그래프의 x축과 y축의 의미를 설명하라
* x축은 모델의 가중치, y축은 loss value를 뜻합니다.
#### GD 중에 때때로 loss가 증가하는 이유를 설명하라
* 첫번째로 learning rate가 너무 크면 한번의 업데이트에서 minima를 지나칠 수 있습니다. 두번째로 미니 배치 간의 분포 차이로 인한 변동성이 있을 수 있습니다. 세번째로 loss function의 landscape가 복잡해 local minima를 탈출할 때 발생할 수 있습니다.
#### GD와 SGD의 차이를 설명하라
* GD는 전체 데이터셋을 모두 사용하여 느리지만 안정적으로 학습합니다.
* SGD는 데이터셋의 일부를 사용하여 빠르게 학습하지만 불안정할 수 있습니다.
#### RMSprop과 Adam에 대하여 설명하라
* RMSprop은 기울기의 제곱에 대한 지수이동평균을 이용해 학습률을 동적으로 조절하는 방법입니다. 기울기가 큰 파라미터의 학습률을 줄여 더 안정적으로 학습을 진행합니다.
* Adam은 여기에 모멘텀을 추가하여 더 빠르고 효율적으로 학습하는 방법입니다.
#### 모멘텀을 수식으로 설명하라
* 물리학적 관점의 관성을 알고리즘화한 것입니다. 기존 가중치에 속도인 모멘텀을 더해줍니다. 이번 단계의 속도는 이전 단계의 속도와 이번 단계의 기울기를 조합해 계산합니다.
#### backpropagation에 대하여 설명하라
* 입력에서 출력 방향인 순방향을 계산해 예측값을 구하고 loss를 구합니다.
* loss를 출력에서 입력 방향으로 전파하며 가중치를 얼마나 바꿔야 오차가 줄어드는지 계산합니다. 이것은 chain rule에 의해 각 가중치에 대한 그라디언트를 계산하면 얻을 수 있습니다. (그라디언트 = 현재 가중치가 얼마나 잘못되었는지에 대한 벡터)
* 계산된 가중치를 학습률과 곱해 모든 가중치를 업데이트 합니다.
* (손 계산)
    * 순전파: 출력 계산과 활성화 함수 대입 반복 후 최종 예측값 도출
        * sum(입력값 * 웨이트) = 출력값
        * 출력값을 활성화 함수에 넣고 계산 (x에 대입 y 도출)
    * 손실값: 예측값과 실제값을 MSE 공식에 넣고 loss 계산
        * 1/n (sum(손실 - 예측)^2)
    * 역전파: loss의 그라디언트를 러닝 레이트와 곱해 빼서 업데이트
        * (새 웨이트) = (기존 웨이트) - (그라디언트 loss) * (러닝 레이트)
        * (그라디언트 loss) ∇C = dC/dw (loss의 웨이트 편미분)
        * dC/dw (loss의 웨이트 편미분) = dC/dO * dO/dz * dz/dw (체인 룰)
        * 체인 룰: 두 변수의 미분 관계를 모를 때 각각 아는 미분값으로 연쇄적으로 연결해서 해결
        * dC/dO (loss의 아웃풋 편미분) * dO/dz (아웃풋의 활성화 함수 z노드 아웃풋 편미분) * dz/dw (z노드 아웃풋의 웨이트 편미분)
#### local minima로 인해 딥러닝이 안되는 매커니즘을 설명하라
* 모델이 local minima에 빠지면 더 나은 global minima에 도달하지 못하고 성능 개선이 멈춰버립니다.
#### saddle point 문제에 대하여 설명하라
* 차원 공간에서 한 방향에서는 최소값을 가지지만 다른 방향에서는 최대값을 가지는 지점을 말합니다. 한 방향에서 미분이 0이 나오고 다른 방향을 줄이려다가 원래 방향의 값이 증가할 수 있는 문제로, 더이상 학습을 진행하지 않을 수 있습니다.
* 초기 값을 다양하게 설정하거나 모멘텀 기법을 사용하여 해결할 수 있습니다.
#### 찾은 해가 global minima인지 판단하는 방법은 무엇인가
* loss function landscape를 시각화하거나 다양한 초기값으로 학습해서 최소값에 변화가 있는지 비교해봅니다.
#### 지도학습과 비지도학습의 objective funtion과 차이를 설명하라
* 지도학습은 실제값과 예측값의 loss를 계산하고 최소화하는 방법을 사용합니다. (ex. MSE, CE)
* 비지도학습은 데이터의 구조를 파악하고 군집이나 밀도를 목표로 합니다. (ex. 클러스터링, PCA)
#### 과적합 방지를 위해 사용하는 방법을 모두 설명하라
* dropout, regularization, batch norm, 데이터 증강 기법, early stopping 등이 있습니다.
#### dropout의 개념과 사용하는 이유를 설명하라
* 드롭아웃은 학습 시 무작위로 무작위로 뉴런을 비활성화하여 특정 뉴런에 의존하지 않도록 합니다.
* 과적합을 방지하고 모델의 일반화 성능을 높일 수 있습니다.
#### 정규화(regularization)에 대하여 설명하라
* 과적합 방지를 위한 제약조건으로 L1, L2 등이 있습니다. 이 값을 실제 손실함수에 패널티로 더해주면 모델은 가중치의 크기를 줄이는 방향으로 학습합니다.
* L1은 lasso로 가중치의 절대값 합을 패널티로 부과합니다. 모델에 중요하지 않은 특성의 가중치를 0으로 만들어 희소성을 유지합니다.
* L2은 ridge로 가중치의 제곱 합을 패널티로 부과합니다. 전체적인 특성의 가중치를 작은 값으로 만들어 과적합을 방지합니다.
#### 정규화(norm)와 표준화(stand)의 차이점을 설명하라
* 정규화(normalization)는 데이터를 0에서 1 범위로 변환하는 것이고 표준화(standardization)는 평균은 0 분산은 1이 되도록 변환하는 것입니다.
#### 정규화(norm)을 하는 이유를 설명하라
* 학습 중에 특성 간의 크기 차이를 제거하고 특정 뉴런의 의존도가 너무 높지 않도록 하여 학습을 안정화 시킵니다.
#### batch normalization의 개념과 사용하는 이유를 설명하라
* 배치 노멀라이제이션은 각 미니배치 입력의 평균과 분산을 0과 1로 조절합니다. 따라서 초기값에 의해 특정 미니배치가 과하게 학습되는 과적합 현상을 방지해줍니다.
#### batch norm과 layer norm의 차이를 설명하라
* 입력 텐서의 (batch, 이미지 토큰 수, dim)이 (64, 196, 768)인 예시로 설명하겠습니다.
* batch norm은 같은 토큰 같은 dim에서 batch를 기준으로 값을 정규화하는 것입니다. 입력 값의 분포가 학습 중에 변하는 것을 방지합니다. 하지만 배치에 의존적이기 때문에 작은 배치에서는 효과가 불안정할 수 있습니다.
* layer norm은 같은 토큰 같은 batch에서 dim을 기준으로 값을 정규화하는 것입니다. 같은 샘플 내의 뉴런의 의존도 편향을 방지합니다. 따라서 배치에 독립적이고 작은 배치에서도 안정적으로 동작합니다.
#### softmax 함수에 대하여 설명하라
* 여러 클래스의 점수를 확률로 변환하는 함수 입니다. 모든 출력값의 합이 1이 되도록 normalization 해줍니다.
#### softmax 함수의 수식을 설명하라
* 여러 개의 실수값을 입력받아 0에서 1 사이의 확률값으로 변환하는 함수 입니다. 각 입력값에 지수함수를 적용하고 (해당 지수값) / (모든 지수값의 합)으로 나타낼 수 있습니다.
#### 분포가 불균형한 데이터를 분류 할 때 발생하는 문제는 무엇인가
* 구성 비율이 낮은 클래스가 무시되어 모델이 편향되고 성능이 떨어집니다.
* 오버샘플링이나 언더샘플링을 사용하면 문제를 해결할 수 있습니다.
#### cost function과 activation function을 설명하라
* cost function은 loss function으로 실제값과 예측값의 차이를 계산합니다. (ex. MSE, CE)
* activation function은 뉴런의 출력을 결정하고 모델에 비선형성을 부여합니다. (ex. relu, softmax)
#### 파이토치와 텐서플로우의 특징과 차이를 설명하라
* 파이토치는 더 파이써닉한 코드라 가독성이 좋습니다. 또한 실행 중에 텐서를 이용해 동적으로 그래프를 그릴 수 있어 디버깅이 편합니다.
* 텐서플로우는 배포의 용이성과 텐서보드 시각화에 강점이 있습니다. 또한 미리 그래프를 선언해 정적인 그래프를 그릴 수 있어 속도가 빠릅니다.
#### 하이퍼 파라미터는 무엇인지 설명하라
* 학습 전에 사람이 직접 설정하는 파라미터로 모델의 성능에 큰 영향을 미칩니다.
* learning rate, batch size, epoch, dim, block 수 등이 있습니다.
#### weight initialization 개념과 종류를 설명하라
* 가중치의 초기값을 설정하는 방법으로 ±0.1 사이의 균일한 분포 값을 넣는 랜덤, 입출력 뉴런 수를 고려한 xavier 방법 등이 있습니다.
#### training set과 test set을 분리하는 이유를 설명하라
* 모델의 일반화 성능을 객관적으로 평가하기 위해서 입니다. 과적합된 경우 학습에 사용한 데이터는 모델이 이미 외우고 있을 수 있습니다.
#### validation set이 필요한 이유를 설명하라
* 하이퍼 파라미터 튜닝이나 학습 중간에 경과를 평가하기 위해서 사용합니다.
#### GPU를 사용하는 이유를 설명하라
* 병렬 연산이 가능해서 CPU보다 더 빠른 속도로 학습할 수 있습니다. 딥러닝은 행렬 연산을 많이 사용하기 때문에 GPU를 사용합니다.
#### GPU를 두개 사용하는 방법을 설명하라
* 배치를 나눠서 각 GPU에서 병렬로 데이터를 처리할 수 있습니다. 파이토치에서 분산학습 메서드인 DistributedDataParallel를 사용하면 됩니다.
#### 학습에 필요한 GPU 메모리를 계산하는 방법을 설명하라
* 배치크기 * 파라미터수 * 4(float32)로 계산할 수 있고 모델 (인스턴스, 그라디언트, 옵티마이저)를 고려해 4배 정도 됩니다.
#### 트랜스포머의 전체적인 구조를 설명하라
* 인코더-디코더 구조로 되어 있고 어텐션 레이어를 사용합니다. 인코더에는 셀프어텐션, 디코더에는 masked 셀프어텐션, 인코더-디코더 어텐션 구조로 되어 있습니다.
* 인코더와 디코더의 마지막에는 Feed Forwad Network가 있고 어텐션 레이어와 FFN 뒤에는 residual connection과 norm을 진행합니다.
* 입력이 들어오면 이를 임베딩으로 만들고 포지션 임베딩을 더해줍니다. 그리고 인코더-디코더 구조를 거친 뒤 최종 임베딩을 linear layer와 softmax를 거쳐 최종 결과를 냅니다.
#### 트랜스포머가 위치정보를 전달하는 방법을 설명하라
* 포지션 임베딩을 사용하여 위치 정보를 전달합니다. sin, cos 함수를 기반으로 인코딩하며 순차성은 있지만 의미 정보가 변질되지 않도록 ±1사이의 값입니다. 주기성을 이용하여 각 위치마다 고유한 패턴을 만들어냅니다.
#### 어텐션 매커니즘의 과정을 수식으로 설명하라
* 입력 임베딩에 Q, K, V 매트릭스를 내적해 Q, K, V 벡터를 먼저 얻을 수 있습니다.
* 현재 단어의 Q와 모든 단어의 K의 전치행렬을 각각 내적하여 각각의 어텐션 스코어를 구하고 이를 softmax 함수에 넣어 각각의 어텐션 웨이트를 구합니다.
* 각각의 어텐션 웨이트를 각각의 V와 곱한뒤 모두 더해 컨텍스트 벡터를 구할 수 있습니다.
* 이 컨텍스트 벡터는 QKV 벡터와 같은 사이즈의 행렬이며 다음 시점의 모델에 입력입니다.
#### 어텐션 매커니즘의 Q, K, V 벡터의 정성적인 의미를 설명하라.
* Q는 현재 단어가 필요로 하는 정보에 대한 representation 입니다. 그리고 K와 V는 입력 시퀀스의 각 단어에 대한 특징으로 보통 같은 값을 사용하지만 용도가 다릅니다. K는 어텐션 스코어 계산에 사용되며 V는 컨텍스트 벡터 계산에 사용됩니다.
* 어텐션 스코어는 현재 단어의 Q와 각 단어 K의 유사도를 의미하며 어텐션 웨이트는 현재 단어에 대한 각 단어의 중요도를 의미합니다.
* 컨텍스트 벡터는 현재 시점에서 각 단어 간의 중요도에 대한 요약을 의미합니다.
#### 인코더 셀프 어텐션과 디코더 셀프 어텐션의 차이를 설명하라
* 인코더 셀프 어텐션은 모든 단어를 사용할 수 있지만 디코더 셀프 어텐션은 마스킹 때문에 현재 위치 까지의 단어만 사용할 수 있습니다. 또한 인코더-디코더 어텐션의 경우 인코더 셀프 어텐션의 결과를 Q로 디코더 셀프 어텐션의 결과를 K, V로 사용합니다.
#### BERT와 GPT의 차이점을 설명하라
* BERT는 양방향 인코더 기반으로 입력 시퀀스의 모든 토큰을 사용할 수 있고 Masked Language Model 과 Next Sentence Prediction으로 학습합니다. 반면에 GPT는 단방향 디코더 기반으로 현재 위치 까지의 단어만 사용할 수 있고 다음 단어를 예측하는 task로 학습합니다. BERT는 문장을 이해하거나 분류하는데 강점을 보이고 GPT는 텍스트 생성에 강점을 보입니다.
#### 랭체인에 대하여 설명하라
* 랭체인은 LLM을 쉽고 효율적으로 사용할 수 있게 도와주는 프레임워크 입니다. GPT, 클로드 처럼 회사가 다른 여러 AI 모델을 API를 사용해 같이 사용할 수도 있고, 외부 데이터를 LLM에 쉽게 연결할 수도 있습니다.
#### RAG에 대하여 설명하라
* RAG는 Retrieval Augmented Generation으로 LLM이 답변할 때 외부 데이터베이스에서 관련 정보를 찾아와서 참고하면서 대답하는 방식입니다. 예를 들어, 회사 내부 문서를 참고해서 답변하는 것입니다. 최신 정보를 사용할 수 있는 장점과 출처가 있기 때문에 할루시네이션이 적은 장점이 있습니다.
* 문제점은 우리가 사용하는 PDF, 워드, 엑셀 같은 문서들이 출판용 구조이거나 테이블로 되어 있어 파싱 문제로 잘 작동하지 않습니다.
* 해결하기 위해 전처리와 텍스트 추출을 하는 것이 필요합니다.
#### ToD에 대하여 설명하라
* ToD는 Task-oriented Dialogue로 특정 목적을 달성하기 위한 대화 시스템입니다. 예를 들어, 식당 예약 같은 구체적인 작업을 완료하기 위한 대화 태스크 입니다. NLU, DST, DP, NLG 4가지 모듈로 구성되어 있습니다.
#### CNN의 연산과정을 설명하라
* 입력 이미지에 필터를 슬라이딩하며 컨볼루션 연산을 수행합니다. 이때 필터와 이미지의 각 부분을 곱하고 더하면서 특징을 추출합니다. 또한 활성화함수로 비선형성을 추가하고 풀링 레이어로 피쳐맵의 크기를 줄입니다.
#### ResNet의 핵심 개념을 설명하라
* residual connection을 통해 더 깊은 층으로 구성된 모델도 학습이 가능합니다. 이전 블럭의 결과를 이번 블럭의 결과에 더해주는 구조로 gradiant vanishing 문제를 해결하고 깊은 층의 레이어도 학습할 수 있습니다.
#### MobileNet의 핵심 개념을 설명하라
* 기존 컨볼루션을 depth-wise, point-wise conv로 대체했습니다. 연산을 두단계로 나눠서 하면 연산량이 크게 줄어드는데 이 트릭을 사용한 것입니다. depth-wise conv는 채널 간의 정보는 혼합되지 않고 공간적 특징만 추출하며 3x3 커널을 사용합니다. point-wise conv는 공간적 정보는 건드리지 않고 채널의 정보만 혼합해 특징을 추출하며 1x1 커널을 사용합니다.
#### EfficientNet의 핵심 개념을 설명하라
* 네트워크의 depth, width, resolution을 균형있게 키우는 것입니다. compound scaling이라고 해서 작은 베이스 모델을 만들고 세가지 요소를 동시에 키워나갑니다.
#### CNN과 ViT의 차이를 설명하라
* 두 모델 모두 특징 추출을 하는 모델이지만 추출 매커니즘에 차이가 있습니다. CNN은 로컬 픽셀들 간의 관계에서 패턴을 찾고 ViT는 이미지 패치들 간의 관계에서 패턴을 찾습니다. CNN은 부분적 특징을 추출하는데 강점을 보이고 ViT는 전역적 관계를 추출하는데 강점을 보입니다.
#### CNN과 ViT에서 XAI 방법론을 설명하라
* CNN은 주로 Grad-CAM, Class Activation Map을 사용해 이미지의 어디 부분을 보고 판단했는지 시각화 합니다. ViT는 어텐션 맵을 통해 각 패치가 다른 패치와 얼마나 상호작용을 하는지 봅니다.
#### CNN에 비해 ViT의 학습 속도가 느린 이유를 설명하라
* CNN은 커널을 사용하고 픽셀 사이에 관계가 있다는 가정을 아키텍처에 내포하여 학습합니다. 반면 ViT는 이런 가정이 없고 패치 사이의 관계에서 특징을 추출합니다. 따라서 가정 없이 학습하는 ViT는 모든 관계를 새로 학습해야하기 때문에 학습 속도가 느립니다.
* 계산 복잡도 측면에서도 셀프 어텐션 연산은 시퀀스 길이의 제곱에 비례하고 컨볼루션 연산은 커널 크기와 이미지 크기에 비례합니다.
#### ViT가 프리트레이닝이 필요한 이유를 트랜스포머와 연결하여 설명하라
* CNN는 주변 픽셀과 관계가 있다는 가정이 있지만 ViT는 이런 가정이 없기 때문입니다. 트랜스포머 구조는 원래 NLP 태스크를 위해 만들어졌습니다. 텍스트는 단어 단위로 나뉘어지는데 이미지에서도 인위적으로 패치 단위로 나누게 됩니다. 이 과정에서 CNN과 같은 가정이 사라지고 모든 관계를 새로 학습하기 때문에 프리트레이닝이 필요합니다.
* 대규모 데이터셋으로 프리트레이닝을 하면 이미지의 일반적인 특성을 학습할 수 있습니다. 이 일반적인 특징이 세부 태스크나 작은 데이터셋에서 좋은 성능을 낼 수 있게 합니다.
#### inductive bias에 대하여 설명하라
* 학습하는 과정에서 생긴 사전 가정으로 인간의 선입견과 유사합니다. 학습 데이터나 아키텍처에 의해 발생합니다.
* CNN의 경우에는 근처 픽셀 간에 관계에 대한 인덕티브 바이어스가 생기고, ViT의 경우 상대적으로 인덕티브 바이어스가 없지만 패치 단위로 이미지를 나누는 것에 대한 인덕티브 바이어스가 있습니다.
#### 딥러닝 이전에 detection에 사용했던 방법을 설명하라
* 이미지의 경계와 방향을 분석하는 HOG와 이미지의 밝기 차이를 특정하여 눈코입의 패턴을 감지하는 Haar와 같은 방법이 있습니다.
#### Faster R-CNN의 모델에 대하여 설명하라
* Faster R-CNN은 2 stage 디텍션 모델입니다. Fast R-CNN에 select search 대신 RPN을 사용해 속도를 개선한 모델입니다. RPN이 객체가 있을 만한 영역을 먼저 찾은 후 Fast R-CNN이 객체를 분류하고 박스를 정교하게 조정합니다.
* RPN: Region Proposal Network, ROI (Region of Interest)를 자동 생성
* 장점으로 ROI 풀링과 ResNet 백본의 영향으로 정확도가 높습니다.
* 단점으로 네트워크가 2단계로 진행되어 실시간 처리가 어렵고 모듈수가 많아 구조가 복잡합니다.
#### YOLO의 모델에 대하여 설명하라
* YOLO는 1 stage 디텍션 모델입니다. 이미지를 그리드로 나누고 한번에 객체 검출을 수행하는 방식을 사용합니다. 각 그리드 셀이 객체의 클래스와 바운딩 박스를 한번에 예측하고 NMS로 중복된 박스를 소거합니다.
* NMS: Non-Maximum Suppression, 중복 검출 결과를 제거하는 후처리 기법입니다. 하나의 객체에 대하여 여러개의 바운딩 박스가 예측되면, 박스 중에 컨피던스 스코어가 가장 높은 박스만 선택합니다. 이 박스와 많이 겹치는 (IoU가 높은) 박스는 제거합니다.
* 장점으로 실시간 처리가 가능할 정도로 빠르고 end-to-end CNN 형태로 구조가 간단합니다.
* 단점으로 격자 기반 예측 방식으로 인해 작은 크기의 객체 인식 성능이 낮고 속도에 중점을 뒀기 때문에 상대적으로 정확도가 낮습니다.
#### 가장 선호하는 객체인식 알고리즘을 설명하고 장단점을 설명하라
* YOLO 입니다. 실시간 처리가 가능하며 end-to-end 모델이라는 점이 제가 추구하는 방향이랑 동일하기 때문입니다.
#### DETR 모델에 대하여 설명하라
* DEtection TRansformer는 메타 연구진이 발표한 객체 인식 모델입니다. 기존 모델의 복잡한 후처리 과정인 RPN과 NMS를 없애고 트랜스포머를 사용해 end-to-end로 학습이 가능합니다. 그리고 고정된 숫자의 object query를 사용해서 이미지 내 객체를 직접 예측하고, object query에서 FFN을 통해 객체의 클래스와 위치를 예측합니다.
#### CLIP 모델에 대하여 설명하라
* Contrastive Language-Image Pre-training은 오픈AI가 발표한 멀티모달 모델입니다. 이미지와 텍스트를 같은 스페이스에 매핑해서 둘 사이의 관계를 학습하는 모델로 contrastive learning을 사용합니다.
* contrastive learning: 같은 이미지-텍스트 쌍은 가깝게, 관계없는 이미지-텍스트 쌍은 멀게 학습히는 방법입니다. cosine similarity로 유사도를 계산하는 InfoNCE Loss를 사용합니다.
#### LLaVA 모델에 대하여 설명하라
* LLM 모델인 LLaMA에 CLIP의 비전 인코더를 연결한 멀티모달 모델입니다. instruction tuning으로 시각-언어 데이터의 기본 능력을 학습하고 GPT-4의 데이터로 미세조정을 했습니다.
* instruction tuning: CLIP의 이미지 임베딩을 LLM의 토큰 임베딩과 정렬하는 것을 목적으로 하며, CLIP의 이미지 임베딩을 LLM의 토큰 임베딩으로 변환하는 프로젝션 레이어를 학습합니다.
#### 최신 VLM 모델에 대하여 설명하라 (2025.02)
* DALL-E-3, GPT-4V, Claude 3, MoE-LLaVA, LLaVA-CoT 등이 있습니다. 이미지 인코더와 기존 LLM을 합치는 방향으로 연구가 진행되고 있고 MoE 나 CoT 같은 메서드가 활용되고 있습니다.
* MoE: Mixture of Experts, 여러 전문가 네트워크를 조합해 효율적인 추론을 하는 방식입니다.
* CoT: Chain of Thought, 복잡한 추론을 단계적으로 수행하는 방식입니다.
#### avg pooling과 max pooling의 차이를 설명하라
* 풀링 레이어는 입력 데이터의 크기를 줄이면서 중요한 특징을 추출합니다.
* avg pooling은 영역 내 모든 값의 평균을 취해 전반적인 특징을 보존하고 max pooling은 영역 내 최댓값만 선택해 가장 두드러진 특징만 유지합니다. 일반적으로 max pooling을 더 많이 사용합니다.
#### semantic segmentation을 설명하라
* 이미지의 각 픽셀을 특정 클래스로 분류하는 작업 입니다. 대표적인 모델으로 FCN, U-Net이 있습니다.
#### CNN이 MLP보다 좋은 이유는 무엇인가
* CNN은 필터를 사용하는데 이는 곧 파라미터를 공유하는 것으로 메모리를 효율적으로 사용할 수 있고 주변 픽셀과의 관계를 학습할 수 있습니다.
#### CNN의 파라미터 수를 계산하는 방법을 설명하라
* (커널 크기 * 커널 크기 * 입력 채널 * 출력 채널) + 출력 채널 입니다.
#### 볼츠만 머신을 설명하라
* 현재 딥러닝 네트워크의 전신인 restricted 볼츠만 머신은 가시층과 은닉층으로 구성되어 있습니다. 각 층의 노드들은 확률적 상태를 가지며 실제값과 재구성값의 차이를 가중치 업데이트에 활용합니다. 역전파 알고리즘 없이 학습하는 초기의 딥러닝 알고리즘 입니다. 이 RBM이 곧 FC layer와 동일한 구조를 가집니다.
#### 오토인코더를 설명하라
* 입력을 압축했다가 복원하는 비지도학습 모델입니다. 인코더는 입력을 저차원으로 점차 압축하고 디코더는 압축된 정보를 원본 차원으로 점차 복원합니다.
<br><br>

### [머신러닝]
#### 머신러닝이란 무엇인가
* 데이터에서 패턴을 학습하여 새로운 데이터에 대한 예측을 하는 알고리즘을 말합니다.
#### 머신러닝의 학습법 종류를 설명하라
* 지도학습, 비지도학습 등이 있습니다. 지도학습은 정답이 있는 데이터로 학습하는 것으로 종류는 분류와 회귀가 있습니다. 비지도학습은 정답 없이 데이터의 패턴을 발견하는 것으로 종류는 군집화와 차원축소가 있습니다. 이외에도 강화학습, 자기지도학습 등이 있습니다.
#### precision, recall 공식과 개념을 설명하라
* 프리시전은 양성으로 예측한 것 중에 실제 양성인 비율으로 TP/(TP+FP) 입니다. 리콜은 실제 양성 중에 양성이라 예측한 비율으로 TP/(TP+FN) 입니다.
#### precision, recall의 중요성과 trade-off의 본질은 무엇인가
* 정성적인 의미로 프리시전은 불량이 아닌 것도 얼마나 과하게 검출을 했는가를 평가하는 것이고, 리콜은 불량인 것들 중에서 몇개를 놓쳤는가를 평가하는 것입니다.
* 모델을 어떤 각도로 평가하는지에 따라 중요성이 달라지며 동일한 성능이라고할 때 하나를 높이면 하나는 내려갈 수 밖에 없습니다. 예를들어 모델의 성능은 같은데 불량을 놓치지 않고 싶다면 과하게 검사할 수 밖에 없는 것입니다.
#### F1 공식과 의미를 설명하라
* 2*(프리시전*리콜)/(프리시전+리콜)으로 두 값의 조화평균 입니다. 두 지표가 균형있게 좋은지 평가하는 지표 입니다.
#### 매크로 F1 스코어와 마이크로 F1 스코어 차이를 설명하라
* 매크로 F1 스코어는 각 클래스별 F1 스코어의 평균을 구해 모든 클래스를 동등하게 비교합니다. 반면 마이크로 F1 스코어는 전체 데이터에서 프리시전과 리콜을 먼저 계산하고 F1을 구해 데이터가 더 많은 클래스에 많은 가중치를 줍니다. 소수의 클래스도 중요하면 매크로 F1 스코어를, 다수 클래스가 중요하면 마이크로 F1 스코어를 사용하면 됩니다.
#### 선형 회귀의 기본 가정은 무엇인가
* 선형 회귀는 선형성, 독립성, 등분산성, 정규성을 가정합니다.
* 선형성(독립 변수와 종속 변수의 선형관계), 독립성(오차들이 서로 독립), 등분산성(오차의 분산이 일정), 정규성(오차가 정규분포를 따름)
* (y = w1x1 + w0 + ε에서 ε가 오차. 얼마나 설명하지 못했는지를 나타냄.)
#### KNN과 K-means에 대하여 설명하라
* KNN은 해당 데이터의 K개 이웃의 다수결에 의해 분류하는 지도학습이고, K-means는 랜덤으로 클러스터 중심을 정하고 클러스터에 속한 샘플의 평균값으로 중심을 변경하며 최적의 군집을 찾는 비지도학습 입니다.
#### DBSCAN과 GMM에 대하여 설명하라
* DBSCAN은 특정 반경 내에 있는 점들의 갯수가 일정 수 이상이면 하나의 군집으로 만들며, GMM은 여러 개의 가우시안 분포를 섞어서 데이터를 모델링 합니다.
* 각 모델의 하이퍼파라미터는 DBSCAN은 반경인 입실론과 최소 수인 min 이고, GMM은 군집 수 입니다.
* 각 모델의 특징은 DBSCAN은 군집 수를 정하지 않아도 되지만 밀도가 다양하면 작동하지 않는 것이고, GMM은 데이터가 겹쳐도 잘 작동하지만 군집 수를 정해야하는 단점이 있습니다.
#### 데이터 샘플링을 설명하라
* 데이터의 일부를 추출하여 분석이나 학습에 사용하는 것 입니다.
* 무작위로 선택하는 random 샘플링, 종속변수의 클래스 비율을 유지하는 stratify 샘플링, 복원추출 방식을 사용하는 부트스트랩 샘플링 등이 있습니다.
#### 부트스트랩 샘플링에 대하여 설명하라
* 데이터를 샘플링하고 다시 되돌려 놓는 복원추출 방식으로 여러 개의 데이터셋을 생성하는 방법입니다. 제한된 샘플 데이터로부터 더 큰 통계적 추론을 만들어낼 수 있습니다.
#### 앙상블 학습에 대하여 설명하라
* 보팅, 배깅, 스태킹, 부스팅 등이 있습니다. 보팅 (서로 다른 모델의 투표 결과로 예측), 배깅 (하나의 모델을 부트스트랩 샘플링한 데이터에 대하여 학습하고 결과를 집계), 스태킹 (서로 다른 모델을 부트스트랩 샘플링한 데이터에 대하여 학습하고 결과를 집계), 부스팅 (여러개의 클래시파이어가 가중치를 전달하며 순차적으로 학습).
#### PCA가 무엇이고 언제 사용하는가
* 차원축소 기법 중에 하나로 데이터를 압축할 때 사용합니다. 분산을 최대한 보존하면서(데이터의 특징을 잘 설명하면서) 직교하는 새로운 축을 찾아 투영하는 방식으로 차원을 축소하는 기법입니다.
#### RMSE, MSE, MAE의 수식과 차이점을 설명하라
* MSE는 오차의 제곱의 평균이고 RMSE는 MSE의 제곱근 입니다. MAE는 오차의 절대값의 평균입니다. 제곱이나 평균은 부호를 제거하기 위해서 사용하고 루트는 제곱이 실제값과 크기가 달라지기 때문에 사용합니다.
#### CE에 대하여 설명하라
* (원핫 인코딩된 실제값) * 로그 (예측 확률)을 모두 더한 값으로 예측 확률 분포와 실제 정답 분포 간의 차이를 계산합니다.
#### Markov Chain을 설명하라
* 현재 상태가 직전 상태에만 의존하는 확률 과정입니다. 다음 상태는 오직 현재 상태에만 영향을 받으며, 과거 상태들은 고려하지 않습니다. 날씨 예측이나 주가 예측 등에 활용됩니다.
#### SVM에 대하여 설명하라
* 두 클래스 간의 경계를 찾는 알고리즘으로 마진을 최대화하는 초평면을 찾는 것을 objective로 하는 알고리즘 입니다.
#### SVM은 왜 반대로 차원을 확장시키는 방법을 사용하는지 설명하라
* 저차원에서 선형 분리가 불가능한 데이터를 고차원으로 매핑하면 선형 분리가 가능한데 이를 커널 트릭이라고 합니다. 이렇게 프로젝션과 연산으로 두단계로 한다면 계산량이 늘어나지만 내적을 활용하면 한번에 효율적으로 계산할 수 있습니다.
#### 회귀와 분류에 알맞은 matric을 선택하고 설명하라
* 회귀는 큰 오차가 있을 경우 MSE가 적절하고 이상치가 있을 경우 MAE가 적절합니다.
* 분류는 accuracy가 보편적으로 좋지만 데이터 불균형이 있을 경우 F1이 적절합니다.
#### 인공신경망이 가지는 문제점을 설명하라
* 학습 데이터의 양이 많아야하고 학습에 많은 양의 컴퓨팅 리소스를 필요로 합니다. 또한 블랙박스로 모델 해석이 어렵습니다.
#### ROC 커브에 대하여 설명하라
* 이진 분류기의 성능을 시각화하는 그래프입니다. x축은 FP rate, y축은 TP rate를 나타냅니다. 곡선 아래 면적이 클수록 좋은 성능을 의미합니다.
#### 서버가 100개 있을 때 인공신경망보다 랜덤포레스트를 선택해야 하는가
* 랜덤포레스트가 더 적합합니다. 각 트리를 독립적으로 학습할 수 있어 병렬 처리가 자연스럽고, 서버 간 통신 부하가 적습니다. 반면 신경망은 파라미터 동기화가 필요해 분산 학습 시 통신 부하가 크고, 학습 안정성도 떨어질 수 있습니다.
#### cross validation에 대하여 설명하라
* 전체 데이터를 k개의 폴드로 나누어 k-1개로 학습하고 1개로 검증하는 과정을 k번 반복하는 방법입니다. 과적합을 방지하고 모델의 일반화 성능을 평가하는데 유용합니다.
#### gradient boosting에 대하여 설명하라
* 여러개의 디시전 트리를 순차적으로 학습하는 앙상블 기법입니다. 각 단계에서 이전 모델이 만든 오차를 줄이기 위해 그라디언트를 계산하고 이를 보정하는 방식으로 새 모델을 추가합니다.
#### XGBoost에 대하여 설명하라
* 그라디언트 부스팅의 계산 효율성과 과적합 방지를 개선한 모델입니다. 병렬 처리와 분산 학습이 가능하고 정규화 기법을 포함하고 있습니다.
#### LightGBM에 대하여 설명하라
* 그라디언트 부스팅의 속도와 메모리 사용량을 개선한 모델입니다. leaf-wise 방식으로 트리를 생성해 더 깊은 노드까지 효율적으로 학습하고 카테고리컬 데이터를 인코딩 없이 직접 사용할 수 있습니다.
#### 좋은 모델이란 무엇인가
* 좋은 모델은 과적합 되지 않고 잘 일반화되며 설명이 가능하고 안정적으로 잘 작동하는 모델입니다. 단순히 학습 데이터에서만 성능이 좋은 것이 아니라 실제 문제 해결에 도움이 되어야 합니다.
#### 하이퍼 파라미터 최적화 방법을 설명하라
* 모든 조합을 시도하는 그리드 서치, 레인지 안의 무작위 값을 선택하는 랜덤 서치, 이전 시도 결과를 바탕으로 최적 값을 예측하며 탐색하는 베이지안 옵티마이저 등이 있습니다.
#### feature selection의 목적과 방법을 설명하라
* 과적합을 방지하고 계산 비용을 줄이기 위함입니다. filter 방법으로 상관계수가 높으면 소거할 수 있고, wrapper 방법으로 성능을 보고 선택할 수 있고, embedded 방법으로 학습 과정에서 소거하여 선택할 수 있습니다.
#### 데이터 불균형이 무엇이고 해결하는 방법을 설명하라
* 특정 클래스의 데이터가 다른 클래스에 비해 매우 적은 상황으로 오버피팅이나 언더피팅을 유발합니다. 오버샘플링, 언더샘플링, 클래스 가중치 설정 등을 통해서 해결할 수 있습니다.
#### 다중공산성을 설명하고 문제가되는 이유는 무엇인지 설명하라
* feature들 간에 강한 상관관계가 있는 현상입니다. feature를 많이 사용하더라도 대부분 같은 의미를 설명하기 때문에 소용이 없게 됩니다. 따라서 성능이 낮게 나올 가능성이 큽니다.
#### 차원의 저주에 대하여 설명하라
* 고차원의 데이터에서 차원이 증가할수록 학습에 필요한 데이터의 양이 기하급수적으로 증가하는 현상입니다. 거리 기반 알고리즘의 성능이 저하되고 데이터 밀도가 희박해져 과적합될 가능성이 큽니다. 따라서 차원축소가 필요합니다.
#### feature importance와 shapley vlaue의 주된 차이는 무엇이고 어떤 분석을 선호하는지 설명하라
* feature importance는 컬럼이 데이터셋 전체적으로 얼마나 영향력이 있는지 측정하는 것이고 shapley value는 컬럼이 각 예측 하나하나에 대한 개별 기여도와 방향성을 계산합니다. 따라서 로컬과 글로벌 해석이 모두 가능한 shapley value를 더 선호합니다.
<br><br>

### [통계학]
#### 편향과 분산에 대하여 각각 설명하라
* bias는 예측값이 실제값과 얼마나 다른지를 나타냅니다. variance는 데이터의 변화에 따라 모델의 예측이 얼마나 달라지는지를 나타냅니다. 예를들어 bias가 높고 variance가 낮은 모델은 탄착군은 형성되지만 중심을 못맞추는 사수라고 볼 수 있고 variance가 높고 bias가 낮은 모델은 중심 근처를 맞추지만 넓게 퍼진 형태로 쏘는 사수라고 볼 수 있습니다.
#### p-value를 모르는 사람에게 설명하라
* 가정한 결과가 우연히 나올 확률 입니다. 예를 들어 p-value가 0.05라면 이런 결과가 우연히 나올 확률이 5%밖에 안 된다는 의미로, 결과가 통계적으로 의미있다고 볼 수 있습니다.
#### R^2의 의미는 무엇인가
* 모델이 데이터의 변동을 얼마나 잘 설명하는지를 나타내는 지표입니다. 0~1 사이의 값을 가지며, 일반적으로 0.64가 넘으면 모델의 설명력이 좋다고 판단합니다. 결정계수는 상관계수의 제곱값으로 계산할 수 있습니다.
#### 시그마는 무엇이고 1~3 시그마 값은 몇인가
* 시그마는 표준편차를 의미합니다. 정규분포를 가정하면 중심으로부터 ±1시그마 = 68%, ±2시그마 = 95%, ±3시그마 = 99.7% 입니다. (2시그마랑 p-value 0.05랑 비슷한 수준)
#### 평균과 중앙값의 차이와 사용 예시를 설명하라
* 모든 값의 합을 개수로 나눈 값으로 이상치에 민감합니다. 반면에 중앙값은 데이터를 정렬했을 때 가운데 있는 값으로 이상치의 영향이 적습니다.
#### 중심극한정리를 설명하라
* 표본의 크기가 충분히 크면, 표본평균의 분포는 정규분포에 가까워진다는 이론입니다. 이는 모집단의 분포와 관계없이 성립합니다.
#### 엔트로피와 information gain을 설명하라
* 엔트로피는 데이터의 불확실성을 측정하는 지표이고 information gain은 특정 특성으로 분할했을 때 줄어드는 엔트로피의 양입니다. 디시전 트리에서 사용합니다.
#### probability와 likelyhood의 차이를 설명하라
* probability는 주어진 모수에서 특정 데이터가 관찰될 확률이고 likelyhood는 관찰된 데이터가 주어졌을 때 특정 모수가 맞을 가능성입니다.
* probability는 공정하다는 것을 가정하고 미래의 결과를 예측하는 것이고 likelyhood는 이미 결과를 관찰한 뒤 동전이 공정할 가능성을 평가합니다.
#### 베이지안과 프리퀀티스트의 차이를 설명하고 본인의 의견을 설명하라
* 베이지안은 확률을 확률변수로 해석하고 사전 확률을 설정한 뒤 새로운 데이터로 확률을 업데이트합니다. 반면, 프리퀀티스트는 확률을 장기적인 빈도로 해석하고 확률를 고정된 값으로 봅니다.
* 베이지안의 입장에서 확률은 불확실성이 있고 계속 변하는 것이고 프리퀀티스트의 입장에서 확률은 이미 많은 데이터에 의해 결정된 것 입니다.
* 저는 프리퀀티스트 입니다. 통계적 검정인 p-value 0.05, 상관계수 0.8 등을 활용하는 편이고 데이터는 객관적이고 진실을 반영하며 데이터에 의한 의사결정을 추구하기 때문입니다.
#### missing value가 있을 경우 채워넣을 것인가
* 데이터가 랜덤하게 없을 경우 평균값이나 중앙값으로 대체할 것이고 특정한 패턴이 발견될 경우 그 자체로 의미있는 정보일 가능성이 있으므로 별도로 처리할 것입니다.
#### 아웃라이어를 판단하는 기준은 무엇인가
* 통계적으로 Q1 - 1.5xIQR 과 Q3 + 1.5xIQR을 넘어간 값 입니다. (z-score 3시그마 추가 질문 시 대답)
#### 아이겐벡터와 아이겐벨류가 무엇이고 왜 중요한가
* 아이겐벡터는 선형변환 후에도 방향이 유지되는 벡터이고 아이겐벨류는 해당 벡터의 스케일 변화량 입니다. 차원축소 알고리즘에서 활용할 수 있고 복잡한 선형 변환을 간소화시켜주기 때문에 중요합니다.
#### 상관관계와 인과관계의 차이점을 설명하라
* 상관관계는 두 변수 간의 통계적 연관성이 있다는 것으로 선형이나 비선형관계가 있다는 것 입니다. 인과관계는 긴밀한 원인 결과 관계가 있다는 것으로 한 변수가 다른 변수에 직접적인 영향을 준다는 것 입니다.
#### 귀납적 논리와 연역적 논리의 차이점을 설명하라
* 귀납적 논리는 인덕션으로 사례에서 일반적인 규칙을 도출하는 것이고 연역적 논리는 디덕션으로 일반적인 규칙에서 결론을 도출하는 것입니다. 대표적인 예시로 인덕션에는 머신러닝이 있고 디덕션에는 삼단논법이 있습니다.
#### 동전을 10번 던졌는데 앞면이 1번 나왔다. 공정성 테스트를 위한 귀무가설과 p값은 무엇인가
* 귀무가설은 동전이 공정하다로 앞면이 나올 확률이 0.5인 것입니다. P값은 이항 분포 B(10, 0.5)에서 1번 이하로 나올 확률이므로 P값은 (1+10)x1024 = 0.011 정도 입니다. 유의수준 0.05에서 귀무가설을 기각하므로 동전은 불공정합니다.
#### 1000번 동전을 던졌을 때 550번 앞면이 나왔다. 동전은 편향되었는가
* 귀무가설은 동전이 공정하다로 앞면이 나올 확률이 0.5인 것입니다. 이항분포를 정규분포로 근사하면 n=1000, p=0.5 입니다. 이항분포에서 평균은 np로 500 이고 이항분포에서 시그마는 √np(1-p) 이므로 √250 이고 16정도 입니다. 중심으로부터 벗어난 거리 50을 시그마로 나누면 z score가 3이 넘으므로 동전은 공정하지 않습니다.
#### 4보다 큰 숫자가 나올 때까지 주사위를 연속으로 굴렸는데 4번째에서 나오는 확률은 얼마이고, 4번째 미만의 시도에서 성공할 확률은 얼마인가
* 한번에 성공할 확률은 2/6으로 1/3 입니다. 3번 모두 실패할 확률은 (2/3)^3 이므로 8/27 이고 마지막에 성공할 확률 1/3을 곱하면 8/81으로 약 0.1 입니다. 4번째 미만의 시도에서 성공할 확률은 1-0.1=0.9 입니다.
#### 주사위가 두번 연속으로 5가 나올때까지 굴릴 때 예상되는 굴리는 횟수
* 한번에 성공할 확률은 (1/6)^2로 1/36 입니다. 따라서 예상 횟수는 1/p로 36회 입니다.
#### 두 게임 중에 무엇이 더 유리한가. 게임1: 한번에 두개 주사위를 던져 두 값의 곱에 해당하는 달러를 가진다. 게임2: 하나의 주사위를 던져 값의 제곱에 해당하는 달러를 가진다.
* 주사위의 모든 눈 수의 합은 7*3인 21이고 면이 6개 이므로 기댓값은 21/6=7/2 입니다. 게임 1은 기댓값 두개를 곱하는 것이므로 약 49/4=12 입니다. 게임 2는 1+4+9+...+36=91에 6을 나눈 값으로 약 91/6=15 입니다. 따라서 게임2가 더 유리합니다.
#### 사용자의 80%가 60%의 영화에 좋아요를 누르고 사용자의 20%는 모든 영화에 좋아요를 누르는 'lazy user'이다. 누군가 연속으로 3개 영화에 좋아요를 눌렀다면 'lazy user'일 확률은 얼마나 되는가
* 베이즈 정리를 사용하여 계산합니다. P(Lazy)=0.2, P(3likes|Lazy)=1, P(3likes|Unlazy)=0.6^3=0.2 입니다. 
* P(Lazy|3likes) = P(3likes|Lazy)xP(Lazy)/P(3likes) 이므로 P(3likes)를 구해야합니다.
* P(3likes) = P(3likes|Lazy)xP(Lazy) + P(3likes|Unlazy)xP(Unlazy)로 구할 수 있습니다.
<br><br>

### [데이터분석]
#### AB 테스트에 대하여 설명하라
* 두 가지 버전(A와 B)을 무작위로 사용자에게 보여주고 어떤 버전이 더 효과적인지 통계적 유의성을 검증하여 의사결정에 활용하는 방법입니다.
#### EDA가 중요한 이유를 설명하라
* 데이터의 특성, 패턴, 이상치를 파악하여 더 나은 의사결정을 할 수 있게 해주기 때문입니다. 데이터 전처리 방향과 분석 방법을 선택하는 데 도움을 줍니다.
#### 좋은 feature란 무엇이고 판단하는 방법을 설명하라
* 좋은 feature는 타겟 변수와 높은 상관관계가 있고, 다른 feature들과는 낮은 상관관계를 가지는 feature 입니다.
#### NoSQL과 RDBMS의 차이점을 설명하라
* NoSQL은 유연한 스키마를 가지고 있어 대용량 데이터 처리에 적합하며 수평적 확장이 용이합니다. (=몽고DB, 카산드라) RDBMS는 정형화된 스키마와 관계를 중시하며, 데이터 일관성을 보장합니다. (=MySQL)
#### window 함수에 대하여 설명하라
* 행과 행 간의 관계를 정의하여 연산하는 함수입니다. 랭킹 함수, 집계 함수 등이 있으며 partition by로 그룹을 나누고 order by로 정렬을 할 수 있습니다.
#### MySQL에 대량의 데이터를 insert 하는 방법을 설명하라
* LOAD DATA INFILE을 사용하여 csv 파일을 로드하거나 여러 insert를 하나의 트랜잭션으로 묶어서 처리하면 됩니다.
#### 쿼리 성능을 확인하는 쿼리문은 무엇인가
* SHOW PROFILE을 사용해 쿼리의 실행 시간과 리소스 사용량을 확인할 수 있습니다. EXPLAIN을 사용하면 실행 계획을 자세하게 볼 수 있습니다.
#### MySQL이 느릴 때 가장 먼저 보는 것인 무엇인가
* slow_query_log 설정을 켜서 넥이 되는 쿼리를 확인합니다. 또한 EXPLAIN으로 쿼리의 성능을 확인하고 CPU나 메모리의 상태를 확인합니다.
#### 동작하고 있는 MySQL을 백업하는 방법은 무엇인가
* DB가 작을 경우 논리적 백업으로 mysqldump를 하고 DB가 클 경우 물리적 백업으로 XtraBackup를 사용하면 됩니다.
#### Tableau를 사용하는 이유를 설명하라
* 대시보드 제작이 쉽고 빠르기 때문입니다. 상호작용이 가능한 그래프를 그릴 수 있고 실시간으로 데이터를 업데이트할 수 있는 장점이 있습니다.
#### 4가지 이상의 정보를 시각화하는 방법을 설명하라
* 다차원 플랏을 설계하면 됩니다. 예를들어 뒤에 낮은 투명도로 막대 그래프를 그리고 위에 산점도 그래프를 그립니다. 산점도의 모양, 크기, 색깔을 통해서 차원을 더 추가할 수 있습니다.
#### 파이차트가 좋지 않은 이유를 설명하라
* 각도나 면적 비교가 어려워서 정확한 비교가 어렵습니다. 특히 비슷한 크기의 조각이 있으면 정확한 숫자를 표시해야 누가 더 큰지 알 수 있습니다.
#### hadoop과 spark의 차이를 설명하라
* 하둡은 디스크 기반이고 스파크는 메모리기반 입니다. 그래서 스파크는 속도가 더 빠르고 실시간 처리가 가능하고 하둡은 배치 처리에 특화되어 있습니다.
#### MapReduce에 대하여 설명하라
* 대용량 데이터 처리를 위한 분산 프로그래밍 모델입니다. 키-벨류 쌍을 생성하는 맵 단계, 맵 단계의 중간 결과를 전송하는 셔플 단계, 그룹화된 데이터를 처리해 최종 결과를 계산하는 리듀스 단계로 진행됩니다.
#### 잘 만들어지는 MapReduce는 무엇인가
* 특정 파티션이나 키에 집중되는 데이터 스큐 현상이 없고 네트워크 부하를 발생시키는 셔플링이 최소화된 경우 입니다. 맵 단계에서 최대한 데이터를 필터링한 뒤에 최대한 작은 양의 데이터를 가지고 리듀스 작업을 하는 것이 좋습니다.
#### MapReduce 중간에 fail이 나는 것을 어떻게 모니터링 하는가
* YARN log -applicationId 나 JobTracker를 통해서 모니터링할 수 있습니다.
#### 분산환경의 join은 (디스크, CPU, 네트워크) 중 어디서 병목이 일어나고 해결방법은 무엇인가
* 주로 네트워크에서 병목현상이 발생합니다. 데이터 셔플링을 할 때 네트워크의 부하가 큽니다. 브로드캐스트 조인이나 버킷팅으로 개선할 수 있습니다.
#### 암달의 법칙을 설명하고 shared-nothing 구조를 설명하라
* 암달의 법칙은 병렬화로 얻을 수 있는 최대 성능 향상을 계산하는 법칙 입니다. shared-nothing 구조는 노드 간에 리소스를 공유하지 않는 아키텍처를 말하며 독립적인 리소스를 가지므로 네트워크 부하를 최소화 합니다.
#### shared-nothing의 장단점을 설명하라
* 장점은 확장성이 높고 리소스간에 경쟁이 발생하지 않는 것이고 단점은 데이터 정합성 관리가 어렵고 노드 간 통신에서 부하가 발생할 수 있는 것입니다.
#### 대용량 자료를 빠르게 lookup하기 위한 백엔드는 무엇인가
* Redis 같은 인메모리 DB가 좋습니다. 키-벨류 구조로 빠른 검색이 가능하기 때문입니다.
#### Apache 보다 Nginx가 성능이 좋은 이유를 설명하라
* 이벤트 기반 처리 방식으로 메모리를 적게 사용하고 동시 접속도 잘 처리하기 때문입니다. 아파치는 프로세스 기반이라 리소스를 많이 사용합니다.
#### node.js는 빠르지만 사용하면 안되는 경우를 설명하라
* node.js는 CPU 집약적 계산을 목적으로 만든 언어가 아니며 싱글 스레드이기 때문에 계산 시간이 오래걸리면 다른 요청이 모두 막히기 때문입니다.
<br><br>

### [알고리즘]
* [ref](https://velog.io/@cis07385/%EB%A9%B4%EC%A0%91-%EC%98%88%EC%83%81-%EC%A7%88%EB%AC%B82-8dy1ey0c)
#### 파이썬의 특징에 대해 설명하라
* 파이썬은 인터프리터 언어입니다. 코드를 작성한 후 컴파일 없이 즉시 실행할 수 있습니다. 가독성이 높은 특징이 있고 머신러닝과 데이터 분석과 같은 다양한 분야에서 사용됩니다.
#### 인터프리터와 컴파일러의 차이를 설명하라
* 인터프리터는 소스 코드의 내용을 한번에 한줄씩 읽어들여서 실행합니다. 소스 코드를 해석하는데는 적은 시간이 걸리지만 실행 시간은 느립니다.
* 컴파일러는 전체 프로그램 코드를 스캔하여 소스 코드(하이 레벨 프로그래밍 언어)를 오브젝트 코드(로우 레벨 프로그래밍 언어)로 바꾸어주는 역할을 합니다. 컴파일러는 소스코드를 해석하는데는 많은 시간이 걸리지만 한번 오브젝트 코드로 바꿔놓으면 실행 시간은 빠릅니다.
#### PEP8에 대하여 설명하라
* PEP는 파이썬 코딩 규칙에 대한 제안서 입니다. 내용으로는 들여쓰기에서 tab과 space 혼합사용 금지, 최대 줄 79자 이상에서 백 슬래시 사용, 네이밍에서 클래스는 첫글자 대문자와 함수는 소문자와 언더바 사용 등이 있습니다.
#### 파이썬 데코레이터, 제너레이터, 이터레이터의 개념과 사용 예시를 설명하라
#### 탐색의 방법은 무엇이 있고 각각의 시간 복잡도를 설명하라
#### 해시 알고리즘을 설명하라
<br><br>

### [자료구조]
#### 리스트와 튜플의 공통점과 차이점을 설명하라
* 공통점으로는 둘 다 여러 데이터를 담을 수 있는 컨테이너형 변수입니다. 그리고 인덱스를 통해 특정 요소에 접근할 수 있으며, iterable 합니다.
* 차이점으로는 리스트는 mutable 하지만 튜플은 immutable 합니다. 수정할 수 없는 특징 때문에 리스트는 딕셔너리의 키 값으로 사용 불가능 하지만, 튜플은 사용 가능합니다. 또한 같은 개수의 for 문을 돌리면 튜플이 리스트보다 속도가 빠릅니다. 리스트는 객체가 생성된 후 크기 확장을 대비해 추가 메모리를 할당하지만 튜플은 크기가 고정적이기 때문에 최소 메모리만 할당하기 때문입니다.
#### 파이썬의 메모리 할당 방법을 설명하라
* 
#### 파이썬 리스트와 딕셔너리의 차이를 설명하라
<br><br>

### [컴퓨터과학]
#### 서버를 처음 사고 어떤 보안적 조치를 할지 설명하라
#### 동시에 10개 컴퓨터에 라이브러리를 설치하는 번거로움을 해결하는 방법
#### vim과 emacs 중에 어떤 것을 사용하는가
#### 가장 좋아하는 리눅스 배포판과 이유를 설명하라
#### 관리하는 서버가 10대가 넘었을 때 중요한 모니터링 지표는 무엇인가
<br><br>



## `[인성 면접]`
* 두괄식으로 말하기
* 내가 가진 경험, 역량, 소프트 스킬과 연계
* 경험 목록
    * 석사 논문의 딥러닝 설계
    * 멀티 GPU 리눅스 서버
    * 모델링 직무 준비 과정
    * LGD 애플워치 자동검사
    * 데이터분석 프로젝트
    * 논문 리뷰 블로그
* 역량 목록
    * AI 모델링
    * 도메인 지식 활용
    * AI 모델 숙련도
    * 수학적 이해와 통계적 지식
    * 논문 리서치
    * AI 모델 트렌드
* 소프트 스킬 목록
    * 문제해결력
    * 창의성
    * 커뮤니케이션
    * 스토리텔링
    * 자기주도적 성장 의지
<br><br>

### [필수]
#### 자기소개
* 안녕하십니까 트랜스포머 연구 경험을 가진 김가람 지원자 입니다. 저는 (직무명) 직무를 원활히 수행할 수 있는 2가지 역량을 가지고 있습니다.
* 첫째 (역량) 입니다. (짧은 설명), 둘째 (소프트 스킬) 입니다. (짧은 설명)
* 이러한 (역량)과 (소프트 스킬)를 바탕으로 정량적인 성과를 이끌어내는 (직무명)으로 성장하겠습니다.
#### 지원동기
* 평소 (도메인)에 대한 관심을 가지고 있었고, (직무에서 하는일) 경험을 통해 (직무명)에 대한 확신이 생겼기 때문에 지원하게 되었습니다.
* (도메인 관련 경험)을 통해 (도메인)에 관심이 있었고 (회사명)에서 제 역량을 발휘할 수 있다고 생각해 지원하게 되었습니다.
* (직무 관련 경험)을 통해 (직무명)에 대한 확신이 생겼습니다.
* 종합적으로 제가 가지고 있는 (도메인)에 대한 관심과 경험을 통해 쌓은 (직무에서 하는일) 역량을 발휘해 (회사명)과 함께 발전할 수 있다는 생각을 해서 지원하게 되었습니다.
#### 장단점
* 장점으로 (소프트 스킬1)을 가지고 있습니다. (짧은 설명) (예시) (업무 적용)
* 단점으로 (소프트 스킬2)를 가지고 있습니다. (짧은 설명) (극복 방법)
<br><br>

### [회사관심도]
#### 우리 회사를 어떤 회사로 알고 있고 왜 지원했는가
* (도메인)에서 (직무에서 하는일)을 잘 활용하는 혁신적인 회사로 알고 있습니다. 대표적인 서비스로 (서비스명)을 사용해봤습니다.
* (지원동기)
#### 본인 역량을 우리 도메인에 어떻게 사용할 수 있는가
* (역량, 소프트 스킬)을 바탕으로 (구체적인 방법론)으로 (서비스명)에 활용하겠습니다.
* (서비스명)은 (구체적인 원인) 때문에 (역량, 소프트 스킬)이 필수적입니다.
* 저는 (경험)을 통해서 (역량, 소프트 스킬)을 키워왔습니다.
#### 입사 시 하고싶은 일이 무엇인가
* (구체적인 서비스)에서 (구체적인 업무) 업무를 하고 싶습니다.
* (구체적인 업무)은 (구체적인 원인) 때문에 (역량, 소프트 스킬)이 필수적입니다.
* 저는 (경험)을 통해서 (역량, 소프트 스킬)을 키워왔습니다.
#### 입사 후 포부를 말하라
* 먼저 새로 들어온 구성원으로서 업무를 적극적으로 배우겠습니다. 뚜렷한 목표를 가지고 회사의 노하우가 담긴 (직무에서 하는일) 방법론을 이해하겠습니다.
* 더 나아가 현재보다 더 높은 수준의 AI 모델링 능력을 위해 꾸준히 최신 논문과 알고리즘을 공부하겠습니다.
* 최종적으로 (구체적인 업무) 업무에서 (회사명)에 큰 힘이 되도록 노력하겠습니다. (역량1)과 (역량2)를 최대한 발휘하여 정량적인 성과를 이끌어내도록 하겠습니다.
#### 마지막 한마디
* (회사명)와 함께 (회사 맞춤 혁신적인 서비스)를 꼭 해보고 싶습니다.
<br><br>

### [직무경험]
#### 직무 경험에 대하여 짧게 설명하라
* 요약 -> S(상황) -> T(과제) -> A(행동) -> R(성과)
    * 석사 논문의 딥러닝 설계
    * LGD 애플워치 자동검사
#### 직무 경험에 대하여 자세히 설명하라
* 요약 -> S(상황) -> T(과제) -> A(행동) -> R(성과)
    * 석사 논문의 딥러닝 설계
    * LGD 애플워치 자동검사
#### 직무에서 이루고자 하는 목표는 무엇인가
* AI를 통해 실질적인 비즈니스 가치를 창출하는 것입니다. AI는 정말 유용한 도구이지만 아직 큰 돈을 벌거나 혁신적인 서비스를 만들어낸 기업이 많지 않다고 생각합니다. AI를 활용해서 금전적 가치와 공익적 가치를 창출해서 모범사례가 되고 싶습니다. 일하는 사람의 능력에 대한 가치를 평가한 것이 연봉인 것처럼 회사의 성장 가능성이나 지금 가지고 있는 능력에 대한 가치를 평가한 것이 투자금과 주가라고 생각합니다. 그래서 항상 금전적인 가치로 증명을 해야한다고 생각해서 금전적인 가치와 공익적 가치를 모두 창출하는 것이 목표입니다. 그리고 이 과정에서 회사와 제가 같이 큰 성장을 할 수 있다고 생각합니다.
#### 최근 가장 인상적으로 읽은 논문은 무엇인가
* I-JEPA 입니다. 이 모델은 2023년에 얀르쿤 교수님 연구진이 발표한 자기지도학습 모델입니다. 기존 마스킹 기반 모델과 달리 latent representation을 예측하는 방식을 사용했는데 픽셀을 복원할 필요 없이 representation 그대로를 예측하자는 간단하면서 임팩트 있는 아이디어가 인상적이었습니다.
<br><br>

### [프로젝트]
#### 이 알고리즘을 사용한 이유는 무엇인가
#### 다른 유사한 알고리즘을 알고 있는가
#### 이 알고리즘의 단점은 무엇인가
#### 주요 역할과 배운점은 무엇인가
#### 프로젝트를 다시 진행한다면 어떻게 할 것인가
<br><br>

### [압박]
#### 본인은 전공자가 아닌데 왜 이 직무를 지원하는가
#### 본인은 이 직무를 위해 어떤 준비를 해왔는가
#### 본인은 분석가 인재인가 사이언티스트 인재인가
#### 경쟁사를 지원했는가 왜 둘중에 우리 회사를 선택하는가
#### 다른 도메인의 회사도 지원했는가
#### 왜 박사를 하지 않았는가
#### 희망하지 않는 업무를 준다면 어떻게 할 것인가
<br><br>

### [소프트스킬]
#### 가장 힘들었던 순간은 언제인가
#### 리더 경험을 설명하라
#### 팔로워 경험을 설명허라
#### 존경인물이 누구인가
#### 가장 후회되는 일은 무엇인가
#### 취미는 무엇인가
#### 주량은 어떻게 되는가
#### 가족을 소개하라
#### 노조 문제에 대하여 어떻게 생각하는가
#### 상사와의 갈등이 생긴다면 어떻게 할 것인가
#### 상사가 부당한 지시를 내린다면 어떻게 할 것인가
#### 회사일과 개인일이 충돌하면 어떻게 할 것인가
<br><br>

### [역질문]
#### (능력있는 동료, 재밌는 주제, 돈이 되는 사업)
#### 팀의 규모와 구성은 어떻게 되나요?
#### 현재 진행되는 사업은 무엇이고 계획중인 신사업은 무엇인가요?
#### 직무에 도움이 될만한 공부 분야나 책이 있나요?
<br><br>


