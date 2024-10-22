# DBeaver

## `[디비버 개요]`

### [디비버 장점]
* 오픈소스 툴
* 다양한 DB 지원
* 직관적 인터페이스
* 쉬운 import
* ERD 그리기 가능
<br><br>

### [초기 환경설정]
* Upper case
    * 윈도우 탭 -> 환경설정 -> 편집기 -> SQL 편집기 -> SQL 포맷
    * keyword case를 Upper로 고치기
* 행번호 표시
    * 윈도우 탭 -> 환경설정 -> 편집기 -> 문서 편집기
    * 행번호 표시 체크
<br><br>

### [자주 쓰는 단축키]
* CMD + ENTER: 현재 쿼리 실행
* CMD + \: 새탭에서 현재 쿼리 실행
* CMD + /: 주석 전환
* CMD + ]: 새 SQL 편집기 열기
<br><br>



## `[디비버 기본]`

### [DB 연결]
* 좌측 상단 플러그 + 모양 클릭
* 새 데이터베이스 연결 -> MySQL 선택
* 비밀번호 입력
* test connection -> connected 확인
* 완료
* 좌측 탭에 localhost 클릭 -> Databases 우클릭 -> DB 생성
* 생성된 DB 우클릭 -> 데이터 가져오기 -> CSV로 가져오기 -> CSV 선택
<br><br>

### [Table 분리 생성]
* 유니크한 고유 키값 정하기 (ex. 사번)
* table create
    * create table로 껍데기 만들기 -> insert into로 넣기
        * CREATE TABLE table2 (col1 int(11), col2 varchar(50));
        * INSERT INTO table2 (SELECT col1, col2 FROM table1);
    * source table로 소싱 -> create (select from )으로 넣기
        * 소싱할 테이블 더블클릭 -> 테이블 좌측상단 우클릭
        * Advanced copy -> 컬럼명 복사
        * CREATE TABLE table2 (SELECT col1, col2, FROM table1);
* DB 더블클릭 -> 엔티티 관계도 확인 가능
* 원하는 키값 db2에서 드래그 앤 db1으로 드랍
<br><br>






