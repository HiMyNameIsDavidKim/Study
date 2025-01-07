# [은행/ML] 계좌 개설 사기 탐지를 통한 사기 패턴 분석
* ![]()
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
    * 군집 추출
    * 머신러닝 LightGBM 모델링
    * shaply value를 통한 모델 해석
<br>



## 🧱 데이터 수집 및 전처리
* __데이터__
    * ![뉼립스](https://github.com/user-attachments/assets/e8ff241a-756f-42c8-80f0-e2f7ad6407be)
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
* 사기의 점유율 (36%) 과 사기의 확률 (7%) 이 동시에 높은 군집 A를 추출한다.
<br>



## 🤖 머신러닝 모델링
* [`소스 코드 (Process 2: 모델링)`](https://github.com/HiMyNameIsDavidKim/Study/blob/main/6Project/team_project/project_fraud.ipynb)
<br>

### 1. 모델 탐색
* 
<br>






## 📊 결론
## 📚 배운점



