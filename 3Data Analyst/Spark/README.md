# Spark

## `[스파크 개요]`

### [APACHE Spark]
* 분산 클러스터링 컴퓨팅 오픈소스 프레임워크.
* 대규모 데이터 처리용으로 설계됐다.
* 계산 부하를 여러 노드에 분담 병렬 처리한다.
* 구조: cluster manager, driver process, executors
* cluster manager
    * 사용 가능한 자원 파악한다.
    * 데이터 처리 작업을 관리하고 조율한다.
    * 사용자가 스파크 어플리케이션을 제출하는 곳 이다.
* driver process
    * 클러스터 노드 중 하나 이다.
    * 드라이버 프로그램의 명령을 executor에 할당한다.
    * 할당을 위해 분석, 배포, 스케쥴링 진행한다.
    * spark session: 스파크 어플리케이션의 통합 진입점
* executors
    * 드라이버 프로세스가 할당한 작업을 수행한다.
    * 진행 상황을 다시 드라이버 노드에 보고한다.
<br><br>

### [스파크의 데이터 처리 방식]
* partition
    * executor가 병렬로 작업을 수행하도록 하는 단계이다.
    * 파티션이라는 청크 단위로 데이터를 분할한다.
    * 클러스터의 물리적 머신에 존재하는 행의 집합이다.
    * 하나의 전체 데이터 -> 파티션 나누기 -> 각각에 executor n개 할당
* transformation
    * 데이터 변경을 원할 때 변경 방법을 알려주는 단계이다.
    * 논리적 실행 계획 '만' 세운다.
    * 실제 연산은 나중에 액션 단계에서 한다.
* lazy evaluation
    * 연산 명령을 받았을 때 즉시 데이터를 수정하지 않는다.
    * 데이터에 적용할 트랜스포메이션 자체만 실행한다.
    * (데이터를 넣지 않고 함수만 미리 계산한다.)
    * 액션 전까지 전체 데이터 흐름을 최적화한다.
* action
    * 실제 연산을 수행하기 위한 사용자 명령이다.
    * 최종 결과를 계산하고 출력하도록 지시한다.
* catalyst
    * 트랜스포메이션을 적용할 때 논리 계획이 담긴 트리 그래프를 먼저 만든다.
    * 로지컬 옵티마이저에 의해서 최적의 논리를 만들고 데이터를 반환한다.
    * (어떤 순서로 계산해야하는지 촤적화한다.)
    * 따라서 더 빠른 계산을 할 수 있다.
    * (ex. 인메모리 연산보다 네트워크 연산이 느리므로 더 늦게 진행한다.)
<br><br>

### [Pyspark]
* 파이썬에서 스파크를 사용하게 해주는 api
* 기능
    * SparkSQL 쿼리 사용 가능
    * 데이터 프레임 2차원 구조 지원
    * 판다스와 같은 문법 사용
    * 정적 데이터와 같은 방식으로 계산을 표현
    * MLlib 모델링 가능
<br><br>



## `[스파크 기본]`