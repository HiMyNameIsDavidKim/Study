# SQL (제로베이스 강의)
<br><br>

## `[MySQL 기초 및 분법]`

### [Database 정의]
* 여러 사람이 공유하여 사용할 목적으로 체계화해 통합, 관리하는 데이터의 집합체.
* DBMS: DB를 관리해주는 서비스
* RDB: 관계형 DB, 저장된 데이터 사이에 관계가 있다.
* SQL: DB에서 데이터를 정의, 조작, 제어하기 위해 사용하는 언어.
<br><br>

### [SQL 구성]
* DDL: 데이터 정의(Definition) 언어 (CREATE, ALTER, DROP)
* DML: 데이터 조작(Manipulation) 언어 (INSERT, UPDATE, DELETE, SELECT)
* DCL: 데이터 제어(Control) 언어 (GRANT, REVOKE, COMMIT, ROLLBACK)
* 데이터 사이언스의 경우 DML을 많이 사용하고 특히 SELECT가 중요.
* 터미널에서 시작
    * mysql -u root -p
<br><br>

### [Database 관리]
* DB 목록 확인
    * show databases;
* DB 생성
    * create database testdb;
    * show databases;
* DB 사용
    * use testdb;
* DB 삭제
    * drop database testdb;
    * show databases;
<br><br>

### [User 관리]
* user 조회
    * use mysql;
    * select host, user from user;
* user 생성
    * 로컬
        * create user 'username'@'localhost' identified by 'password';
        * 여기서 username 이랑 password 알아서 수정
        * select host, user from user;
    * 외부
        * create user 'username'@'%' identified by 'password';
        * 여기서 username 이랑 password 알아서 수정
        * select host, user from user;
* user 삭제
    * drop user 'username'@'localhost';
<br><br>

### [User 권한 관리]
* 사전 작업
    * create database testdb;
    * use mysql;
    * create user 'noma'@'localhost' identified by '1234';
* 모든 권한 목록 확인
    * show grants for 'noma'@'localhost';
* 특정 DB의 모든 권한 부여
    * grant all on testdb.* to 'noma'@'localhost';
* 안보일 때 새로고침
    * flush privileges;
* 특정 DB의 모든 권한 삭제
    * revoke all on testdb.* from 'noma'@'localhost';
<br><br>



## `[Table]`
* DB 안에서 데이터가 저장되는 형태. row와 column로 구성된 데이터 모음.
<br><br>

### [테이블 생성]
* 사전 설정
    * create database zerobase default character set utf8mb4;
* 테이블 생성
    * create table mytable(id int, name varchar(16));
    * show tables;
* 테이블 정보 확인
    * desc mytable;
    * (컬럼 별로 디스크립션 출력)
<br><br>

### [테이블 변경, 삭제]
* 테이블 이름 변경
    * alter table mytable rename person;
    * show tables;
* 컬럼 추가
    * alter table person add column agee double;
    * desc person;
* 컬럼 데이터 타입 수정
    * alter table person modify column agee int;
    * desc person;
* 컬럼 이름 수정
    * alter table person change column agee age int;
    * desc person;
* 컬럼 삭제
    * alter table person drop column age;
    * desc person;
* 테이블 삭제
    * drop table person;
    * show tables;
<br><br>



## `[DML]`
<br><br>

### [INSERT 문법]
* 데이터 추가 명령어
* 입력한 컬럼 이름 순서와 값의 순서가 일치해야함.
* insert into 외우기
* 사전 설정
    * use zerobase;
    * create table person(id int, name varchar(16), age int, sex char);
    * desc person;
* 데이터 추가
    * insert into person (id, name, age, sex)
    * values (1, '이효리', 43, 'F');
    * select * from person;
* 모든 컬럼을 다 넣는다면 컬럼명 생략 가능
    * insert into person values
    * (2, '이상순', 48, 'M');
    * select * from person;
<br><br>

### [SELECT 문법]
* 데이터 조회 명령어
* select * from table 외우기
* 데이터 조회
    * select name, age, sex from person;
    * select * from person;
<br><br>

### [WHERE 문법]
* 특정 조건에 만족하는 것 조회
* where 사용 조회
    * select * from person where sex='F';
<br><br>

### [UPDATE 문법]
* 데이터 수정 명령어
* update table set 수정사항 외우기
* 데이터 수정
    * update person set age=23 where name='이효리';
    * select * from person where name='이효리';
<br><br>

### [DELETE 문법]
* 데이터 삭제 명령어
* delete from 외우기
* 데이터 삭제
    * delete from person where name='이상순';
    * select * from person;
<br><br>

### [실습 준비]
* 테이블 생성
    * create table celeb
    * (
        ID int not null auto_increment primary key, 
        NAME varchar(32) not null default '',
        BIRTHDAY date,
        AGE int,
        SEX char(1),
        JOB_TITLE varchar(32),
        AGENCY varchar(32)
        );
* desc celeb;
* 데이터 입력
    * INSERT INTO celeb VALUES (1, '아이유', '1993-05-16', 29, 'F', '가수, 텔런트', 'EDAM엔터테이먼트');
    INSERT INTO celeb VALUES (2, '이미주', '1994-09-23', 28, 'F', '가수', '울림엔터테이먼트');
    INSERT INTO celeb VALUES (3, '송강', '1994-04-23', 28, 'M', '텔런트', '나무엑터스');
    INSERT INTO celeb VALUES (4, '강동원', '1981-01-18', 41, 'M', '영화배우, 텔런트', 'YG엔터테이먼트') ;
    INSERT INTO celeb VALUES (5, '유재석', '1972-08-14', 50, 'M', 'MC, 개그맨', '안테나');
    INSERT INTO celeb VALUES (6, '차승원', '1970-06-07', 48, 'M', '영화배우, 모델', 'YG엔터테이먼트');
    INSERT INTO celeb VALUES (7, '이수현', '1999-05-04', 23, 'F', '가수', 'YG엔터테이먼트');
* select * from celeb;
<br><br>

### [ORDER BY 문법]
* select 문에서 특정 컬럼을 기준으로 정렬
* ASC(ascending)은 오름차순 정렬
* DESC(descending)은 내림차순 정렬
* 기본 값은 ASC 오름차순
* 정렬해서 가져오기
    * select age, name from celeb order by age asc;
    * select age, name from celeb order by age desc;
    * select age, name from celeb order by age, name;
    * select age, name from celeb order by age desc, name asc;
<br><br>

### [Comparision operators]
* 비교 연산자
* 같다(=), 같지 않다(<>, !=)
* 초과 미만(>), 이상 이하(>=)
* 비교 연산자 사용
    * select name, age from celeb where age=29 order by age;
    * select name, age from celeb where age!=29 order by age;
    * select name, age from celeb where age<>29 order by age;
    * select name, age from celeb where age>29 order by age;
    * select name, age from celeb where age<29 order by age;
    * select name, age from celeb where age>=29 order by age;
    * select name, age from celeb where age<=29 order by age;
<br><br>

### [Logical operators]
* 논리 연산자
* 결과를 bool로 리턴
* AND, OR
* NOT: 조건 만족하지 않을때 TRUE
* BETWEEN: 조건값이 범위 사이에 있을때 TRUE
* IN: 조건값이 목록에 있으면 TRUE
* LIKE: 조건값이 패턴에 맞으면 TRUE
* AND가 OR보다 먼저 적용
* 괄호 사용하면 우선순위 수정 가능
* AND, OR 사용
    * select * from celeb where age=29 and sex='F';
    * select * from celeb where sex='M' and age>40 order by name desc;
    * select * from celeb where age<25 or age>30 order by age;
    * select * from celeb where (age<29 and sex='F') or (age>30 and sex='M') order by age, sex;
    * select * from celeb where (agency='YG엔터테이먼트' or agency='나무엑터스') and age<30;
* NOT 사용
    * select * from celeb where not sex='F';
    * select * from celeb where (agency='YG엔터테이먼트' and not sex='M') or (job_title='가수' and not agency='YG엔터테이먼트');
    * select * from celeb where (birthday>19901231 and not sex='F') or (birthday<19800101 and not agency='안테나');
* BETWEEN 사용
    * select * from celeb where age between 20 and 40;
    * 범위는 이상, 이하로 해당 숫자 포함이며, and로 대체 가능
    * select * from celeb where age>=20 and age<=40;
    * not 같이 사용하려면 between 앞에 적은 컬럼보다 앞에 not
    * select * from celeb where (not birthday between 19800101 and 19951231 and sex='F') or (agency='YG엔터테이먼트' and not age between 20 and 45);
* IN 사용
    * select * from celeb where age in (28, 48);
    * or로 대체 가능
    * select * from celeb where age=28 or age=48;
    * select * from celeb where not agency in ('나무액터스', '안테나', '울림엔터테이먼트') and (sex='F' or age>=45);
* LIKE 사용
    * select * from celeb where agency like 'YG엔터테이먼트';
    * =로 대체 가능
    * select * from celeb where agency='YG엔터테이먼트';
    * 퍼센트 (%)
    * 원하는 부분이 일치하는 데이터
    * select * from celeb where agency like 'YG%';
    * select * from celeb where agency like '%엔터테이먼트';
    * select * from celeb where job_title like '%가수%';
    * 언더바 (_)
    * 두번째 글자가 G 인 데이터
    * select * from celeb where agency like '_G%';
    * 가 로 시작하고 최소 2글자 이상인 데이터
    * select * from celeb where job_title like '가_%';
    * 영 으로 시작하고 모델로 끝나는 데이터
    * select * from celeb where job_title like '영%모델';
    * 영화배우, 텔런트 병행 데이터
    * select * from celeb where job_title like '%영화배우%' and job_title like '%텔런트%';
    * 직업이 하나 이상, 영화배우 혹은 텔런트가 아닌 데이터
    * select * from celeb where job_title like '%,%' and not (job_title like '%영화배우%' or job_title like '%텔런트%');
<br><br>

### [UNION 문법]
* 여러개 SQL문을 합쳐서 하나의 SQL문으로 만들기
* 컬럼의 개수가 반드시 같아야 한다.
* 컬럼의 종류가 달라도 괜찮은데 개수는 같아야 한다.
* UNION: 중복된 값을 제거하여 리턴
* UNION ALL: 중복된 값도 모두 리턴
* 실습환경 구축
    * create table test1 (no int);
    * create table test2 (no int);
    * insert into test1 values (1);
    * insert into test1 values (2);
    * insert into test1 values (3);
    * insert into test2 values (5);
    * insert into test2 values (6);
    * insert into test2 values (3);
* UNION 사용
    * select * from test1 union all select * from test2;
    * select * from test1 union select * from test2;
    * select * from celeb where sex='F' union all select * from celeb where agency ='YG엔터테이먼트';
    * select * from celeb where sex='F' union select * from celeb where agency ='YG엔터테이먼트';
<br><br>

### [JOIN 문법]
* 두개 이상의 테이블을 결합하는 것
* table1 join table2 on 조건 외우기
* INNER JOIN: 교집합
* LEFT JOIN: 왼쪽 + 교집합
* RIGHT JOIN: 교집합 + 오른쪽
* FULL OUTER JOIN: 합집합
* SELF JOIN: 결과는 이너 조인이랑 동일
* LEFT와 RIGHT 특징
    * 교집합이 아닌 데이터는 NULL로 채워서 나옴
    * 레프트는 왼쪽이 먼저 표시, 교집합이 이어서 표시
    * 라이트는 교집합이 먼저 표시, 오른쪽이 이어서 표시
* FULL OUTER JOIN 특징
    * mysql에서는 사용 불가
    * 순서는 왼쪽 먼저 표시, 교집합 이어서 표시, 오른쪽 이어서 표시
* 실습환경 구축
    * create table snl_show (ID int not null auto_increment primary key, SEASON int not null, EPISODE int not null, BROADCAST_DATE date, HOST varchar(32) not null);
    * desc snl_show;
    * INSERT INTO snl_show VALUES (1, 8, 7, '2020-09-05', '강동원');
    INSERT INTO snl_show VALUES (2, 8, 8, '2020-09-12', '유재석');
    INSERT INTO snl_show VALUES (3, 8, 9, '2020-09-19', '차승원') ;
    INSERT INTO snl_show VALUES (4, 8, 10, '2020-09-26', '이수현');
    INSERT INTO snl_show VALUES (5, 9, 1, '2021-09-04', '이병헌') ;
    INSERT INTO snL_show VALUES (6, 9, 2, '2021-09-11', '하지원') ;
    INSERT INTO snl_show VALUES (7, 9, 3, '2021-09-18', '제시');
    INSERT INTO snl_show VALUES (8, 9, 4, '2021-09-25', '조정석');
    INSERT INTO snl_show VALUES (9, 9, 5, '2021-10-02', '조여정') ;
    INSERT INTO snl_show VALUES (10, 9, 6, '2021-10-09', '옥주현');
    * select * from snl_show;
* JOIN 사용
    * select celeb.id, celeb.name, snl_show.id, snl_show.host from celeb inner join snl_show on celeb.name=snl_show.host;
    * select celeb.id, celeb.name, snl_show.id, snl_show.host from celeb left join snl_show on celeb.name=snl_show.host;
    * select celeb.id, celeb.name, snl_show.id, snl_show.host from celeb right join snl_show on celeb.name=snl_show.host;
    * select celeb.id, celeb.name, snl_show.id, snl_show.host from celeb left join snl_show on celeb.name=snl_show.host union select celeb.id, celeb.name, snl_show.id, snl_show.host from celeb right join snl_show on celeb.name=snl_show.host;
* SELF JOIN 사용
    * 쿼리에서는 생략 가능. 알아서 돌아간다.
    * from 뒤에 테이블을 2개 다 적어야 한다.
    * select celeb.id, celeb.name, snl_show.id, snl_show.host from celeb, snl_show where celeb.name=snl_show.host;
    * select celeb.name, celeb.job_title from celeb, snl_show where celeb.name=snl_show.host and celeb.agency='안테나';
    * select celeb.name, celeb.age, celeb.job_title, snl_show.season, snl_show.episode from celeb, snl_show where celeb.name=snl_show.host and ((not celeb.job_title like '%영화배우%' and celeb.agency='YG엔터테이먼트') or (celeb.age>=40 and agency!='YG엔터테이먼트'));
    * select snl_show.id, snl_show.season, snl_show.episode, celeb.name, celeb.job_title from snl_show, celeb where snl_show.host=celeb.name;
    * select snl_show.host from snl_show, celeb where snl_show.host=celeb.name and (snl_show.episode in (7, 9, 10) or celeb.agency like 'YG______') and broadcast_date>='20200915';
<br><br>

### [CONCAT 문법]
* 여러 문자열을 하나로 합치거나 연결
* CONCAT 사용
    * select concat('concat', ' ', 'test')
    * select concat('이름:', name) from celeb;
<br><br>

### [ALIAS 문법]
* 컬럼이나 테이블 이름에 별칭 생성
* as라고 사용하면 되는데 생략도 가능
* ALIAS 사용
    * select name as '이름' from celeb;
    * select name as '이름', agency as '소속사' from celeb;
    * select concat(name, ': ', job_title) as profile from celeb;
    * select s.season, s.episode, c.name, c.job_title from celeb as c, snl_show as s where c.name=s.host;
    * select concat(s.season, '-', s.episode, '(', s.broadcast_date, ')') as '방송정보', concat (c.name, '(', c.job_title, ')') as '출연자정보' from celeb as c, snl_show as s where c.name=s.host;
    * select concat(s.season, '-', s.episode, '(', s.broadcast_date, ')') as '방송정보', concat (c.name, '(', c.job_title, ')') as '출연자정보' from celeb c, snl_show s where c.name=s.host;
<br><br>

### [DISTINCT 문법]
* 검색한 결과의 중복 제거
* select 바로 뒤에 넣기
* DISTINCT 사용
    * select distinct agency from celeb;
    * select sex, job_title from celeb where job_title like '%가수%';
    * select distinct sex, job_title from celeb where job_title like '%가수%';
<br><br>

### [LIMIT 문법]
* 검색결과를 정렬된 순으로 주어진 숫자만큼의 행만 조회
* 가장 마지막에 적어서 사용
* LIMIT 사용
    * select * from celeb limit 3;
    * select * from celeb order by age limit 4;
<br><br>



## `[AWS RDS]`

### [AWS RDS 정의]
* Amazon Web Service, Relational Database Service
* 클라우드 상에 데이터베이스를 구축
<br><br>

### [AWS RDS 생성]
* 회원가입
    * AWS 들어가서 회원가입
    * 개인으로 선택
    * 리전은 대한민국 선택
    * 서포트 플랜 선택 (무료 버전)
* MySQL RDS 생성
    * AWS 관리 콘솔 -> 왼쪽 상단 서비스 선택
    * 데이터베이스 - RDS 클릭
    * 데이터베이스 생성 누르기
    * 표준 생성 선택
    * MySQL 선택
    * 템플릿은 프리티어로 선택
    * DB 인스턴스 식별자는 그대로 사용
    * 마스터 사용자 이름 입력 (예시, root)
    * 마스터 암호 입력 (예시, root)
    * 프리티어로 사용 가능한 클래스 선택
    * 버스터블 클래스(t 클래스 포함) 선택
    * 스토리지 SSD로 선택
    * 스토리지 자동 조정은 반드시 비활성화
    * 나머지는 기본으로 선택
    * 연결 설정은 모두 기본값, 퍼블릭 액세스는 예 선택
    * 퍼블릭 액세스 가능은 외부에서 연결 가능하도록 하는 것
    * 보안 그룹, 포트 모두 기본
    * 데이터베이스 인증은 암호 인증 (test 위한 것. 주의.)
    * 추가구성 모두 기본값, 백업은 자동 백업 비활성화 선택
    * 모니터링 비활성화
    * 유지관리 모두 기본값, 삭제 방지는 활성화
    * 데이터베이스 생성
    * 상태가 사용 가능이 되면 생성 완료
* AWS RDS 외부 접속
    * AWS 관리 콘솔 -> 왼쪽 상단 서비스 선택
    * 데이터베이스 - RDS 클릭
    * Amazon RDS의 데이터베이스 클릭
    * 생성된 데이터베이스 클릭
    * 연결 및 보안
        * VPC 보안 그룹 클릭
        * 보안 그룹 ID 클릭
        * 인바운드 규칙 편집
        * 규칙 추가
        * MySQL/Aurora 선택, AnywhereIPv4 선택
        * 규칙 저장 클릭
        * 외부 접근 권한 발급 완료
<br><br>

### [AWS RDS 사용]
* AWS RDS 접속
    * AWS 관리 콘솔 -> 왼쪽 상단 서비스 선택
    * 데이터베이스 - RDS 클릭
    * Amazon RDS의 데이터베이스 클릭
    * 생성된 데이터베이스 클릭
    * 연결 및 보안
    * 엔드포인트, 포트 복사 해놓기
    * (터미널)
    * mysql -h <엔드포인트> -P <포트> -u <마스터 사용자 이름> -p
    * 마스터 암호 입력
    * show databases;
    * use mysql
    * select host, user from user;
* AWS RDS 중지
    * AWS 관리 콘솔 -> 왼쪽 상단 서비스 선택
    * 데이터베이스 - RDS 클릭
    * Amazon RDS의 데이터베이스 클릭
    * 중지하려는 데이터베이스 목록 체크
    * 작업 버튼 -> 중지 클릭
    * 스냅샷 아니오, 중지합니다 클릭
    * 시간이 많이 걸림
    * 7일 중지되고 자동으로 다시 시작되니 주의
* AWS RDS 시작
    * AWS 관리 콘솔 -> 왼쪽 상단 서비스 선택
    * 데이터베이스 - RDS 클릭
    * Amazon RDS의 데이터베이스 클릭
    * 시작하려는 데이터베이스 클릭
    * 오른쪽 상단에 작업 -> 시작 클릭
    * 시간이 많이 걸림
<br><br>



## `[SQL File]`

### [SQL File 정의]
* 
* 실습 환경
    * 깃허브-로컬 레포지토리 하나 파기
    * vscode로 해당 폴더 실행
<br><br>




