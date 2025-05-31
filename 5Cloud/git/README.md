# Git

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
* 맥 쓰는 사람 master에서 main으로 수정
    * git config --global init.defaultBranch main
* git config --global --list
* cat ~/.gitconfig
<br><br>

### [저장소에 파일 추가]
* 로컬 폴더 업로드 (remote 방식)
    * 터미널 저장소로 만들 폴더로 cd
    * git init
    * 깃허브에 리포지토리 리드미 없이 생성
    * git remote add origin (리포지토리의 https 키)
    * git add .
    * git commit -m "first commit"
    * git branch -M main
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

### [커밋 안될 때]
* add 한거 한번 취소한 뒤 다시 커밋
* git reset HEAD^
* git commit -m “10/5 17:50 study update”
* git push origin main
<br><br>

### [임시 저장]
* git stash
    * 임시 저장하고 다른 작업 가능 (ex. 브랜치 이동)
    * 앞에 했던 커밋 상태로 복구하고 작업 내용은 임시 저장 된다.
* git stash pop
    * 가장 최근 임시 저장본을 현재 branch에 적용
    * 적용과 함께 사라진다.
* git stash list
    * stash에 저장된 항목 출력
* git stash apply
    * git stash pop처럼 적용하지만 삭제는 하지 않는다.
* git stash clear
    * stash list 모두 삭제
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
    * github action을 활용하는 대표적인 기능.
    * 레포지토리의 규모가 클 때 시간낭비를 방지해준다.
* workflow : 레포지토리에 추가할 수 있는 자동화된 커맨드의 집합.
* branch : 독립적으로 작업을 진행하는 작업공간.
    * main : 메인 브렌치
    * release : 양산 브렌치
    * hotfixes : 에러를 잡거나 테스트 하는 브렌치
    * develop : 차세대를 개발하는 브렌치
    * feature : 기능을 개발하는 브렌치
* merge : 브렌치 간 합치는 기능.
<br><br>

### [checkout과 branch]
* git checkout (커밋 id)
    * 특정 버전(시점)으로 이동
    * 파일의 수정 상태나 생성도 모두 복원
    * git status 하면 HEAD가 해당 버전을 가리킴
* 브랜치 개념
    * 원래 코드를 복사하여 독립적으로 개발할 때 사용
    * 특정 버전에서 새로운 브랜치를 만들어 작업 후 병합 가능
    * 레포지토리를 처음 만들면 main 브랜치가 기본적으로 생성
* git branch
    * 로컬 브랜치 목록 보기
    * 아스타로 현재 브랜치 표시
* git branch -r
    * 리모트 브랜치 목록 보기
* git branch -a
    * 모든(로컬 + 리모트) 브랜치 목록 보기
* git branch (브랜치 이름)
    * 브랜치 생성
    * HEAD가 가리키는 현재 상태에서 브랜치가 생성
* git checkout -b (브랜치 이름)
    * 브랜치 생성과 동시에 이동
* git push origin (브랜치 이름)
    * 브랜치 배포
* git branch --delete (브랜치 이름)
    * 로컬 브랜치 삭제
* git push origin --delete (브랜치 이름)
    * 리모트 브랜치 삭제
* git checkout (브랜치 이름)
    * 브랜치 간 이동
<br><br>

### [merge와 conflict]
* 머지 개념
    * 현재 위치한 버전에 다른 버전을 병합
    * 헤드의 위치가 어딘지가 제일 중요
    * 브랜치를 병합할 때 사용
    * push pull할때 저절로 발생
* 머지 예시
    * dev와 main 브랜치가 있을때 둘을 main 브랜치로 병합하고 싶을 때
    * git checkout main
    * main 브랜치로 이동
    * git merge dev 하기
    * main 브랜치에 새로운 버전 하나가 생기고 머지된 버전이 저장
    * (컨플릭트 발생)
        * IDE에서 수락 or 직접 수정
        * git add .
        * git commit -m (메시지)
        * 커밋까지 해야만 컨플릭트 해결
    * git push origin main
    * 서버로 전송까지 완료
* 머지 예시 2
    * dev에서 main 브랜치를 가져와 병합하고 싶을 때
    * git checkout dev
    * dev 브랜치로 이동
    * git merge main 하기
    * dev 브랜치에 새로운 버전 하나가 생기고 머지된 버전이 저장
    * (컨플릭트 발생)
        * IDE에서 수락 or 직접 수정
        * git add .
        * git commit -m (메시지)
        * 커밋까지 해야만 컨플릭트 해결
    * git push origin dev
    * 서버로 전송까지 완료
* 컨플릭트 개념
    * 오토 머지가 불가능한 상황에서 발생
    * 두 브랜치에서 같은 버전의 같은 부분을 수정한 상황
    * 개발자가 직접 해결해야만 한다.
    * 컨플릭트가 발생한 파일은 특수문자가 생겨 표시
    * 충돌이 발생한 부분을 ======를 기준으로 위 아래 다른걸 표시
* 컨플릭트 해결 과정
    * 컨플릭트 발생한 파일 수정 (통일)
    * git add (파일 이름)
    * git commit -m (메시지)
    * 가끔 안될 때는 git commit -i -m (메시지)로 강제 커밋
    * 충돌 발생 부분을 파일에서 찾기로 완전히 수정하는게 중요
* 컨플릭트 꿀팁
    * 보통 push pull 과정에서 발생
    * 평소에 바로 push 하지말고 pull 먼저 하고 작업 하는게 중요
    * push 하다가 실패: pull해서 conflict 에러 수정
    * pull 하다가 실패: conflict 에러 수정
<br><br>



## `[CI/CD]`
* Continuous Integration / Continuous Deployment
* 지속적인 통합 / 지속적인 배포
* 테스트, 머지, 배포 과정을 자동화하는 것을 의미한다.
* 새로운 기능을 추가할 때 반복되는 과정을 자동화한다.
<br><br>

### [레퍼런스]
* [`입문, JSCODE`](https://www.youtube.com/watch?v=DZJsVVoPGuo&list=PLtUgHNmvcs6pzeVotjaBaRy-BtoWo_qBd&index=2)
* [`개념, 드림코딩`](https://www.youtube.com/watch?v=0Emq5FypiMM)
* [`공식 문서`](https://docs.github.com/ko/actions)
<br><br>

### [CI]
* 지속적인 통합
* 개발자들은 코드 변경을 주기적으로 빈번하게 머지해야 한다.
    * 이때 최대한 작은 단위로 쪼개고 개발하는 것이 머지하기 편하다.
* 통합을 위한 단계 (빌드, 테스트, 머지)를 자동화 한다.
    * CI 스크립트를 통해 자동으로 빌드와 테스트를 완료한다.
    * 테스트를 통과하면 자동으로 반영된다.
    * 테스트에 실패하면 개발자에게 자동으로 알람이 간다.
* 장점
    * 머지에 시간 낭비가 없으므로 개발 생산성이 향상된다.
    * 자동이므로 문제점을 더 빠르게 발견할 수 있다.
    * 자주 업데이트 되므로 버그 수정이 용이하다.
    * 따라서 코드의 퀄리티가 올라간다.
<br><br>

### [CD]
* 지속적인 배포
* 릴리즈할 준비 과정을 거친다.
* 릴리즈 준비가 끝난 버전을 자동으로 배포한다.
* 배포는 수동으로 하는 경우도 있다.
<br><br>

### [CI/CD 툴]
* 툴 종류
    * github actions
    * jenkins
    * circle CI
    * travis CI
* github actions와 jenkins를 많이 사용한다.
<br><br>

### [github actions 개념]
* 로직을 실행시킬 수 있는 일종의 컴퓨터.
* 구성 요소
    * Events: 깃허브에서 발생할 수 있는 이벤트. (ex. merge, commit)
    * Workflows: 수행하고자 하는 일들, jobs의 집합.
    * Jobs: 수행하고자 하는 일, 스크립트 (Steps)로 구성. (ex. unit test, E2E test)
    * Actions: 재사용 가능한 오픈된 액션들. (ex. action check out)
    * Runners: 각 jobs를 실행하는 VM.
* Actions에 자주 사용하고 필요한 것들이 대부분 공개되어 있다.
* Jobs는 기본적으로 병렬적으로 수행된다.
<br><br>

### [github actions 실습]
* 워크 플로우
    * 개발자가 코드 작성 후 커밋
    * 깃허브에 푸시
    * 깃허브 액션에 작성한 자동화 로직 실행
    * 로직: 빌드 -> 테스트 -> EC2 서버로 배포
    * 최신 코드로 EC2 서버 재실행
* 만드는 과정
    * 프로젝트 가장 위에 `.github` 폴더 만들기
    * `.github` 폴더 안에 `wrokflows` 폴더 만들기
    * `wrokflows` 폴더 안에 `[workflow 이름].yml` 파일 만들기
    * ```yml
      name: github actions example
      
      # Events
      on: 
        push: 
          branches: 
            - main
      
      # Jobs
      jobs: 
        My-Deploy-Job: 
          runs-on: ubuntu-latest

        # Steps
        steps: 
          - name: print Hello World
            run: echo "Hello World"
          
          - name: multi print
            run: |
              echo "Good"
              echo "Morning"
      ```
    * 깃허브 레포지토리에 올리기
* 실행 과정 보기
    * `.github` 파일 올라갔는지 확인
    * 깃허브 리포지토리 탭에 Actions 클릭
    * 이벤트에 의해 작동했다면 과정을 확인할 수 있다.
    * All workflows에서 워크플로우 선택
    * Jobs 중 하나 선택
    * steps 열어보면 내부 과정을 볼 수 있다.
<br><br>

### [Secrets and Variables]
* 보안이 필요한 변수를 저장할 수 있는 기능.
* steps에서 ${{ secrets.PASSWORD }} 처럼 불러와서 사용할 수 있다.
<br><br>



## `[Git 개념]`

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

### [git log 문법]
* git log
    * 저장소의 커밋 이력을 시간순으로 모두 출력
* git log -2
    * 최근 2개만 출력
* git log --skip 5
    * 최근 5개 스킵하고 나머지 모두 출력
* git log -p -1
    * diff를 포함해서 출력
* git log --oneline
    * 커밋 로그 id와 커밋 메시지만 보기
* git log --author=(유저 이름 or 유저 이메일)
    * 사용자 정보로 검색
* git log -S (검색어)
    * 파일의 변경 내용으로 검색
* git log --grep (검색어)
    * 커밋 메시지 내용으로 검색
<br><br>

### [remote repository]
* git remote add origin (url)
    * remote 저장소 추가
* git remote set-url origin (url)
    * 주소 수정
* git remote rename (old_name) (new_name)
    * 이름 수정
* git remote remove (name)
    * 삭제
* git remote -v
    * 정보 확인
* git remote show origin
    * 정보 상세 보기
* git pull origin main
    * 저장소의 최산 상태를 로컬에 동기화
    * Fetch + Merge 과정이 순차적으로 진행
* git push origin main
    * 로컬의 작업 내용을 저장소에 업로드
<br><br>

### [git tag]
* 깃 태그
    * 특정 버전에 태그를 달아놓을 필요가 있을 때 사용
    * 보통 버전을 릴리즈할 때 사용
    * tag 이름으로 체크아웃 가능
* git tag (태그 이름)
    * 태그 생성
    * HEAD가 가르키는 버전을 태그로 생성
* git tag
    * 태그 목록 조회
* git tag (태그 이름) (커밋 id)
    * 지금 버전 말고 이전 버전으로 태그를 생성
* git push origin (태그 이름)
    * 태그 배포하기
    * 깃허브에 태그가 표시되며 업로드
* git show (태그 이름)
    * 특정 태그 상세 조회
* git tag --delete (태그 이름)
    * 로컬에서 태그 삭제
* git push origin --delete (태그 이름)
    * 리모트에서 태그 삭제
<br><br>



## `[README.md]`

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
    * ~~내용~~ : 취소선
* 코드블럭
    * 일반 코드 블럭
    * <code> sum = a + b </code>
    * 복사가 가능한 코드 블럭
    * <pre><code> print(sum) </code></pre>
* 수평선 긋기
***
---
* 링크 표현
    * [Google](https://google.com)
    * <https://python.org>
* 이미지
    * 이슈탭에서 뉴 이슈 클릭
    * 내용 부분에 이미지 드래그드롭
    * 생성된 이미지 링크 사용
<br><br>
