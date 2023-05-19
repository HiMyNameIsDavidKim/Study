# Natural Language Processing(자연어 처리)

## `[examples]`
* [`Transformer 논문 구현`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/transformer_paper.py)
* [`소설 암기 모델 GRU_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/shakespeare_gru.py)
* [`소설 암기 모델 RNN_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/shakespeare_rnn.py)
* [`입력 기억 모델 LSTM_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/remember_lstm.py)
* [`입력 기억 모델 RNN_PT`](https://github.com/HiMyNameIsDavidKim/ML_Example/blob/main/NLP/remember_rnn.py)
<br><br>



## `[Attention]`
* 어탠션 매커니즘 : 특정 시점에 입력 데이터 중에 키워드에 집중하게 하는 기술.
    * 어탠션 매커니즘의 벡터
        * Query : 현재 시점에서 주의를 기울여하는 키워드.
        * Key : 입력 데이터의 각 부분에 대한 피쳐 값. (어탠션 스코어용)
        * Value : 입력 데이터의 각 부분에 대한 피쳐 값. (컨텍스트 벡터용)
        * 보통 키와 벨류는 같은 벡터를 사용하나 용도가 다르다.
    * 어탠션 스코어 : Query와 Key 간의 유사도.
        * 입력 데이터가 Query와 얼마나 관련이 있는지에 대한 수치.
        * 구하는 방법에 따라 어탠션 매커니즘의 종류가 결정.
        * 내적, 스케일드 내적 등
    * 어탠션 웨이트 : 입력 단어에 대한 중요도.
        * 어탠션 스코어를 소프트맥스 함수에 넣는다.
    * 컨텍스트 벡터 : 어탠션 웨이트와 value의 행렬곱 값.
        * 현재 시점에서 주의를 기울여야 하는 부분에 대한 요약.
        * 다음 시점의 모델에 입력으로 제공.
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