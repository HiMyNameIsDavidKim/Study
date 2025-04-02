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




