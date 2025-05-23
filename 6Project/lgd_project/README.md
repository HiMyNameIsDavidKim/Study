# [제조/ML] 애플워치 검사 자동화 알고리즘 설계 및 운영
* `패널 불량 검출 예시 이미지, (Jeong et al., 2021, JID)`
* ![](https://github.com/user-attachments/assets/87bef640-0dc6-4cf1-a79c-71fe4b67cd16)
<br>

## 목차
### 👨‍🏫 개요
### 👨‍🏭 As-is
### 💡 Break-through Idea
### 🤖 To-be
<br>



## 👨‍🏫 개요
* __문제 정의__: 
    * 자동화 검사는 품질 관리, 성능, 속도, 데이터화 측면에서 사람보다 우수하다.
    * 애플워치 검사기에서 데이터를 추출하고 머신러닝을 활용해 자동화한다.
    * 검사 자동화 알고리즘을 설계하여 품질을 개선하고 비용을 절감 한다.
* __기간/인원__: 2021. 12. 10 - 2022. 8. 4 (9개월) / 약 70명
* __예상 결과물__: 
    * 자동화 검사 알고리즘
    * 13종 불량의 검출 레시피
    * 유지 관리 방안
* __주요 역할__:
    * 검출 레시피 도출 (ML rule extraction)
    * 카메라 데이터 일관성 유지 (통계학, C++)
    * 협력업체 및 유관부서 소통 (커뮤니케이션)
* __상세 역할__:
    * LG디스플레이 검사팀 AI빅데이터 직무로 애플워치 검사 완전 자동화 달성.
    * 카메라로 추출한 100개 feature를 머신러닝을 활용해 불량 검출 레시피 도출.
    * 분석을 통한 이상 데이터 제거, 카메라의 일관된 데이터 추출을 위한 방법 도출.
    * 자동화 검사기 협력업체 (7개), 유관부서 (3개), 베트남팀 (2개) 소통 유도.
<br>



## 👨‍🏭 As-is
* ![사람](https://github.com/user-attachments/assets/7c4d7b74-c3e8-4d10-8b55-9bd3542ef75a)
<br>

### 1. 문제점
* (품질) 사람은 일관성 있는 검사가 불가능하다.
* (품질) 사람이 검사할 수 없는 미세한 불량이 있다.
* (공정) 검사 속도가 자동화 알고리즘보다 느리다.
* (공정) 과거 이력이 데이터로 남지 않는다.
<br>

### 2. 자동화 적용 실패 원인 분석
* Feature engineering에 대한 노하우가 없다.
* 머신러닝을 적용하는 방법에 대한 지식이 없다.
* 같은 패널도 카메라 데이터가 일관성 없게 추출된다.
* 이상 데이터를 처리하는 방법을 모른다.
* 자동화 적용 이후 유지 관리에 대한 방법이 없다.
<br>



## 💡 Break-through Idea

### 1. 검출 레시피 도출
* 불량품과 상관성 높은 `주요 feature를 추출`한다.
* 주요 feature로 `머신러닝 rule extraction`을 진행한다.
* 도출된 레시피에 대한 테스트 및 수정을 진행한다.
* 최종 레시피로 불량 검출을 테스트 및 적용한다.
<br>

### 2. 카메라 데이터 처리 개선
* 카메라 데이터 일관성 문제의 원인을 분석한다.
* 평탄도, 포커스 등 `일관성 유지 방안`을 정립한다.
* 이상 데이터 처리에 `통계학 방법론`을 적용해 개선한다.
* `코드 효율성 증대`를 통한 속도를 개선한다.
<br>

### 3. 검출 불가 유형 알고리즘 신규 개발
* 기존과 다른 `신규 feature를 연구하고 추출`한다.
* 창의적 아이디어로 `미사용 데이터를 발굴`한다.
* 신규 불량 발생 시 대응 프로세스 문서화한다.
<br>

### 4. 유지 관리 프로세스 정립
* 카메라 데이터 `일관성 점검 방법을 문서화`한다.
* 신규 불량 수집 및 대응 프로세스를 정립한다.
* 베트남 현지 엔지니어 육성 후 자립 유도한다.
<br>



## 🤖 To-be
* ![알고리즘](https://github.com/user-attachments/assets/0d4473eb-3fb9-4594-af28-34f07e78dc09)
<br>

### 1. 결과 (대외비 생략)
* (품질) 일관성 있는 검사를 진행한다.
* (품질) 검출 불가 유형을 추가로 검출한다.
* (공정) 검사 속도가 사람에 비해 xx% 빠르다.
* (공정) 공정 데이터를 기록하여 지속 활용한다
<br>

### 2. 정량적 성과 (대외비 생략)
* `비용절감`
    * `속도 개선, Capa 상승`으로 xx억 저감.
    * `인원 감축, 인건비 감축`으로 연간 xx억 저감.
* `품질개선`
    * 불량 검출 `F1 score xx% 개선`.
    * 일관된 검사로 `분석 속도 xx% 개선`.
<br>




