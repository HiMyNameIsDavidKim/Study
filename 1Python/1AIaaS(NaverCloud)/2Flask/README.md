# 작업 순서 메모

## `[데이터 분석 모델링]`
* 개발 순서 : 이닛(메뉴 추가) -> 뷰(알고리즘 순서 로직) -> 모델(세부 알고리즘 개별 구현)
* 실행되는 순서는 개발 순서의 역순이다. 모델 -> 뷰 -> 이닛
* 기본세팅
    * 1.데이터셋 다운로드 -> 디렉토리 저장
    * 2.모델, 뷰, 템플릿 -> 패키지에 파일 생성
    * 3.데이터셋 -> 패키지에 파일 생성 -> 클래스와 IO 생성
    * 4.모델 : 데이터셋 불러오기, 기본 함수 선언
    * 5.데이터셋 : 게터 세터 선언
    * 6.이닛파일 : 작성(While문)
    * 7.뷰 : 데이터셋 불러오기, 모델 불러오기, 기본 함수 선언
    * 8.템플릿 : 데이터셋 불러오기, 모델 불러오기, 이닛 메서드에 엔트리
    * 9.모델 : 뉴모델 메서드 작성(csv파일 리딩)
* 시각화
    * 1.템플릿 : 플랏하는 메서드 작성
    * 2.이닛파일 : 1번에 플랏 작동시키기
* 전처리
    * 1.뷰 : 모델링 메서드 작성
    * 2.뷰 : 프리프로세스 메서드 작성
    * 3.이닛파일 : 2번에서 작동하도록 한다.
    * 4.모델 : 크리에이트 트레인, 크레에이트 레이블, 드랍 피쳐 메서드 작성
    * 5.모델 : feature들 모두 숫자로 변경. (+추가 feature 생성)
    * 6.뷰 : 프리프로세스 메서드 추가 작성(feature관련)<br><br>