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



