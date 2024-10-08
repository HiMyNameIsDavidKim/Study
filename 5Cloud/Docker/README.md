# Docker

## `[Docker]`
* 리눅스의 응용 프로그램들을 컨테이너를 이용해 다른 OS에서 관리할 수 있게 해주는 프로그램.
* 컨테이너 : 격리된 공간에서 프로그램을 동작시키는 가상화 기술. OS 가상화.
* 이미지 : 컨테이너 실행에 필요한 파일과 설정값을 포함하고 있는 것. (클래스)
  * 컨테이너는 이미지를 복제하여 실행한 상태. (인스턴스)
  * 이미지의 근본 설정값(param)은 변하지 않고, 추가되거나 변하는 상태값(arg)은 컨테이너에 저장된다.
  * 도커파일 : 이미지와 컨테이너를 포함하는 파일.
* 도커 이미지 버전 바꾸는 법 : docker rmi (이미지의 uuid)
* 도커 허브 : 도커 이미지를 올리는 허브. 깃허브와 유사하다.
<br><br>

### [리셋 명령어]
* 모든 도커 컨테이너 삭제
  * docker stop $(docker ps -a -q)
  * docker rm $(docker ps -a -q)
* 모든 도커 이미지 삭제
  * docker rmi $(docker images -q)
* 이미지 캐시 완전 삭제
  * docker system prune --all --force
<br><br>



## `[서버 구축]`

### [DB Server_MySQL]
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
    * init-connect='SET NAMES utf8mb4'
    * character-set-server = utf8mb4
  * [client] 밑에 적기
    * default-character-set = utf8mb4
  * [mysql] 밑에 적기
    * default-character-set = utf8mb4
  * 컨테이너 재시작
    * (재시작)
    * mysql -u root -p
    * show variables like 'lower_case_table_names';
    * status
* mysql 파이참 연결
  * 파이참 DB 눌러서 설정(ID/PW)
  * admin폴더 -> setting파일 DATABASES 정보 수정
  * (파이참 터미널)
  * python m(탭) runserver
  <br><br>

### [Backend Server_Django(REST)]
* 환경변수 설정
  * 프로젝트에 requirements.txt 생성
  * 파일에 설치할 라이브러리 모두 작성
  * (파이참 터미널)
  * pip install --user --no-warn-script-location -r requirements.txt 
* mysql 자동테이블 생성 설정
  * (파이참 터미널)
  * django-admin startapp users
  * admin -> settings.py -> INSTALLED_APPS에 "users.apps.UsersConfig" 하나 추가
    * 주의 : users의 models.py는 반드시 이렇게 만들어야 한다. (정확하게 안하면 기능 안됨)
  * users -> models.py의 클래스 안에 use_in_migrations = True 및 컬럼들 추가 코딩
  * (파이참 터미널)
  * python manage.py makemigrations
  * python manage.py migrate
  <br><br>



## `[Compose Up]`
* 도커에 mysql과 django와 react 3가지를 모두 올려서 합치는 작업.
* 3개의 다른 컨테이너가 하나로 묶이는 것.
* docker-compose.yml 수정.
* 파이참 터미널
  * docker compose up
<br><br>