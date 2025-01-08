# [은행/ML] 계좌 개설 사기 탐지를 통한 사기 패턴 분석
* `4가지 ML 모델 탐색, LightGBM 선정, 개발 진행`
* ![](https://github.com/user-attachments/assets/9d418cac-829b-4478-8b71-410ed679a7fa)
<br>

## 목차
### 👨‍🏫 개요
### 🧱 데이터 수집 및 전처리
### 💡 EDA 및 시각화
### 🏘️ 군집 추출
### 🤖 머신러닝 모델링
### 📊 결론
### 📚 배운점
<br>



## 👨‍🏫 개요
* __문제 정의__: 
    * 계좌 개설 사기는 재산 손실, 법적 리스크, 고객 신뢰도 감소를 초래한다.
    * 분류 모델링을 통해 계좌 개설 사기를 탐지하고 예방할 필요가 있다.
    * 모델 해석을 통해 사기 패턴을 분석하고 인사이트를 도출한다.
* __기간/인원__: 2024. 10. 24 - 11. 18 (1개월) / 4명
* __예상 결과물__: 
    * 사기거래 분류 모델
    * 사기 예방 해결책
    * 사기 관련 구체적 인사이트
* __주요 역할__:
    * 군집 추출 (데이터 EDA)
    * 머신러닝 모델링 (LightGBM, TabNet)
    * 모델 해석 (shaply value)
<br>



## 🧱 데이터 수집 및 전처리
* __데이터__
    * ![뉼립스](https://github.com/user-attachments/assets/c1296fca-d759-41ed-a4a8-40e304548192)
    * NeurIPS 2022, Bank Account Fraud (BAF) Dataset Suite
    * 1,000,000개 행, 30개 컬럼
    * 사기 비율이 낮은 비대칭 데이터, False (98.9%) / True (1.1%)
    * 저명한 컨퍼런스에서 발표한 데이터셋, 공신력, 실제 기반
    * 비교적 최근에 공개한 데이터셋, 차별성 있는 프로젝트 기획
    * [`데이터 출처 링크`](https://github.com/feedzai/bank-account-fraud)
* __전처리__
    * STEP 1: 명세서 설명과 불일치하는 컬럼 제거 (intended_balcon_amount)
    * STEP 2: 숫자로 구성되었으나 카테고리컬인 컬럼을 분리
    * STEP 3: 머신러닝 학습 시, LabelEncoder 사용하여 카테고리컬 컬럼 인코딩
<br>



## 💡 EDA 및 시각화
* [`소스 코드 (Process 1: 데이터 EDA)`](https://github.com/HiMyNameIsDavidKim/Study/blob/main/6Project/team_project/project_fraud.ipynb)
<br>

### 1. 카테고리컬 데이터 분석
* ![](https://github.com/user-attachments/assets/3be5676c-aafe-4117-9611-9b5c7cc6fbac)
* 평균 사기 비율 (1.1%) 보다 `사기 비율이 높은 컬럼들을 탐색`한다.
* 이 컬럼들을 `고객 군집화에 사용`한다.
<br>

### 2. 뉴머리컬 데이터 분석
* ![](https://github.com/user-attachments/assets/a9194ee1-4f91-461a-b21d-44161cfe5e4a)
* 바이올린 플랏의 형태를 비교하여 `확률분포에 유의차가 있는 컬럼들을 탐색`한다.
* `모델 결과 분석 시 상관관계가 높을 것으로 예상`된다.
<br>



## 🏘️ 군집 추출
* [`소스 코드 (Process 1: 데이터 EDA)`](https://github.com/HiMyNameIsDavidKim/Study/blob/main/6Project/team_project/project_fraud.ipynb)
<br>

### 1. 군집 추출
* ![](https://github.com/user-attachments/assets/f6071a9c-a6ef-4feb-a84c-f4c883ff37bb)
* 사기의 점유율 (36%) 과 사기의 확률 (7%) 이 동시에 높은 `군집 A를 추출`한다.
<br>



## 🤖 머신러닝 모델링
* [`소스 코드 (Process 2: 모델링)`](https://github.com/HiMyNameIsDavidKim/Study/blob/main/6Project/team_project/project_fraud.ipynb)
<br>

### 1. 모델 탐색
* ![](https://github.com/user-attachments/assets/9d418cac-829b-4478-8b71-410ed679a7fa)
* 4가지 ML 모델을 탐색해보고 LightGBM을 최종 선정했다.
<br>

### 2. 모델링
* ![](https://github.com/user-attachments/assets/f294edbb-4d52-4364-98f6-9f5b8f7f6a6d)
* 하이퍼 파라미터 최적화 (1차): 
    * `learning rate, epoch, drop rate를 변경`했다.
    * -> f1 score 개선 (0.24 -> 0.27)
* 언더 샘플링: 
    * 사용한 데이터는 비대칭 데이터이다. (False:True = 93:7)
    * `False 데이터를 랜덤 샘플링 해 70%만 사용`한다.
    * -> f1 score 개선 (0.27 -> 0.54)
* 하이퍼 파라미터 최적화 (2차): 
    * `learning rate, num leaves, threshold, epoch 변경`했다.
    * -> f1 score 개선 (0.54 -> 0.88)
* __중간 결과 (군집 A):__
    * 군집 A의 사기 3918개 중에 `81.1% 검출`했다. (3178개)
    * 전체 fraud, 11029개 중에 28.8% 검출한 것이다.
<br>



## 🏘️ 군집 추출
* [`소스 코드 (Process 3: 데이터 EDA)`](https://github.com/HiMyNameIsDavidKim/Study/blob/main/6Project/team_project/project_fraud.ipynb)
<br>

### 2. 2차 군집 추출
* ![](https://github.com/user-attachments/assets/dd38dc20-097d-444d-92df-0038eb4e4722)
* 사기의 점유율 (59%) 과 사기의 확률 (2%) 이 동시에 높은 `군집 B를 추출`한다.
<br>



## 🤖 머신러닝 모델링
* [`소스 코드 (Process 4: 모델링)`](https://github.com/HiMyNameIsDavidKim/Study/blob/main/6Project/team_project/project_fraud.ipynb)
* [`소스 코드 (Process 5: 결과 해석)`](https://github.com/HiMyNameIsDavidKim/Study/blob/main/6Project/team_project/project_fraud.ipynb)
<br>

### 3. 2차 모델링
* ![](https://github.com/user-attachments/assets/103ec1be-994b-4547-9c21-e0570af1160e)
* 언더 샘플링: 
    * 사용한 데이터는 비대칭 데이터이다. (False:True = 98:2)
    * `False 데이터를 랜덤 샘플링 해 20%만 사용`한다.
    * -> f1 score 개선 (0.25 -> 0.49)
* 하이퍼 파라미터 최적화 (2차):
    * `learning rate, threshold, epoch 변경`했다.
    * -> f1 score 개선 (0.49 -> 0.74)
* __중간 결과 (군집 B):__
    * 군집 B의 사기 6545개 중에 `83.6% 검출`했다. (5472개)
    * 전체 fraud, 11029개 중에 49.6% 검출한 것이다.
* __종합 결과 :__
    * 군집 A, B를 종합하여 `전체 사기 11029개 중에 78.4%를 검출`했다.
<br>

### 4. 모델 평가
* ![](https://github.com/user-attachments/assets/07a43744-a331-4aeb-a9fe-9b20f4eb0345)
* ROC curve와 cumulative gain curve 분석을 진행한다.
* `높은 분류 성능과 학습 타당성 확인`을 할 수 있다.
<br>

### 5. 모델 해석
* ![](https://github.com/user-attachments/assets/85f7899a-7eeb-4848-bb47-e86613ee1048)
* 모델의 feature importance와 shaply value 분석을 진행한다.
* `허위정보, 자동화, 소득이 중요하게 작용`하는 점을 볼 수 있다.
<br>

### 5. 레시피 도출
* ![](https://github.com/user-attachments/assets/d9726bec-2721-4677-8ed0-260d2784a1fc)
* Top 5 feature 학습 후 rule extraction으로 레시피를 도출한다.
* `주의 고객 집단 추출 후 모니터링`을 진행한다.
<br>



## 📊 결론

### 1. 계좌 개설 사기 탐지에 효과적인 분류 모델 개발
* 전체 사기 계좌 11029개 중에 78.4%를 검출했다.
* `연간 전체 피해금액 1,080억 중 847억원의 손실 감소 예상 (출처: 2021년 금감원)`
<br>

### 2. 사기 패턴 분석 및 인사이트
* 사기 패턴: 허위 주소와 인적사항 사용, 자동화 프로그램 사용, 소득이 높은 경우
* 인사이트: 정보 인증 강화, 자동화 차단, 고소득 고객 모니터링 필요
* 주요 feature: 집전화, 이름 메일 유사도, 디바이스 OS, 세션 정보, 신청 속도
* `사기를 사전에 예방하여 리스크 방지. (재정적 손실, 법적 책임 등)`
<br>



## 📚 배운점
* __시각화에서 한눈에 집약적인 데이터를 표현하였는가?__
    * `다차원을 고려하여 한번에 많은 정보와 인사이트`를 얻을 수 있는지 유념했습니다.
* __머신러닝 모델 별 특징을 알고 있는가?__
    * `TabNet 모델링 실패 원인 분석을 통해 TabNet의 특징과 파라미터를 더 공부`했습니다.
        * TabNet 논문: 어텐션 레이어를 사용(=대용량 반복 학습 필요), raw data를 넣는 것을 권장
        * 회사 수준의 대용량 데이터가 아니였고 짧은 시간 안에 학습하기 힘든 모델
        * 경험과 노하우가 필요한 하이퍼 파라미터(cat_dim, n_d) 가 있어 숙달이 필요
    * `LightGBM 모델링을 통해 모델의 특징과 파라미터에 대한 경험과 지식`을 쌓았습니다.
        * leaf-wise 파라미터를 집중 조절, XGBoost에 비해 대용량 데이터에 적합
        * 데이터의 불균형이 있을 경우에는 언더 샘플링, 오버 샘플링을 활용하여 해결
* __전문적인 모델 해석을 했는가?__
    * 처음에 feature importance만 했으나 부족하다고 생각하여 자료조사를 했습니다.
    * `Shaply value 분석과 Rule extraction에 대하여 공부하고 프로젝트에 적용`했습니다.
<br>




