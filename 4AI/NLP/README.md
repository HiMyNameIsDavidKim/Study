# Natural Language Processing(자연어 처리)

## `[examples]`
* [`Transformer 논문 구현`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/transformer_paper.py)
* [`소설 암기 모델 GRU_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/shakespeare_gru.py)
* [`소설 암기 모델 RNN_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/shakespeare_rnn.py)
* [`입력 기억 모델 LSTM_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/remember_lstm.py)
* [`입력 기억 모델 RNN_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/remember_rnn.py)
<br><br>



## `[morphology]`
* 형태론, 단어가 어떻게 구성되는지에 대한 연구
* Morpheme: 형태소, 의미를 가진 가장 작은 언어 단위
* Stem: 어간, 단어의 핵심 의미를 담고 있는 부분
* Affix: 어미, 어간에 붙어 문법적 기능이나 추가 의미를 제공
* Inflection: 굴절, 단어의 문법적 기능을 변경하지만 품사를 바꾸지 않는 형태 변화
* Derivation: 파생, 새로운 단어를 만드는 과정으로, 종종 품사를 변경
* Compounding: 합성, 두 개 이상의 어간을 결합하여 새로운 단어를 만드는 과정
* Morphological analysis: 단어를 형태소 단위로 분리
* Stemming: 단어에서 접사를 제거하고 어간을 추출
* Lemmatization: 단어를 기본형으로 변환
* Prefix(접두사), Suffix(접미사), Infix(중간삽입사)
<br><br>



## `[VAE]`
* 데이터의 latent space를 학습하여 새로운 데이터를 생성할 수 있는 확률적 생성 모델.
* 베이즈 이론과 가우시안 확률 분포를 활용하며, 인코더와 디코더로 구성된다.
* latent space가 continuous 하다.
* 인코더
    * 입력 데이터를 받아 주요 feature를 인코딩한 결과인 latent variable을 생성한다.
    * 입력 데이터를 특정 확률 분포(=가우시안)로 변환한다.
    * 확률 분포를 통해 latent variable의 가능한 값과 가장 잘 표현된 값을 알 수 있다.
* 디코더
    * latent variable로 부터 원래 입력 데이터를 재구성한다.
    * latent variable에서 샘플링된 값을 사용하여 입력 데이터 재구성에 활용한다.
* 변형
    * VQ-VAE
        * latent space가 discrete 하다.
        * VAE 인코더의 가우시안을 사용하지 않는다. (확률 분포 가정 자체를 안함)
        * codebook을 discrete하게 양자화한 것으로 가장 가까운 codebook에 매핑한다.
    * dVAE
        * latent space가 discrete 하다.
        * 생성하는 데이터도 discrete 하다.
        * VAE 인코더의 가우시안을 다항이나 베르누이 같은 이산 확률 분포로 변경한 구조다.
<br><br>



## `[LLM]`
* upstream = pre-training, downstream = fine-tuning
* foundation model = pre-trained model
* prompt : 모델에 대한 지침. 올바른 결과를 유도하는 명령어.
* prompt engineering : 모델이 특정 작업을 수행하도록 도와주는 텍스트를 생성.
<br><br>



## `[Attention]`
* 어텐션 매커니즘 : 특정 시점에 입력 시퀀스의 각 단어 간의 중요도를 계산.
    * 어텐션 매커니즘의 벡터
        * 입력 임베딩에 W_Q, W_K, W_V 매트릭스를 내적해 얻을 수 있다.
        * Query : 현재 단어가 필요로 하는 정보에 대한 representation.
        * Key : 입력 시퀀스의 각 단어에 대한 특징. (어텐션 스코어용)
        * Value : 입력 시퀀스의 각 단어에 대한 특징. (컨텍스트 벡터용)
        * 보통 키와 벨류는 같은 벡터를 사용하나 용도가 다르다.
    * 어텐션 스코어 : 현재 단어의 Q와 각 단어 K의 유사도.
        * 현재 단어의 Q와 모든 단어의 K의 전치행렬을 각각 내적한다.
        * 여기에 sqrt(dim)을 나눠 스케일링 한다. (기울기 소실 방지)
        * 각 단어의 특징이 Q와 얼마나 관련이 있는지에 대한 수치.
        * 구하는 방법에 따라 어텐션 매커니즘의 종류가 결정.
        * 내적, 스케일드 내적 등
    * 어텐션 웨이트 : 현재 단어에 대한 각 단어의 중요도.
        * 어텐션 스코어를 소프트맥스 함수에 넣어 정규화한다.
    * 컨텍스트 벡터, Z_n : 현재 시점에서 각 단어 간의 중요도에 대한 요약.
        * 어텐션 웨이트와 V를 곱한 뒤 모두 더하여 얻을 수 있다.
        * 어텐션 웨이트는 단어 별로 상수값이고 V는 행렬이다.
        * 따라서 결과는 QKV 벡터와 같은 사이즈의 행렬로 나온다.
        * 각 단어에 대한 컨텍스트 벡터들을 concat하면 W_QKV 매트릭스와 같은 사이즈의 행렬이다.
    * 결과 임베딩, Z : 최종적으로 추출된 representation.
        * multi-head 수 만큼의 Z_n을 concat 한다.
        * 출력 매트릭스 W_O를 곱해 입력 임베딩과 같은 사이즈로 만든다.
        * 다음 시점의 모델에 입력 임베딩으로 제공 된다.
        * W_O도 학습 되는 것이고 사이즈를 바꾸면 출력 사이즈를 바꿀 수 있다.
<br><br>



## `[RNN]`
* 원 핫 벡터 : 단어 집합의 크기만큼의 벡터를 만들고, 각 단어의 인덱스에 1의 값과 나머지는 0을 부여하는 방법.
    * (ex. hello = [1,0,0], python = [0,1,0], ruby = [0,0,1])
    * 벡터들은 내적 시 무조건 0이 나온다. -> 단어마다 유사도가 있음을 표현할 수 없다.
    * 단어를 1개 추가하려면 모든 단어의 벡터를 수정해야한다.
* 임베딩 : 일정한 길이를 가지는 벡터 공간에 투영하는 방법.
    * (ex. [[hello, 0.05, 0.05, 0.05], [python, 0.51, 0.21, 0.31], [ruby, 0.52, 0.22, 0.32]])
    * 같은 계열인 python과 ruby는 비슷한 값을 가지게 할 수 있다.
    * CBOW, skip-gram 두가지 방법이 대표적.
    * CBOW : 주변 단어들로부터 가운데 들어갈 단어가 유추되도록 임베딩.
    * skip-gram : 중심 단어로 부터 주변 단어들이 유추되도록 임베딩.
<br><br>



## `[웹 크롤링]`
* 웹사이트, 하이퍼링크, 데이터를 자동화된 방법으로 수집 분류 저장하는 것.
    * 웹 사이트 : HTTP 프로토콜을 사용하여, URL에 HTML로 쓰인 문서.
    * 하이퍼 링크 : 주소와 주소를 중간과정 없이 옮겨다닐 수 있는 인터페이스.
    * 하이퍼 텍스트 : 하이퍼링크가 포함된 문서.
    * 플레인 텍스트 : 일반적인 NL만 있는 문서.
* URL 가져오는 방법 : F12 누르기 -> 엘리먼트 선택 툴 -> 사진 클릭 -> 코드 나옴
* html은 헤더와 바디로 나뉜다.
<br><br>

### [크롤러]
* 크롤러(기계 자동), 브라우저(인간 수동)
    * 크롤러 : 하이퍼 텍스트를 따라가며 자동으로 수집 분류 저장하는 프로그램. 인간의 개입X
    * 브라우저 : 하이퍼 텍스트를 읽도록 해주는 프로그램. 인간의 개입O
* 웹(데이터가 있다), 네트워크(데이터가 없다)
    * 네트워크가 있는 상태에서 데이터가 흐르게하면 웹이다.
* 크롤러(웹의 데이터에 접근하는 것) -> 스크래퍼(특정 데이터를 추출하는 것)
    * (flaskProject - scrapper 참고)
    <br><br>

### [라이브러리]
* 뷰티플수프 : 웹크롤링에서 가장 많이 사용하는 라이브러리.
* lxml : 빠르고 유연한 parser
    * Parser는 크롤링에서 쓰는 HTML 번역기.
    * xml : XML 파일에만 사용.
    * html5lib : 복잡한 구조의 HTML에 대해서 사용.
    * html.parser : 빠르지만 유연하지 않음. 단순한 HTML문서에 사용.
* HTML : 항상 start tag, element content, end tag로 구성된다.
    * start tag는 <태그이름> 형식으로, end tag는 </태그이름> 형식으로 쓴다.
* zip함수 : 여러개의 리스트를 for문에서 동시에 사용하고 싶은 경우 사용.
* URL 분석 : ‘{도메인}?{쿼리}’로 구성되며, 쿼리에는 키와 벨류가 있다.
<br><br>



## `[KONLP]`
* 한글을 사용한 NLP 라이브러리.
<br><br>



### [konlp 설치]
* jdk 설치 및 환경변수 여부 확인
* pip install JPype1-py3
* pip install konlpy
* pip install tweepy
<br><br>