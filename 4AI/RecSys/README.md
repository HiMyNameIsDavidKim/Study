# Recommendation System

## `[레퍼런스]`

### [캐글]
* [`T아카데미 기초 모델 구현`](https://www.kaggle.com/datasets/chocozzz/t-academy-recommendation2/code)
* [`CF 아키텍처 베이스라인`](https://www.kaggle.com/code/jamesloy/deep-learning-based-recommender-systems)
<br><br>



## `[Metric]`
* 여기서 관심은 클릭으로 하는 것이 좋다.
* 순서 미포함
    * Precision@K: (유저 관심 아이템) / (추천 아이템 K개)
    * Recall@K: (추천 아이템 중 정답) / (유저 관심 아이템 전체)
* 순서 포함
    * CG@K: Σ(rel(i))
        * Cumulative Gain
        * rel(i): int, 유저와 특정 아이템의 관련도, (주로 별점 사용)
        * 별점이 없다면 클릭으로 하는 것도 고려한다.
    * DCG@K: Σ(rel(i)/log(i+1))
        * Discounted CG
        * 추천 순서가 뒤로 갈수록 분모가 커진다.
    * IDCG@K: Σ(rel(i)_opt/log(i+1))
        * Ideal DCG
        * 가장 이상적인 DCG 값 or 최적화된 DCG 값이다.
    * nDCG@K: DCG@K/IDCG@K
        * Normalized DCG
        * 가장 이상적인 DCG 대비 현재 DCG, 정규화된 값이다.
        * 0에서 1 사이로 정규화된다.
    * HR@K: (적중 유저) / (전체 유저)
        * Hit Rate
        * 유저 관심 아이템 중 1개를 제외한다.
        * 나머지 아이템으로 추천 시스템을 학습한다.
        * 유저 별로 K개 아이템을 추천하고 제외한 아이템이 포함되면 Hit로 간주한다.
    * AP@K: 1/m Σ(Pre@i * rel(i))
        * Average Precision
        * m: 유저 관심 아이템 전체
        * rel(i): bool, i번째 추천 아이템에 대한 관심 여부
    * MAP@K: 모든 유저에 대한 AP@K의 평균
        * Mean AP
* 평점 예측
    * MAE, RMSE 사용
<br><br>



## `[Feature Store]`
* AI 시스템의 피처를 관리하는 중앙 집중식 저장소.
* 추론 과정에 필요한 수많은 데이터들을 제공하는 역할을 한다.
* AI 데이터 파이프라인을 효율적으로 관리한다.
<br><br>

### [레퍼런스]
* [`피처 스토어 구조 정리`](https://zzsza.github.io/mlops/2020/02/02/feature-store/)
* [`회사별 피처 스토어 소개`](https://www.featurestore.org/)
* [`리디 테크 블로그`](https://ridicorp.com/story/ridi-personalization-system-feature-store/)
* [`하이퍼커넥트 유튜브`](https://www.youtube.com/watch?v=_tXV_l581KI)
* [`토스 유튜브`](https://www.youtube.com/watch?v=-u3rhd7k2JQ)
* [`카카오 유튜브`](https://www.youtube.com/watch?v=r1ELaD1DiU0)
* [`당근 테크 블로그`](https://medium.com/daangn/%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EC%8B%AC%EC%9E%A5-feature-store-%EC%9D%B4%EC%95%BC%EA%B8%B0-1-75ffee8ccacd)
<br><br>

### [핵심 기능]
* 피처 관리: 피처 생성, 저장, 버전 관리 및 문서화를 일관적으로 수행한다.
* 데이터 일관성: 훈련과 서빙 환경 간의 피처 불일치를 방지한다.
* 재사용성: 팀 전체에서 표준화된 피처를 공유하고 재사용한다.
* 확장성과 유연성: 일괄적으로 실험 환경을 빠르게 변경할 수 있다.
* 실시간성: 일반적인 웨어하우스와 다르게 (준)실시간으로 피처를 업데이트하고 서빙한다.
<br><br>

### [구성 요소]
* 온라인 스토어: 실시간 예측을 위한 저지연 데이터 제공 (키-값 저장소)
* 오프라인 스토어: 훈련을 위한 대용량 피처 데이터 저장 (데이터 웨어하우스)
* 피처 파이프라인: 원시 데이터를 피처로 변환하는 프로세스 관리
<br><br>

### [대표 솔루션]
* Feast (오픈소스)
* Hopsworks (오픈소스)
* Tecton
* AWS SageMaker
* GCP Vertex AI
<br><br>

### [일반적인 구축 목적]
* feature의 변환을 한 곳에서 일관되게 한다.
* 다양한 저장소의 데이터를 일관된 스키마와 파이프 라인으로 통합한다.
* 피처와 변환 로직의 일관성, 최신성, 정합성을 유지한다.
* 한번 만들어둔 피처를 여러 모델에서 재사용 한다.
<br><br>

### [주의 사항]
* 독립된 파이프라인 구성
    * 파이프라인 간의 강한 결합은 새로운 기능 도입 시 문제를 야기한다.
    * 한 파이프라인의 문제가 전체 시스템에 연쇄적 영향을 미친다.
* 데이터 모듈화 및 계층화
    * 데이터를 4단계로 구분하고 명칭 통일
        * 원시 데이터: 가공되지 않은 데이터. DB나 빅쿼리에서 직접 추출한 것.
        * 원천 데이터: 원시 데이터를 전처리한 데이터. 기본 클리닝과 정규화.
        * 피처 데이터: 원천 데이터를 세분화하여 가공한 데이터.
            * Lv 1: 모델의 인풋.
            * Lv 2: 모델의 피처 변환 후 아웃풋.
        * 추천 데이터: 피처 데이터를 서빙될 수 있는 형태로 가공한 데이터.
<br><br>

### [피쳐 내용 예시]
* azar::history:
    * feature_type: 큰 타입
    * Owner: 관리자
    * schema: 
        * user_id: 
            * type: Text
            * is_key_field: True
        * gender: 
            * type: Text
            * description: ""
            * default_value: ""
<br><br>



## `[Feast]`

### [레퍼런스]
* [`공식 문서`](https://docs.feast.dev/getting-started/quickstart)
* [`공식 문서 번역`](https://heon28.tistory.com/16)
* [`설명 및 실습, 2024`](https://ministop.kr/17)
* [`설명 및 실습, 2023`](https://d-yong.tistory.com/116)
* [`설명 및 실습, 2021`](https://dailyheumsi.tistory.com/265)
* [`스노우플레이크 테크 블로그`](https://medium.com/snowflake-korea/feast%EC%99%80-snowflake%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-al-ml-feature-store-%EA%B5%AC%EC%B6%95-e4e09bcb0aeb)
* [`쿠팡 테크 블로그`](https://medium.com/coupang-engineering/%EC%BF%A0%ED%8C%A1%EC%9D%98-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%ED%94%8C%EB%9E%AB%ED%8F%BC%EC%9D%84-%ED%86%B5%ED%95%9C-ml-%EA%B0%9C%EB%B0%9C-%EA%B0%80%EC%86%8D%ED%99%94-de29804148bb)
<br><br>

### [용어 정의]
* (오프라인 스토어, offline data 저장, historical feature)
* (온라인 스토어, online data 저장, online feature)
* data producer: feast를 호출하는 객체, 파이프라인이나 추천 서빙 서버.
* client: feast 입장에서 클라이언트는 data producer.
* 리퀘스트 소스: 모델 서빙 시점에 실시간으로 제공되는 데이터 소스.
* 스트림 소스: 지속적으로 업데이트되는 실시간 데이터 소스. (kafka, ...)
* 배치 소스: 주기적으로 처리되는 대용량 데이터 소스. (빅쿼리, parquet, ...)
* 레지스트리: 선언한 피처 뷰, 엔터티, 데이터 소스 등의 정의가 저장된 파일.
<br><br>

### [주요 기능]
* 오픈소스로 파이썬 SDK를 통해 사용할 수 있다.
* features, entities, sources 등을 정의할 수 있다.
* 오프라인 저장소, 온라인 저장소에 저장해둔 feature를 사용할 수 있다.
* feature를 탐색할 수 있는 UI를 제공한다.
* feature 확인 및 업데이트 할 수 있는 CLI 도구를 제공한다.
* 직무 별 활용
    * Data Scientist: 피처를 쉽게 정의, 저장, 검색. 모델 설계에만 집중.
    * MLOps: DS가 스스로 feature 관리하므로 유지 관리에 집중.
    * Data Engineers: 다양한 저장소에 대한 추상화를 제공.
    * AI Engineers: fine-tuning 및 성능 최적화 시간 단축.
* 다른 툴과의 비교
    * (vs ETL): 파이프라인의 목적 외에도 저장소로 기능한다.
    * (vs 데이터 오케스트레이션): 함께 통합해서 사용한다.
    * (vs 데이터 웨어하우스): 웨어하우스의 데이터를 사용한다.
    * (vs DB): DB의 데이터를 사용한다.
<br><br>

### [부족한 기능]
* 온라인 저장소 (DB) vs 오프라인 저장소 (빅쿼리) 동기화 문제가 있다.
    * 온라인 데이터로 오프라인 데이터를 동기화할 수 없다. (단방향 동기화)
* 온라인 저장소 실시간 업데이트가 느리다.
* 일부 온라인 저장소를 지원하지 않는다. (ex. 자체구축DB)
* API가 있긴 하지만 공식 SDK가 파이썬만 존재한다.
<br><br>

### [architecture, 구조]
* 그림 참고
* Push Model
    * 다양한 소스에서 데이터를 받아 online store로 피처를 push (저장) 한다.
    * low-latency로 실시간으로 데이터를 제공한다.
* Feature Transformation Engine
    * 리퀘스트 소스나 스트리밍 소스에 대한 피처 변환을 지원한다.
    * 향후 배치 소스에 대한 피처 변환을 지원할 예정이다.
* Write Pattern
    * 적재하는 방법에 대한 패턴이다.
    * 커뮤니케이션 패턴: data producer가 feast로 데이터를 주는 패턴.
    * 피처 값 계산 패턴: 사전 계산, 실시간 계산, 혼합 사용.
* Role-Based Access Control (RBAC)
    * 조직 내 유저별 접근 제한이 가능하다.
    * 피처를 함부로 변경할 수 없도록 하여 보안과 무결성을 제공한다.
<br><br>

### [concept, 개념]
* 그림 참고
* Project
    * infrastructure 레벨의 객체.
    * (1 피처 스토어 = 1 프로젝트)
    * 서로 다른 프로젝트는 피처를 교환할 수 없다.
    * (RDBMS의 DB와 역할이 유사하다.)
* Entity
    * 의미적으로 연결된 피처들의 집합.
    * 각 엔터티 별로 특정 도메인(주소)에 할당시켜 사용한다.
    * (RDBMS의 PK와 역할이 유사하다.)
    * name: 엔티티 식별 이름.
    * join_key: 해당 엔티티의 PK가 되는 컬럼명.
    * ```python
      driver = Entity(name='driver', join_keys=['driver_id'])
      ```
* Data ingestion
    * Data source
        * 데이터 웨어하우스 같은 소스에 저장된 데이터를 수집한다.
        * 기본적으로 스트림 데이터는 수집할 수 없다. (일부만 가능)
        * 크게 리퀘스트, 스트림, 배치 소스에서 데이터를 받는다.
        * (RDBMS의 테이블과 역할이 유사하다.)
    * Batch data ingestion
        * `materialize_incremental`: 모든 엔터티에 대해 가장 최근 데이터를 가져오는 명령어, 추가된 데이터만 처리하여 저장소를 업데이트.
        * 스키마가 명시되지 않으면 `apply` 시 Feast가 추론해서 작성한다.
    * Stream data ingestion
        * Push API 혹은 contrib Spark 프로세서를 사용한다.
* Feature view
    * 각종 데이터 소스에서 정의된 Feature 들의 논리적인 집합.
    * feature view의 종류에 따라 피처 변환을 포함할 수도 있다.
    * (RDBMS의 뷰와 역할이 유사하다. 각종 테이블에서 뷰를 따오는 것.)
    * 하나의 트레이닝 데이터셋을 위해 여러 feature view가 필요할 수 있다.
    * 타임스탬프가 없으면 에러나기 때문에 더미라도 주입해야 한다.
    * 스키마를 적지 않으면 feast가 추론해서 적는다.
    * 구성 요소
        * 이름
        * data source
        * 0개 이상의 entity
        * (Optional, 권장) feature에 대한 스키마 (없으면 추론)
        * (Optional, 권장) 메타데이터 (관리자, 설명, 사용컬럼, 버전, 수정날짜 등)
        * (Optional) TTL, 얼마나 과거까지 조회할 것인지
    * ```python
      driver_stats_fv = FeatureView(
          name="driver_activity",
          entities=[driver],
          schema=[
              Field(name="trips_today", dtype=Int64),
              Field(name="rating", dtype=Float32),
          ],
          source=BigQuerySource(
              table="feast-oss.demo_data.driver_activity"
          )
      )
      ```
* Feature service
    * 하나 이상의 feature view를 조합한 feature의 논리적인 집합.
    * (1 AI 모델 = 1 feature service)
    * ```python
      # Feature service 객체 정의
      driver_stats_fs = FeatureService(
          name="driver_activity",
          features=[driver_stats_fv, driver_ratings_fv[["lifetime_rating"]]]
      )

      # Feature store 초기화
      feature_store = FeatureStore('.')

      # Feature service 객체 반환
      feature_service = feature_store.get_feature_service("driver_activity")

      # 1) Feature 조회 from online store
      features = feature_store.get_online_features(
          features=feature_service, entity_rows=[entity_dict]
      )

      # 2) Feature 조회 from offline store
      feature_store.get_historical_features(features=feature_service, entity_df=entity_df)
      ```
* 데이터셋
    * 훈련에 필요한 historical retrieval로 이루어진 row의 집합.
    * feature view의 조인을 통해 생성된다.
    * (vs Feature view)
        * feature view는 데이터 스키마 및 데이터 소스에 대한 데이터를 포함한다.
        * dataset은 이러한 데이터 소스에 대한 쿼리 후 실체화된 데이터를 의미한다.
    * (vs Data source)
        * data source는 dataset의 인풋으로 사용된다.
        * 하나의 dataset을 위해 1개 이상의 data source를 사용한다.
<br><br>

### [추가 기능 정리]
* 동적 피처 사용
    * Retrieving features
    * 훈련과 추론에 시간대가 다른 피처를 사용할 수 있다.
    * entity key와 timestamps를 같이 사용하여 구현한다.
* 피처 변환
    * 데이터를 변환하여 새로운 피처를 만들어 사용할 수 있다.
    * on_demand_feature_view() 함수를 사용한다.
* 스트림 소스 피처 사용
    * 기존 feature view는 배치 소스만 접근 가능하다.
    * 스트림 소스에 접근하기 위해서는 전용 함수를 사용한다.
    * stream_feature_view() 함수를 사용한다.
* 피처 반환
    * feature retrieval, 피처를 반환하는 패턴.
    * 트레이닝 데이터셋 생성: get_historical_features()
    * 배치소스에서 오프라인 피처 검색: get_historical_features()
    * 실시간 모델을 위한 온라인 피처 검색: get_online_features()
* 이벤트 타임 스탬프
    * featrue view의 데이터 소스에서 해당 이벤트가 발견 또는 생성된 timestamp
    * point-in-time 조인 시 사용되고 Entity rows의 최신 행을 유지하는데 사용한다.
* Point-in-time joins
    * feature view들의 시간별 JOIN 작업을 매우 쉽게 사용할 수 있다.
    * (ex. TTL을 2시간으로 설정해 2시간 내 가장 최신 데이터를 JOIN)
    * get_historical_features()에서 자동으로 수행한다.
* Push source
    * 실시간으로 온라인 스토어와 오프라인 스토어에 피처를 푸시할 수 있다.
    * 푸시 소스는 여러 피처 뷰에 동시에 사용할 수 있다.
    * 푸시 소스에 데이터가 푸시되면 연동된 모든 피처 뷰에 피처 값이 적재된다.
    * 하지만 여전히 (온라인 스토어 -> 오프라인 스토어) 저장은 불가능 하다.
<br><br>

### [component, 요소]
* Functionality, 기능
    * create features: 배치/스트림 피처를 만들 수 있다.
    * feast apply: 버전 관리된 feature repo를 배포하여 레지스트리를 영구 저장한다.
    * feast materialize: (오프라인 스토어 -> 온라인 스토어) 피처를 업로드 한다.
    * model training: 학습 파이프라인을 시작해 학습 데이터셋을 반환한다.
    * get historical features: 학습 파이프라인에서 피처 리스트와 엔터티 df를 반환한다.
    * deploy model: 모델 서빙 시스템에 학습된 모델을 배포한다.
    * prediction: 백엔드에 요청하여 모델 서빙 시스템으로부터 예측값을 받는다.
    * get online features: 온라인 서빙 서비스에 온라인 피처를 요청한다.
* component, 요소
    * 관계도 그림 참고
    * feast registry: 피처 스토어에 저장된 피처 정의를 저장하는 저장소.
    * feast python SDK/CLI: 유저가 바라보는 곳.
    * stream processor: 스트림 데이터를 온라인/오프라인 스토어에 저장하는 객체.
    * batch materialization engine: (오프라인 스토어 -> 온라인 스토어) 데이터를 로드하는 엔진.
    * online store: 각 엔터티 별로 최신 피처 값만 저장하는 저장소.
    * offline store: feast에 수집된 배치 데이터를 저장하는 저장소. (쿼리만 저장)
    * Authorization manager: 권한 토큰을 감지하여 권한 및 정책을 관리하는 매니저.
<br><br>

### [feast registry]
* 모든 피처 정의 및 메타 데이터들을 중앙에서 관리하는 카탈로그.
* 선언한 Feast 객체들 (ex. 피처 뷰, 엔터티, 데이터 소스 등)도 저장한다.
* 레지스트리는 apply, list, retrieve object, delete object 같은 메서드를 제공한다.
* 파일 기반 또는 SQL 기반으로 구현할 수 있다.
* 프로그래밍으로 레지스트리 지정하기
    * ```python
      repo_config = RepoConfig(
          registry=RegistryConfig(path="gs://feast-test-gcs-bucket/registry.pb"),
          project="feast_demo_gcp",
          provider="gcp",
          offline_store="file",
          online_store="null",
      )
      store = FeatureStore(config=repo_config)
      ```
* yaml 파일에서 레지스트리 지정하기
    * ```yaml
      project: feast_demo_aws
      provider: aws
      registry: s3://feast-test-s3-bucket/registry.pb
      online_store: null
      offline_store:
          type: file
      ```
<br><br>

### [offline store]
* 데이터 소스에 저장된 historical 피처를 작업할 인터페이스.
* 다양한 구현체가 있다. (ex. 파일, 빅쿼리, 스노우플레이크, ...)
* 구현체의 종류는 하나만 가능하다. (빅쿼리와 파일 혼용 불가능)
* yaml 파일에서 오프라인 스토어 지정하기
    * ```yaml
      project: my_project
      registry: data/registry.db
      provider: local
      offline_store:
          type: bigquery
      ```
<br><br>

### [online store]
* 데이터 소스에서 materiaize 커맨드로 로드된 online 피처를 작업할 인터페이스.
* 다양한 구현체가 있다. (ex. MySQL, Redis, 스노우플레이크, ...)
* feast materialize 커맨드 입력 시 최신 피처 값만 저장한다.
* yaml 파일에서 온라인 스토어 지정하기
    * ```yaml
      project: my_project
      registry: data/registry.db
      provider: local
      online_store:
          type: sqlite
          path: data/online_store.db
      ```
<br><br>

### [batch materialization engine]
* (오프라인 스토어 -> 온라인 스토어) 데이터를 로드하는 엔진.
* AWS Lambda에 위임하여 작업할 수도 있다.
* yaml 파일에서 엔진 지정하기
    * ```yaml
      project: my_project
      registry: s3://my_bucket/registry.db
      provider: local
      materialization_engine:
          type: local
      ```
<br><br>

### [Provider, 환경]
* 피처 스토어 구현에 사용되는 구성 요소들을 조율하는 환경.
* local, aws, gcp 등이 있다.
<br><br>

### [Authorization Manager]
* Feast 서버에서 현재 요청에서 유저의 권한을 관리하는 객체.
* 외부 인증 서비스 (AWS Cognito, Keycloak)의 토큰을 활용할 수 있다.
* 자체적인 인증 토큰 발행 기능은 없다.
<br><br>



## `[ONNX]`
* [`공식 문서`](https://onnx.ai/onnx/intro/concepts.html)
* [`공식 문서 번역`](https://velog.io/@openjr/1.-ONNX-Concepts)
* [`에너자이 테크 블로그`](https://medium.com/@enerzai/onnx-너-누구야-who-are-you-5c1435b997e2)
<br><br>

### [개념]
* Open Neural Network Exchange, AI 모델의 상호 운용성을 위한 오픈 소스 표준. (by MS, Meta)
* AI 프레임워크 간에 자유롭게 변환하고 배포할 수 있도록 중간 표현 형식을 제공한다.
* 신경망을 연산 그래프 형태로 표현하기 때문에 프레임워크에 독립적이다.
* JSON 포맷처럼 ONNX 라는 합의된 AI 모델 포맷이 존재한다고 이해할 수 있다.
* 파이토치, 텐서플로우, 사이킷런, 케라스 등을 모두 ONNX로 변환할 수 있다.
* 기본적으로 DL 모델 변환을 위해 만든 것이지만 ML 모델도 지원한다.
<br><br>

### [연산 그래프]
* computational graph
* 수학적 연산들을 노드와 엣지로 이루어진 그래프.
* 노드 = 덧셈, 곱셈, 함수 등 / 엣지 = 데이터 흐름
<br><br>

### [ONNX Runtime]
* ONNX가 지원하는 다양한 플랫폼에서 효율적으로 실행할 수 있게 해주는 추론 엔진.
* OS, 하드웨어, 개발 언어 등 대부분의 환경에서 모두 구동 가능하다.
* 추론 성능 최적화 기술 (연산자 제거, 융합, 양자화 등)을 지원한다.
* 심지어 브라우저와 모바일에서도 구동할 수 있다.
<br><br>

### [일반적인 구축 목적]
* 배포: 운영 환경에 배포할 때 하드웨어, 운영 체제에 제약이 없고 안정적이다.
* 경량화: 메모리 사용량이 적고 프레임워크 자체가 더 가볍다.
* 속도 개선: ONNX 형식이 추론 속도가 더 빠르다.
<br><br>

### [구조]
* 프로토콜 버퍼
    * ONNX가 모델 구조를 정의하는 방법이다.
    * .onnx 파일이 프로토콜 버퍼로 작성된다.
    * 프로토콜 버퍼: 구글에서 만든 데이터 저장 방식
* 핵심 구성 요소
    * 노드: 개별 연산자를 표현
    * 엣지: 데이터 흐름을 표현
    * 이니셜라이저: 모델 가중치와 상수값
    * 입출력: 모델의 입력과 출력 명세
* 연산자 집합
    * 신경망 레이어와 함수를 표준화된 연산자 집합으로 정의한다.
    * (ex. Convolution, MatMul, Relu, Softmax, BatchNormalization)
* 타입 시스템
    * 스트롱 타입 시스템을 채택해 타입 안정성을 보장한다.
    * 텐서의 shape와 type을 명시적으로 정의한다.
* 메타데이터
    * 모델에 대한 (버전, 저자, 라이선스) 등을 포함할 수 있다.
* 예시
    ```protobuf
    Input: float[M,K] x, float[K,N] a, float[N] c
    Output: float[M, N] y
    
    r = onnx.MatMul(x, a)
    y = onnx.Add(r, c)
    ```
    * 노드: onnx.MatMul(x, a), onnx.Add(r, c)
    * 엣지: x, a, r, c, y
    * 이니셜라이저: a, c 의 가중치
    * 입출력: x, y
    * 연산자: MatMul, Add
    * 타입: float[M, K]
<br><br>

### [장단점]
* 장점
    * __배포__: 운영 환경에 배포할 때 하드웨어, 운영 체제에 제약이 없고 안정적이다.
    * __경량화__: 메모리 사용량이 적고 프레임워크 자체가 더 가볍다.
    * __속도 개선__: ONNX 형식이 추론 속도가 더 빠르다.
    * __상호 운용성__: 프레임워크 간 모델을 교차 사용할 수 있다. (ex. PyTorch → TensorFlow)
* 단점
    * __성능 리스크__: 경량화의 영향으로 모델이 ONNX에서는 동작하지 않거나 낮은 성능을 보일 수 있다.
    * __제한된 연산자__: 최신 연구에서 사용되는 커스텀 연산자나 특수 레이어를 지원하지 않는다.
    * __학습 지원 부족__: ONNX는 추론에 최적화되어 학습 과정의 표현에는 제약이 많다.
<br><br>

### [사용 예시]
* 파이토치 학습 후 오닉스로 변환하는 코드.
    ```python
    torch.onnx.export(
        onnx_model,
        (dummy_input, ),
        onnx_model_path,
        verbose=False,
        export_params=True,
        do_constant_folding=True,
        input_names=["inputs"],
        output_names=["outputs"],
        dynamic_axes={'inputs': {0: 'batch_size'}, 'outputs': {0: 'batch_size'}},
        opset_version=14  # ONNX opset version (adjust as needed)
    )
    ```
* 오닉스로 저장된 모델을 실행하는 코드.
    ```bash
    pip install onnxruntime
    pip install onnxruntime-gpu
    ```
    ```python
    import onnxruntime as ort
    import numpy as np
    
    # ONNX 모델 로드
    model_path = "model.onnx"
    session = ort.InferenceSession(model_path, providers=['CUDAExecutionProvider'])
    
    # 입력/출력 정보 확인
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    input_shape = session.get_inputs()[0].shape
    output_shape = session.get_outputs()[0].shape
    
    print(f"입력 이름: {input_name}, 형태 {input_shape}")
    print(f"출력 이름: {output_name}, 형태 {output_shape}")
    
    # 더미 입력 데이터 생성
    input_data = np.random.randn(1, 768).astype(np.float32)
    
    # 추론 실행
    result = session.run([output_name], {input_name: input_data})
    output = result[0]
    
    print(f"출력 결과: {output}")
    ```
<br><br>

### [주의 사항]
* 파이토치 forward에 for문이나 if문이 있으면 onnx가 매우 느려진다.
<br><br>



## `[Airflow]`
* [`Ref`](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
* [`코드잇 유튜브`](https://youtu.be/LmQhHcueJs0?si=JK0OuaOTnIIYPEZI)
<br><br>

### [기본 개념]
* Airflow
    * 파이썬 기반 오픈소스 워크플로우 관리 플랫폼.
    * 프로그래밍으로 워크플로우를 작성, 예약 및 모니터링할 수 있다.
    * DAG (Directed Acyclic Graph) 구조를 기반으로 작업 간 의존성을 관리한다.
* DAG
    * 방향성 비순환 그래프를 말한다.
    * (DAG 예시)
        * ![DAG](https://github-production-user-asset-6210df.s3.amazonaws.com/112922638/462890436-7718faf3-b9b7-4576-9c7f-d585c9604596.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250706%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250706T082127Z&X-Amz-Expires=300&X-Amz-Signature=b6e9dc5f929173dcde8e266acc919fd8aa85a7dc63706cef15de1873276b7672&X-Amz-SignedHeaders=host)
    * 순환 그래프가 되면 DAG가 아니게 된다.
    * (순환 그래프 예시)
        * ![Cyclic](https://github-production-user-asset-6210df.s3.amazonaws.com/112922638/462890739-3c37104e-054b-4602-9c53-494e856d89f8.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250706%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250706T082224Z&X-Amz-Expires=300&X-Amz-Signature=7269708536d696599c8c15a337e49fe9965d531da55af2508f5b9ebc3170e542&X-Amz-SignedHeaders=host)
* 워크플로우
    * 워크플로우는 DAG로 표현된다.
    * DAG는 Task라고 부르는 개별 작업을 포함한다.
        * (ex. 데이터 가져오기, 분석 실행, 다른 시스템 트리거 등)
    * Task는 종속성과 데이터 흐름을 고려해 정렬된다.
<br><br>

### [구성 요소]
* 필수
    * scheduler: DAG를 주기적으로 실행
    * DAG processor: DAG 파일을 파싱
    * webserver: 사용자 인터페이스 제공
    * DAG files folder: DAG 정의 파일 저장
    * metadata DB: DAG 상태와 실행 기록 저장
* 선택
    * worker: scheduler가 할당한 작업을 실행
    * triggerer: 지연된 작업을 실행 (비동기)
    * plugins folder: 사용자 정의 플러그인 저장
<br><br>

### [Scheduler]
* DAG와 task의 실행 일정을 관리하는 핵심 구성요소.
* DAG 파일을 주기적으로 파싱해 새로운 DAG나 변경사항을 감지한다.
* task의 의존성과 스케줄을 확인하여 실행 가능한 task를 식별한다.
* 실행이 준비된 task 인스턴스를 executor에 할당한다.
* task, worker, executor의 상태를 모니터링하고 메타데이터 DB에 기록한다.
* airflow 전체로 봤을 때 두뇌 역할을 하는 핵심 요소이다.
* `airflow scheduler` 명령어로 간단하게 실행할 수 있다.
* airflow.cfg 파일에 지정된 설정에 따라 동작한다.
* scheduler 장애 시 전체 실행이 중단되기 때문에 고가용성 구성이 매우 중요하다.
<br><br>

### [DAG]
* 워크플로우를 실행하는데 필요한 모든 것을 캡슐화하는 모델.
* 주요 속성
    * `schedule`: DAG 실행 주기
    * `tasks`: worker에서 실행되는 개별 작업들
    * `task dependencies`: 작업이 실행되는 순서와 조건
    * `callbacks`: 작업 완료 후 실행할 작업
* DAG는 태스크 내부 일에 관심이 없고 오직 태스크를 어떻게 실행할지만 관여한다.
* 여기서 어떻게는 실행 순서, 재시도 횟수, 타임아웃 여부 등을 말한다.
* 종속성
    * task 나 operator는 단독으로 존재하지 않고 의존성을 가진다.
    * 이런 종속성을 선언하는 것이 DAG 구조를 구성한다.
    * `>> 및 << 연산자` 를 사용해 task 간의 의존성을 정의한다.
    * (ex1. first_task >> [second_task, third_task])
    * (ex2. third_task << fourth_task)
    * set_downstream()을 사용할 수도 있다.
    * cross_downstream()을 사용하면 task 리스트 간에 설정할 수 있다.
    * chain()을 사용하면 여러 task를 한번에 설정할 수 있다.
    * chain()과 리스트 컴프리헨션을 사용하면 다이나믹하게 설정할 수 있다.
<br><br>

### [DAG Run]
* 특정 시점 DAG의 인스턴스.
* DAG가 실행될 때마다 DAG Run이 생성되고, DAG Run 내 모든 Task가 실행된다.
* 각 DAG Run은 서로 독립적이고 동시에 여러 DAG Run이 실행될 수 있다.
* DAG Run status
    * DAG Run의 현재 상태를 나타내는 속성이다.
    * 상태는 `running`, `success`, `failed`, `skipped` 등으로 표시된다.
* Data interval
    * DAG Run은 작동하는 시간 범위인 data interval이 할당된다.
    * (ex. @Daily 스케줄의 경우, Data interval은 매일 00:00부터 다음날 24:00)
* 외부 트리거
    * DAG Run은 CLI 또는 웹UI를 통해 수동으로 생성할 수도 있다.
    * CLI를 사용해 `airflow dags trigger <dag_id>` 명령을 사용하면 된다.
<br><br>

### [Task]
* 에어플로우에서 실행의 기본 단위.
* Task들은 DAG 내에 배열되고, 실행 순서를 위해 종속성이 설정된다.
* 종류
    * Operator: 사전에 정의된 task의 템플릿
    * Sensor: 외부 이벤트 감지에 특화된 operator의 하위 클래스
    * TaskFlow-decorator @task: 커스텀 파이썬 함수를 task로 변환
    * 내부적으로 모두 BaseOperator의 하위 클래스이다.
    * task와 operator의 개념은 어느정도 겹치는 부분이 있다.
* Relationships
    * task 사용의 핵심은 서로 어떻게 관련되는지 `종속성`을 정의하는 것이다.
    * airflow에서는 이것을 upstream과 downstream으로 표현한다.
    * upstream: 다른 task에 선행하는 task (부모 task)
    * downstream: 다른 task에 후행하는 task (자식 task)
    * task는 모든 upstream task가 성공적으로 완료된 후에만 실행된다.
    * 예외적으로 branching, 일부만 기다리기 등을 사용할 수 있다.
* task는 서로 정보를 전달하지 않으며, 필요할 경우 XCom을 사용해야한다.
* task 인스턴스
    * task의 실행 인스턴스.
    * 상태를 가지는 task의 representaion이다.
    * 상태 종류
        * `none`: 아직 실행 대기열에 추가되지 않음.
        * `scheduled`: scheduler에 의해 실행 대기열에 추가됨.
        * `queued`: Executor에 할당되고 worker를 기다리고 있음.
        * `running`: worker에서 실행 중.
        * `success`: 오류 없이 성공적으로 완료됨.
        * `restarting`: 실행 중에 외부에서 재시작 요청됨.
        * `failed`: 오류 발생으로 실패함.
        * `skipped`: branching 등의 이유로 건너뛰어짐.
        * `upstream_failed`: upstream task가 실패하여 실행되지 않음.
        * `up_for_retry`: 실패했지만 재시도 횟수가 남아 재스케줄링될 예정임.
        * `up_for_reschedule`: reschedule 모드의 센서임.
        * `deferred`: 트리거에 의해 지연됨.
        * `removed`: 실행 이후 DAG에서 제거되어 사라짐.
    * 이상적인 순서: none -> scheduled -> queued -> running -> success
* timeout을 설정해 task에 최대 실행 시간을 설정할 수 있다.
<br><br>

### [Worker]
* task 인스턴스를 받아와 실제로 실행하는 프로세스 또는 스레드.
* executor 타입에 따라 worker의 형태가 달라진다.
* 동시에 실행 가능한 worker의 수는 parallelism 설정으로 제어할 수 있다.
* worker는 task 실행 중 로그를 생성하고 상태를 scheduler에 보고한다.
<br><br>

### [Executor]
* task 인스턴스가 실행되는 매커니즘.
* worker가 task를 실행하는 방법을 정의한다.
* 다양한 executor가 있어서 유연하게 교체할 수 있다.
* airflow.cfg 파일의 [core] 섹션에서 executor를 설정할 수 있다.
* 종류1: 로컬
    * task를 로컬 머신에서 실행한다.
    * 장점: 쉽고 빠르다. 지연 시간이 짧다. 설치 요구 사항이 적다.
    * 단점: 기능에 제약이 있다. scheduler와 리소스를 공유하므로 서로 영향을 준다.
    * LocalExecutor: 소규모 환경에서 가장 간단한 실행 옵션이다.
* 종류2: 원격, 큐/배치
    * task를 원격으로 실행하며, worker 풀을 통해 실행된다.
    * 내부 큐의 task를 redis 큐로 전송하고 worker가 큐에서 task를 가져와 실행한다.
    * 장점: scheduler와 분리로 견고하다. 비용 효율적이다. 지연 시간이 짧다.
    * 단점: task들이 리소스를 두고 경쟁한다. 워크로드 관리가 필요하다.
    * CeleryExecutor: Celery를 사용해 분산 실행한다.
    * BatchExecutor: 대규모 데이터 처리에 적합하다.
* 종류3: 원격, 컨테이너
    * task를 원격으로 실행하며, worker 풀을 통해 실행된다.
    * task가 컨테이너 내에서 즉시 실행된다. (task가 컨테이너로 격리)
    * 장점: task 격리로 안정적이다. 각 task에 맞춤 설정을 할 수 있다.
    * 단점: 컨테이너를 시작할 때 지연 시간이 있다. 쿠버네티스 설정이 필요하다.
    * KubernetesExecutor: 쿠버네티스 클러스터에서 task를 실행한다.
    * EcsExecutor: AWS ECS에서 task를 실행한다.
* 다중 Executor를 사용할 수 있다.
<br><br>

### [구성 요소 요약]
* Scheduler: DAG와 task 의존성 확인, DAG 동기화, 큐에 task 적재, ~~Airflow의 본체~~
* Executor: scheduler가 큐에 적재한 task를 worker에 할당
* Worker: task를 실제로 실행하는 프로세스, 스레드
* Web Server: UI 제공, DAG와 task 모니터링 관리, Flask 기반, HTTP
* Metadata DB: 모든 상태 정보와 메타데이터 저장
* DAG Files Folder: DAG 정의 파일 저장
* Airflow.cfg: Airflow 설정 파일
<br><br>

### [단계1: DAG 폴더 스캔]
* airflow.cfg 파일에 지정된 DAG 폴더 경로가 어딘지 확인한다.
* DAG 폴더를 주기적으로 스캔해 새로운 DAG와 변경점을 확인한다.
* 스캔 과정에서 DAG 파일을 파싱하고 DAG 객체를 생성해 메모리에 저장한다.
* DAG 객체는 DAG의 구조, task 간의 의존성 등을 포함한다.
* 메모리에 저장된 DAG 객체는 이후에 scheduler가 사용한다.
<br><br>

### [단계2: 새로운 DAG와 task 인스턴스 생성]
* 새로운 DAG를 발견하면 DAG에 정의된 task의 실행 일정을 확인한다.
* scheduler가 DAG와 task의 다음 실행 시점을 결정한다.
* 실행 시점이 되면 scheduler는 task 인스턴스를 생성한다.
* 이때 task 인스턴스의 상태는 `none`에서 `scheduled`로 변경된다.
<br><br>

### [단계3: task queue에 task 인스턴스 등록]
* scheduler는 생성된 task 인스턴스를 task queue에 등록한다.
* 이때 task 인스턴스의 상태는 `queued` 상태로 변경된다.
* queue에 있는 task를 executor의 worker가 가져가 실행한다.
* 이때 task 인스턴스의 상태는 `running`으로 변경된다.
* 작업이 완료되면 task 인스턴스의 상태가 `success`로 변경된다.
<br><br>

### [단계4: 메타데이터 DB와 상호작용]
* scheduler는 모든 스케줄링 정보를 메타데이터 DB에 기록한다.
* 예를 들어, DAG와 task 인스턴스의 상태, 실행 기록 등을 저장한다.
* DB에 저장된 정보를 통해 Web Server는 DAG의 상태를 유저에게 보여준다.
* 유저는 웹 UI를 통해 DAG의 실행 상태와 로그를 확인할 수 있다.
<br><br>

### [전체 단계 요약]
* scheduler가 task 인스턴스를 큐에 넣는다.
* executor가 worker에 task 인스턴스를 할당한다.
* worker가 task 인스턴스를 실행한다.
* 실행 결과가 scheduler에 보고된다.
* scheduler가 상태를 메타데이터 DB에 기록한다.
* Web Server의 UI에서 DAG와 task 인스턴스의 상태를 모니터링한다.
<br><br>


### [장단점]
* 장점
    * 코드 기반 워크플로우로 유연성, 재사용성, 버전 관리 (Git)가 가능하다.
    * 내장 오퍼레이터가 많고 AWS, GCP 등 클라우드와 연동할 수 있다.
    * 웹 UI, 상세한 로그, 이메일과 슬랙 알림 기능이 있다.
* 단점
    * Airflow의 개념 이해, DAG 작성과 디버깅에 진입장벽이 있다.
    * 대규모 파이프라인은 메모리와 CPU 사용량이 높다.
    * 실시간 스트리밍에는 제약이 있다. (데이터 전달 이슈, 작업 간 오버헤드)
<br><br>

### [도커를 이용한 설치]
* 도커 설치, 도커 컴포즈 설치
* Airflow 설치
    * ```bash
      # 프로젝트 위치에서 터미널 켜기
      pwd

      # 윈도우의 경우 우분투로 실행
      wsl -d Ubuntu-22.04

      # 2.11.0 버전 설치 (3 버전 설치 안됨)
      curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.11.0/docker-compose.yaml'

      # docker-compose.yaml 파일, AIRFLOW__CORE__LOAD_EXAMPLES: 'false'로 변경

      # airflow 유저 설정
      mkdir -p ./dags ./logs ./plugins ./config
      echo -e "AIRFLOW_UID=$(id -u)" > .env

      # airflow metadata DB 시작
      docker compose up airflow-init

      # airflow 시작
      docker compose up
      ```
* http://localhost:8080 접속해서 로그인
    * (ID: airflow, PW: airflow)
<br><br>

### [프로젝트 구성]
* ```
  airflow-project/
  ├── docker-compose.yml
  ├── dags/
  │   └── simple_tutorial.py  # here
  ├── logs/
  ├── plugins/
  └── .env
  ```
* dags 디렉토리에 파이썬 파일을 넣는다.
* docker compose 컨테이너를 멈춘다.
* docker compose up
* 즉시 실행하기
    * http://localhost:8080, DAG의 우측, 재생 버튼 (Trigger DAG) 클릭
<br><br>

### [간단 예제]
* simple_tutorial.py
* ```python
  from datetime import datetime, timedelta
  from airflow import DAG
  from airflow.operators.python import PythonOperator
  from airflow.operators.bash import BashOperator

  # DAG 기본 설정
  default_args = {
      'owner': 'airflow',
      'start_date': datetime(2024, 1, 1),
      'retries': 1,
      'retry_delay': timedelta(minutes=5),
  }

  # DAG 정의
  dag = DAG(
      'simple_tutorial',
      default_args=default_args,
      description='간단한 Airflow 튜토리얼',
      schedule_interval=timedelta(days=1),
      catchup=False,
  )

  # Task 1: 시작 메시지
  def start_task():
      print("🚀 워크플로우 시작!")
      data = {'users': ['김철수', '이영희', '박민수']}
      print(f"처리할 사용자: {data['users']}")
      return data['users']

  # Task 2: 데이터 처리
  def process_data(**context):
      # 이전 task에서 데이터 가져오기
      ti = context['ti']
      users = ti.xcom_pull(task_ids='start')
    
      print("⚙️ 데이터 처리 중...")
      processed_users = [f"{user}_처리완료" for user in users]
      print(f"처리 결과: {processed_users}")
      return len(processed_users)

  # Task 3: 결과 확인
  def check_result(**context):
      ti = context['ti']
      count = ti.xcom_pull(task_ids='process')
    
      print(f"✅ 총 {count}명의 사용자 처리 완료!")
      return "성공"

  # Task 정의
  start = PythonOperator(
      task_id='start',
      python_callable=start_task,
      dag=dag,
  )

  process = PythonOperator(
      task_id='process',
      python_callable=process_data,
      dag=dag,
  )

  check = PythonOperator(
      task_id='check',
      python_callable=check_result,
      dag=dag,
  )
  
  # Bash 명령어로 완료 메시지
  finish = BashOperator(
      task_id='finish',
      bash_command='echo "🎉 모든 작업 완료!"',
      dag=dag,
  )

  # 실행 순서 설정
  start >> process >> check >> finish
  ```
<br><br>

### [DAG 선언 종류]
* 표준 생성자 (추천)
    * ```python
      import datetime

      from airflow.sdk import DAG
      from airflow.providers.standard.operators.empty import EmptyOperator

      my_dag = DAG(
          dag_id="my_dag_name",
          start_date=datetime.datetime(2021, 1, 1),
          schedule="@daily",
      )
      EmptyOperator(task_id="task", dag=my_dag)
      ```
* with 문
    * ```python
      import datetime

      from airflow.sdk import DAG
      from airflow.providers.standard.operators.empty import EmptyOperator

      with DAG(
          dag_id="my_dag_name",
          start_date=datetime.datetime(2021, 1, 1),
          schedule="@daily",
      ):
          EmptyOperator(task_id="task")
      ```
* @dag 데코레이터
    * ```python
      import datetime

      from airflow.sdk import dag
      from airflow.providers.standard.operators.empty import EmptyOperator

      @dag(start_date=datetime.datetime(2021, 1, 1), schedule="@daily")
      def generate_dag():
          EmptyOperator(task_id="task")

      generate_dag()
      ```
<br><br>


### [주의 사항]
* __pycache__ 때문에 에러가 자주나므로, venv 사용 권장.
* SQLAlchemy 2.0 버전 사용 불가. 1.3.23 버전 권장.
<br><br>

