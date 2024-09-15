# Git

## `[Git]`

### [VCS 개념]
* 버전 관리 시스템(Version Control Systems)
* 형상 관리 시스템(Configuration Management Systems)과 같은 말
* 버전별로 소스 관리, 문제 발생 시 전후 상황 파악
* 협업, 작업 추적, 복구
* 깃 공식 문서 https://git-scm.com/
<br><br>

### [Git 버전 관리]
* 파일을 저장하는 순간의 `스냅샷`을 저장
* 파일의 변경사항이 없는 경우, 파일을 새로 저장하지 않는다.
* Git 구성 요소
    * working directory
        * 작업 공간
        * 우리가 폴더에서 보고 있는 파일
    * staging area
        * 버전을 매기기 전 단계
        * add 시 오는 공간
        * 여기 있어야 커밋 가능
    * git directory
        * 버전을 매기고 관리하는 공간
        * commit 시 오는 공간
* Git 파일의 상태
    * untracked 상태: 워킹 디렉토리에 파일이 생성된 상태
    * tracked 상태: 깃이 파일을 관리하는 상태 (add 이후)
        * staged: add한 상태
        * committed: commit한 상태
        * modified: commit한 파일을 수정한 상태
* Git의 작업 순서
    * working dir 파일 수정
    * staging area에 파일을 staged하여 commit할 스냅샷 생성
    * staging area에 파일을 commit하여 git dir에 스냅샷 저장
<br><br>



## `[Github]`

### [깃 설치]
* brew 설치
    * (https://brew.sh/)
    * 커맨스 복사, 터미널에 붙여넣기, 엔터
    * 환경변수 설정 필요하면 해주기
    * brew --version
* git 설치
    * brew install git
    * 환경변수 설정 필요하면 해주기
    * git --version
<br><br>

### [유저 등록]
* git config --global user.email "...."
* git config --global user.name "...."
* 윈도우 쓰는 사람 CRLF 수정
    * git config core.autocrlf = true
* git config --global --list
* cat ~/.gitconfig
<br><br>

### [저장소에 파일 추가]
* 로컬 폴더 업로드 (init 방식)
    * 터미널 저장소로 만들 폴더로 cd
    * git init
    * git add .
    * git commit -m "first commit"
    * git branch -M main
    * git remote add origin (리포지토리의 https 키)
    * git push -u origin main
* 깃허브와 로컬 연결 (clone 방식)
    * 깃허브에 리포지토리 생성
    * 로컬에 폴더 생성할 곳에서 터미널
    * git clone (리포지토리의 https 키)
    * cd (리포지토리 이름)
    * (파일 수정)
    * git add .
    * git commit -m "first commit"
    * git push -u origin main
<br><br>

### [애드, 커밋, 푸시]
* git add .
* git commit -m “10/5 17:50 study update”
* git push origin main
<br><br>

### [기본 문법]
* git status
    * working dir과 staging area 상태 표시
    * 파일의 상태를 확인할 때 사용
    * 학습 초반에는 계속 status로 확인해보기
* git ignore
    * *.a: 확장자가 a인 파일 전부 무시
    * !lib.a: 확장자 a인 파일 전부 무시하지만 lib.a는 제외
    * /TODO: 현재 디렉토리 안의 TODO라는 파일만 무시 (다른 디렉토리는 x)
    * build/: build/ 디렉토리 모든 파일 무시
    * doc/*.txt: doc 폴더 안에 있는 txt 확장자만 무시
    * doc/**/*.txt: doc 폴더 아래 모든 txt 확장자 무시
* git rm
    * 깃에서 관리하는 파일 삭제
    * 로컬 파일을 먼저 지우더라도 깃에서 파일을 지워야 함
    * git status 쳤을때 워닝(deleted) 나오면 git rm 도 해줘야 함.
* git mv
    * 깃에서 파일이름 혹은 파일위치 변경에 사용
    * 로컬 파일을 먼저 옮기더라도 깃에서 파일을 옮겨야 함
    * git status 쳤을때 워닝(deleted 랑 untracked) 나오면 git rm 로 옮긴 파일 지우고, git add 로 옮겨진 파일 추가 
<br><br>

### [커밋 안될 때]
* add 한거 한번 취소한 뒤 다시 커밋
* git reset HEAD^
* git commit -m “10/5 17:50 study update”
* git push origin main
<br><br>

### [브랜치 생성]
* 폴더 생성
* git clone (리포지토리의 https 키)
* cd 폴더
* git branch -r
* git checkout -t origin/브렌치명
<br><br>

### [풀 리퀘스트]
* git add .
* git commit -m “10/5 17:50 study update”
* git push origin 브렌치명
* 깃허브 사이트에서 pull request
<br><br>

### [Github 응용]
* 협업 시 git을 사용하려면 추가적인 개념을 알아야 한다.
* push : 레포지토리 변경사항 업로드.
* pull : 레포지토리 변경사항 다운로드.
* github action : pull, push와 같은 이벤트 발생 시 자동화된 작업을 진행.
* CI/CD : push 이후 자동으로 빌드 및 배포 스크립트를 실행시켜주는 기능.
* **github action을 활용하는 대표적인 기능.
* **레포지토리의 규모가 클 때 시간낭비를 방지해준다.
* workflow : 레포지토리에 추가할 수 있는 자동화된 커맨드의 집합.
* branch : 독립적으로 작업을 진행하는 작업공간.
* **main : 메인 브렌치
* **release : 양산 브렌치
* **hotfixes : 에러를 잡거나 테스트 하는 브렌치
* **develop : 차세대를 개발하는 브렌치
* **feature : 기능을 개발하는 브렌치
* merge : 브렌치 간 합치는 기능.
<br><br>



## `[MarkDown]`

### [마크다운 문법]
* 제목 만들기
    * '#'입력하고 제목 적으면 됨.
    * '#'의 개수에 따라 제목이 탑다운 됨.
* 순서가 있는 목록
    * 1.목록1
    * 2.목록2
    * 3.목록3
* 순서가 없는 목록
    * *목록
    * *목록
    *     * 하위 목록
    * 탭으로 띄우면 됨.
* 텍스트 강조하기
    * **내용** : 굵게 표시하기
    * *내용* : 기울이기
<br><br>
