# Docker

## `[Docker]`
* 리눅스의 응용 프로그램들을 컨테이너를 이용해 다른 OS에서 관리할 수 있게 해주는 프로그램.
* 컨테이너 : 격리된 공간에서 프로그램을 동작시키는 가상화 기술. OS 가상화.<br><br>

### [DB Server]
* 도커에서 컨테이너 생성
  * docker pull --platform linux/amd64 mysql
  * docker pull --platform linux/amd64 mysql:5.7
  * docker run --platform linux/amd64 -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root --name mysql-container mysql:5.7
  * docker ps
  * docker exec -it (컨테이너ID) bash
* 도커 자체의 한글 깨짐
  * apt-get update
  * apt-get install -y vim
  * vim ~/.bashrc 에서 환경변수 설정(a 눌러서 아랫줄 추가)
  * export LANGUAGE=ko_KR.UTF-8
  * export LANG=ko_KR.UTF-8
  * export LC_ALL=C.UTF-8
* mysql 대소문자 문제, 한글깨짐 문제(구글링)
  * mysql -u root -p
  * show variables like 'lower_case_table_names';
  * exit;
  * apt-get update
  * apt-get install -y vim
  * ls -> cd etc
  * ls -> cd mysql
  * ls -> vim my.cnf 에서 환경변수 설정(a 눌러서 아랫줄 추가)
  * [mysqld] 밑에 적기
    * lower_case_table_names=1
    * skip-host-cache
    * skip-name-resolve
    * collation-server = utf8_unicode_ci 
    * init-connect='SET NAMES utf8' 
    * character-set-server = utf8
  * [client] 밑에 적기
    * default-character-set = utf8mb4 
  * [mysql] 밑에 적기
    * default-character-set = utf8mb4 
  * 컨테이너 재시작
    * (재시작)
    * mysql -u root -p
    * show variables like 'lower_case_table_names';
    * status<br><br>

### [Django(REST)]
