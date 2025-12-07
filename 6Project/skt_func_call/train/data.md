# 데이터셋 분석

## 펑션콜 구성
* <function_XX>()<end>
* XX에 코드명이 들어가는 구조
* () 사이에 하이퍼 파라미터가 들어감
* 한번에 2개 이상의 펑션콜을 할 때 ;를 사용함

## 펑션콜 스키마
* MO: 날씨 질문
* IO: 공기질 질문
* PG: 청정기능 작동
* KI: 복귀 명령
* FF: 청정모드 가동+장소
* WN: 밝기 조절, 밝기 상태 확인
* ZV: 음량 조절
* NK: 풍속 조절, 풍속 상태 확인
* BP: AI모드 가동
* QD: 감지 기능 조절
* GQ: 음성 변경
* JS: 설정 답변 기능
* MV: 음소거 작동, 상태
* IH: 스캐닝 청정 기능
* HG: 대기화면 설정
* NN: UV LED(살균기능)작동유무
* EW: 온도 단위 변경
* SC: 공기질 상태 작동유무
* HS: 언어 변경
* QT: 음성인식 기능
* PC: 청소방법 질문
* EN: 기능문의
* GN: 프라이버시 기능 작동
* HW: 과학 관련 질문
* YA: 운행기능 작동
* SB: 정보 문의(외부)
* SV: 정보 문의(기능)
* ZX: 매너모드 가동
* BS: 고스트모드 가동
* DW: 주의사항
* JJ: 배터리 상태
* CS: 청정기 관련 문의
* EF: 전체 이동공기청정
* FR: 방향전환 (내 쪽)
* CE: 청정 결과
* GV: 맥박 기능
* CK: Follow 기능
* ID: 청정기 작동여부
* UJ: 필터상태 확인
* XO: 오류내역
* UY : 에러코드 설명

## 하이퍼파라미터 스키마
* timeframe: timeframe 1(내일), 2(주말), 3(월) ~ 9(일)
* location: 0(here)
* type: 설명 관련 타입 (int)
* enable: 모드 ON/OFF, (true/false)
* get: 상태 설정, (true/false)
* position: 위치, 스트링 입력, position=""나만의비밀룸""
* brightness: 밝기 5단계(0~100%), brightness 1(20%), 상태 같이 입력(get=ture)
* volume: 음량 5단계(0~100%), volume 2(40%), 상태 같이 입력(get=ture)
* speed: 속도 4단계, 줄이기도 가능
* gender: 목소리 성별 (1: 여성, 2: 남성, -1: 스왑)
* theme: 대기 화면 테마 (0: 기본, 2: 공기질, -1: 스왑)
* mute: 음소거 ON/OFF, (true/false)
* move: 이동 3단계, (0: 정지, 1: 일시정지, 2: 이동)
* scan: 스캐닝 청정 ON/OFF, (true/false)
* action: 고정 공기 청정 (1: 고정 공기 청정)

## 펑션콜-하이퍼파라미터 매핑
| Function | 하이퍼파라미터 |
|---|---|
| MO | timeframe, location |
| IO | timeframe, location |
| PG | - |
| KI | - |
| FF | position |
| WN | brightness, get |
| ZV | volume, get |
| NK | speed, get |
| BP | enable, type, get |
| QD | type, get |
| GQ | gender, get |
| JS | type |
| MV | mute, get |
| IH | scan, get |
| HG | theme, get |
| NN | enable, get |
| EW | type, get |
| SC | enable, get |
| HS | type |
| QT | enable, get |
| PC | type |
| EN | type |
| GN | enable, get |
| HW | type |
| YA | move |
| SB | type |
| SV | type |
| ZX | enable |
| BS | enable |
| DW | type |
| JJ | - |
| CS | type |
| EF | action |
| FR | - |
| CE | - |
| GV | - |
| CK | - |
| ID | get |
| UJ | - |
| XO | - |
| HI | type |
| KP | type |
| UY | - |
