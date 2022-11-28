# Docker

## `[AWS Docker]`
* 리눅스의 응용 프로그램들을 컨테이너로 타 OS에서 관리할 수 있게 해주는 프로그램.

### [DB Server]
* 컨테이너 : 격리된 공간에서 프로그램을 동작시키는 가상화 기술.
* 도커에서 컨테이너 생성
  * docker pull —platform linux/amd64 mysql
  * docker pull mysql:5.6
  * docker run —platform linux/amd64 -d -p 8080:8080 -e MYSQL_ROOT_PASSWORD=root —name mysql_container mysql:5.6
  * docker ps
  * docker exec -it (컨테이너ID) bash
* 도커 자체의 한글 깨짐
  * vim ~/.bashrc에서 환경변수 설정
  * export LANGUAGE=ko_KR.UTF-8 
  * export LANG=ko_KR.UTF-8
  * export LC_ALL=C.UTF-8
* mysql 대소문자, 한글깨짐 문제(구글링)
  * mysql -u root -p
  * show variables like 'lower_case_table_names';
  * exit;
  * apt-get update
  * apt-get install -y vim
  * ls -> cd etc
  * ls -> cd mysql
  * ls -> vim my.cnf
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
  * 도커 재시작
    * mysql -u root -p
    * show variables like 'lower_case_table_names';
    * status