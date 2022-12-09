# DB Server

## `[Set-up(local)]`
* MariaDB 설치
    * brew install mariadb
* 서버 시작
    * brew services start mariadb
* root 계정 비밀번호 설정
    * sudo mariadb-secure-installation
    * sudo mysql -u root -p
    * sudo set password for 'root'@'localhost'=password('비밀번호')
    * flush privileges;
* 권한 부여
    * sudo mysql -u root -p
    * use mysql
    * create database mariadb;
    * show databases;
    * use mariadb
    * create user 'mariadb'@'localhost' identified by 'mariadb';
    * grant all privileges on mariadb.* to mariadb@localhost;
    * flush privileges;
    * exit;
* DB 구축
    * 디렉토리 생성, CRUD 권한 부여
    * DB 생성(CREATE TABLESPACE), DB 확인(SELECT)
    * 테이블 생성(기본 SQL문)
    * 데이터 입력(기본 SQL문)<br><br>

## `[DBMS]`
* DataBase Management System, DB에 대한 CRUD 기능을 위한 복합체.
  * (서버 + 툴), (스토리지 + 환경변수 + 자료가공 로직)
  * 엄밀히 말하면 구축이 완료된 시스템은 툴이 제거된다.
  * 완료되고 나면 (서버 + 클라이언트) 상태가 된다.
* DB 서버 : DB 저장공간 및 질의한 정보를 제공 해주는 시스템 or 가상의 머신.
  * (스토리지 + 환경변수)
* DB 툴 : DB에 대한 CRUD 기능을 가진 모듈. (ex. MariaDB, Oracle)
  * (자료가공 로직)
* DB : 테이블의 집합, 3DTensor
* 테이블 : 데이터의 집합, 데이터 프레임, 2DTensor<br><br>

## `[DB 객체의 종류]`
* 테이블 : 데이터의 집합, 2DTensor
* 뷰 : 하나 이상의 테이블을 연결해 사용하는 객체.
* 인덱스 : 테이블의 값을 찾기 위한 객체
* 시노님 : DB객체에 별칭을 부여한 객체(알리아스)
* 함수 : 연산 후 리턴이 있는 객체(게터)
* 프로시저 : 함수처럼 생겼으나 리턴이 없는 객체(세터)
* 패키지 : 함수와 프로시저를 하나로 묶은 객체(함수)<br><br>