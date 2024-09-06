# SQL (제로베이스 강의)
<br><br>

## `[Database]`
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
* select from 외우기
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
* update set 외우기
* 데이터 수정
    * update person set age=23 where name='이효리';
    * select * from person where name='이효리';
<br><br>

### [DELETE 문법]
* 데이터 삭제 명령어
* select from 외우기
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
        BRITHDAY date,
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
    * select * from celeb where (AGENCY='YG엔터테이먼트' or AGENCY='나무엑터스') and age<30;
* NOT 사용
    * 
<br><br>










