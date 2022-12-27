# Django(REST)

## `[Set-up(local)]`
* 장고 설치
    * cd 설치할곳(ex. /Users/davidkim/PycharmProjects)
    * mkdir djangoProject
    * cd djangoProject
    * pip install django
    * pip install djangorestframework
    * pip install markdown
    * django-admin startproject admin .
    * python manage.py migrate
    * python manage.py createsuperuser --email (본인이메일) --user (본인아이디)
    * python manage.py runserver
    * http://127.0.0.1:8000 를 브라우저 주소창에 넣고 엔터
    * 종료 : Control + C
* 가상환경 설정
    * 파이참으로 djangoProject 오픈 -> 가상환경에 인터프리터 새로 파기
    * (파이참 터미널)
    * conda create -n venv anaconda python=3.9
    * pip install --user --upgrade pip
    * conda create -n venv anaconda python=3.9
    * conda activate venv
    * conda list
    * conda info -e
* 인터프리터 설정
    * 인터프리터 새로 만들기 -> conda executable -> anaconda3/envs/venv/python.exe -> Make available to all projects 클릭 -> 완료
    * 인터프리터 설정에서 django 검색 설치
    * 파이참 edit configuration에서 venv 인터프리터로 설정
    * (파이참 터미널)
    * conda info -e
    * python manage.py runserver
    * http://127.0.0.1:8000 를 브라우저 주소창에 넣고 엔터
    * 종료 : Control + C
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
    * python manage.py migrate<br><br>



## `[Trouble shooting]`

### [Error : No migrations to apply.]
* DB에서 테이블 지우고 다시 테이블 생성 시도할때 나오는 에러.
* DB -> django-migrations 테이블 -> name 겹치는 row 있으면 작성 안됨.
* 쿼리 콘솔 열어서 해당 row delete 해주기.
* 다시 migrate 진행하면 됨.<br><br>
