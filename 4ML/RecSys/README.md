# Recommendation System
* 추천시스템
<br><br>



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

### [우리의 구축 목적]
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



## [Feast]

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




