# Docker

## `[Docker]`
* [`Ref, 드림코딩`](https://www.youtube.com/watch?v=LXJhA3VWXFA&t=25s)
* 네클 수업 내용
  * 리눅스의 응용 프로그램들을 컨테이너를 이용해 다른 OS에서 관리할 수 있게 해주는 프로그램.
  * 도커파일 : 이미지와 컨테이너를 포함하는 파일.
  * 이미지 : 컨테이너 실행에 필요한 파일과 설정값을 포함하고 있는 것. (클래스)
    * 컨테이너는 이미지를 복제하여 실행한 상태. (인스턴스)
    * 이미지의 근본 설정값(param)은 변하지 않고, 추가되거나 변하는 상태값(arg)은 컨테이너에 저장된다.
  * 컨테이너 : 격리된 공간에서 프로그램을 동작시키는 가상화 기술. OS 가상화.
  * 도커 이미지 버전 바꾸는 법 : docker rmi (이미지의 uuid)
  * 도커 허브 : 도커 이미지를 올리는 허브. 깃허브와 유사하다.
<br><br>

### [필수 구성 요소]
* 도커 파일
    * 컨테이너를 어떻게 만들어야 하는지에 대한 설명서.
    * copy files: 설치를 위해 꼭 필요한 파일
    * install dependencies: 설치해야하는 프레임워크나 라이브러리
    * set environment variables: 필요한 환경 변수에 대한 설정
    * run setup scripts: 구동하는 스크립트
* 이미지
    * 도커 파일로 만들어낸 이미지.
    * 실행되고 있는 어플리케이션의 상태를 스냅샷해서 만들어둔다.
    * 변경이 불가능한 상태이다.
* 컨테이너
    * 샌드박스에서 개별적인 이미지를 실행할 수 있는 곳.
    * 샌드박스: 고립된 환경
    * 컨테이너 안에서 어플리케이션이 동작한다.
    * 개별적으로 파일 수정도 가능하며, 이미지에 영향을 주지 않는다.
* 객체지향 관점
    * 이미지 = 클래스, 컨테이너 = 인스턴스
<br><br>

### [배포 과정]
* git과 매우 유사함.
* 순서
    * 로컬과 필요한 서버에 도커 설치
    * 로컬에서 도커 파일 작성
    * 로컬에서 이미지 생성 (build)
    * 컨테이너 레지스트리에 이미지를 push
    * 필요한 서버에서 이미지를 pull
    * 실행
* 컨테이너 레지스트리: 깃허브처럼 시스템 간에 이미지를 공유하는 중개자
    * public: docker hub, red hat
    * private: AWS, GCP, Azure
* 도커 같은 컨테이너 엔진이 반드시 설치되어 있어야 된다.
<br><br>

### [배포 실습]
* Dockerfile 파일 하나 만들기
    * 내용
        * ```Dockerfile
          # 베이스 이미지 설정
          # FROM baseImage
          FROM node:16-alpine
        
          # 실행할 경로 설정
          WORKDIR /app
        
          # 패키지 파일 복사해오기
          COPY package.json package-lock.json ./
        
          # 라이브러리 설치하기
          RUN npm ci

          # 소스 파일 복사해오기
          COPY index.js .

          # 실행하기
          ENTRYPOINT [ "node", "index.js" ]
          ```
    * 팁
        * 레이어 시스템이기 때문에 빈번히 수정하는 파일은 가장 마지막에 작성한다.
        * 이미지를 다시 만들때 변경된 레이어 이하는 다 수정하기 때문이다.
        * RUN npm install 보다 RUN npm ci가 버전 호환성까지 체크되서 더 좋다.
* 이미지 생성 (build)
    * docker build -f Dockerfile -t fun-docker .
    * .: 도커 파일의 위치
    * -f: 도커 파일 이름 설정
    * -t: 이미지의 이름 설정
    * docker images
    * (생성된 이미지를 확인할 수 있다.)
* 도커 컨테이너 실행
    * docker run --name fun-docker -d -p 8080:8080 fun-docker
    * -d: detached, 터미널이 기다리지 않도록 설정
    * -p: 포트 설정 (로컬 포트 주소:컨테이너 포트 주소)
    * docker ps
        * 실행중인 도커 컨테이너 리스트를 확인한다.
    * docker stop [컨테이너 ID]
        * 실행중인 도커를 중지한다.
    * docker kill [컨테이너 ID]
        * 실행중인 도커를 강제 종료한다.
* 배포하기
    * 도커 허브에 리포지토리 하나 만들기
    * 도커 커맨드에서 리포지토리 이름 확인하기
    * docker images
    * docker tag fun-docker:latest (리포지토리 이름):latest
    * docker login (로그인 하기)
    * docker push (리포지토리 이름):latest
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