# 코딩 테스트

## 📋 Contents
### 🐍 Python algorithm
### 🎯 ML baseline
### 📊 SQL query
<br><br>



## `[🐍 Python algorithm]`
* ref: 개발자 장고, 이코테 2021
<br><br>

### [알고리즘 코딩 테스트]
* 시험 구성: 2 ~ 5시간, 2 ~ 7문제
* 보통 모든 문제를 다 맞춰야 통과된다.
* 최다 빈출 유형:
    * 🥇필수: 구현, DFS, BFS
    * 🥈안정권: 그리디, DP, 이진탐색
    * 🥉고득점: 다익스트라
* 푸는 순서
    * 지문 정독, 요구사항과 출제자 의도 분석
    * 구체적으로 주석 적기 (설명, 아이디어, 시간 복잡도, 변수)
    * 코딩
    * 제너럴 케이스, 엣지 케이스 대입
    * 시간 복잡도, 계산 복잡도 계산
    * 제출
<br><br>

### [준비 방법]
* 알고리즘 공부
    * 그리디, 구현(=시뮬레이션)
    * DFS, BFS
    * 정렬 (선택, 삽입, 퀵, 계수)
    * 이진 탐색
    * DP
    * 최단 경로 (다익스트라, 플로이드)
    * 백트래킹, 투포인터, MST
* 대표 유형 풀이
* 코드 암기
* 변형 문제 풀이
    * 1시간 내로 못풀면 답안지 확인
    * 1시간 내로 풀었어도 답안지 공부
    * 한달이 지나기 전에 같은 문제 풀이
    * 15분 내로 풀 수 있을 때까지 반복
* 하루에 4개 알고리즘 씩 반복 연습
    * 루틴:
        * 구현 (Lv1 2개, Lv2 1개, Lv3 가끔)
        * DFS & BFS (Lv2 1개씩)
* 난이도 (프로그래머스 기준)
    * Lv2가 주로 나오며, Lv3는 가끔 출제
    * Lv2을 중점적으로 훈련
* (프로그래머스, 오답노트, 스터디)
<br><br>

### [시간 제한]
* 시간 제한은 보통 1 ~ 5초
* 1초 기준 N 범위, 시간 복잡도
    * N=500, O(N^3)
    * N=2000, O(N^2)
    * N=100K, O(NlogN)
    * N=10M, O(N)
* 파이썬 1초에 20M 번 계산 가능
<br><br>

### [유형 별 분석]
* 유형별 대표 용도
    * 그리디: 모든 경우 확인 (ex. 거스름돈, 1이 될 때까지)
    * 구현: 생각을 코드로 (ex. 게임 구현, 문자열 처리)
    * DFS: 모든 경로 탐색 (ex. 연결 요소 찾기, 섬 개수)
    * BFS: 최단 거리 찾기 (ex. 미로, 최소 간선 수로)
    * 정렬: 순서 기반 문제 (ex. 회의실 배정, 두 배열의 원소 교체)
    * 이진 탐색: 빠른 값 찾기 (ex. 범위 매우 큰 탐색, 파라메트릭 서치)
    * DP: 계산 최적화 (ex. 각종 수열, 최대 최소, 시간이 너무 초과될 때)
* 알고리즘 별 시간 복잡도
    * 각 알고리즘 가져다 쓸 때 시간 복잡도 인지하기
    * sort(): O(NlogN)
    * 해시테이블 구축: O(n)
    * 해시테이블 검색: O(1)
    * 이진 탐색: O(logN)
<br><br>

### [유형1: 그리디]
* 현재 상황에서 지금 당장 좋은 것만 고른다.
* 문제를 풀기 위한 최소한의 아이디어를 요구한다.
* 그리디를 쓰면 되는지에 대한 정당성 분석이 중요하다.
    * 진짜 최적의 해가 나오는가?
    * 최소한의 아이디어 도출 -> 정당한지 검토
* [`예제`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>

### [유형2: 구현]
* 일반적으로: 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정.
* 코테에서는: 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제.
* 구현이라고 부르는 문제들
    * 알고리즘은 간단한데 코드가 지나치게 긴 문제
    * 실수 연산을 다루고 특정 소수점 자리까지 출력하는 문제
    * 문자열 처리 문제, 적절한 라이브러리 사용 문제
    * (=시뮬레이션, 완전탐색)
* 핵심
    * 문제 도식화: 구성하는 로직이 몇개인지, 뭔지 판단
    * 디버깅: 중간에 리턴으로 출력하며 확인
* 행렬 문제 팁
    * ```Python
      # 행렬 형태 (가상)
      # (0, 0), (0, 1), (0, 2)
      # (1, 0), (1, 1), (1, 2)
      # (2, 0), (2, 1), (2, 2)
      
      # 상, 하, 좌, 우
      di = [-1, 1, 0, 0]
      dj = [0, 0, -1, 1]

      # 현재 위치
      i, j = 2, 2
      
      # 현재 위치를 우측으로 이동
      ni = i + di[3]
      nj = j + dj[3]
      print(ni, nj)  # 현재 위치 출력 (2, 3)
      ```
* 보드 문제 팁
    * ```Python
      # 보드 형태
      board = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
      ]
      
      # 상, 하, 좌, 우
      di = [-1, 1, 0, 0]  # 행변화
      dj = [0, 0, -1, 1]  # 열변화

      # 현재 위치
      i, j = 0, 0

      # 말을 우측으로 이동
      ni = i + di[3]
      nj = j + dj[3]
      board[i][j] = 0  # 현재 위치를 0으로
      board[ni][nj] = 1  # 새 위치를 1로
      print(board)  # 말의 위치 출력
      # [0, 1, 0]
      # [0, 0, 0]
      # [0, 0, 0]
      ```
* [`예제`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>

### [유형3 & 4: DFS & BFS]
* 대표적인 그래프 탐색 알고리즘으로 DFS와 BFS가 있다.
* 탐색은 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정이다.
* 스택
    * 먼저 들어온 데이터가 나중에 나가는 형식의 자료구조 (선입후출)
    * 입구와 출구가 동일한 형태
    * 파이썬의 기본 리스트가 스택, append와 pop 사용.
    * 데이터가 오른쪽으로 들어와서 쌓이다가 오른쪽에서 나간다.
    * ```Python
      stack = []

      # 삽입 5, 삽입 2, 삽입 3, 삽입 7, 삭제, 삽입 1, 삽입 4, 삭제
      stack.append(5)
      stack.append(2)
      stack.append(3)
      stack.append(7)
      stack.pop()
      stack.append(1)
      stack.append(4)
      stack.pop()

      print(stack[::-1])  # 최상단 원소부터 [1, 3, 2, 5]
      print(stack)  # 최하단 원소부터 [5, 2, 3, 1]
      ```
* 큐
    * 먼저 들어온 데이터가 먼저 나가는 형식의 자료구조 (선입선출)
    * 입구와 출구가 모두 뚫려있는 터널 형태
    * 파이썬의 deque가 큐, append와 popleft 사용.
    * 데이터가 오른쪽으로 들어와서 왼쪽으로 나간다.
    * ```Python
      # 임포트 및 객체 선언 필수
      from collections import deque
      queue = deque()

      # 삽입 5, 삽입 2, 삽입 3, 삽입 7, 삭제, 삽입 1, 삽입 4, 삭제
      queue.append(5)
      queue.append(2)
      queue.append(3)
      queue.append(7)
      queue.popleft()
      queue.append(1)
      queue.append(4)
      queue.popleft()

      print(queue)  # 먼저 들어온 순서대로 출력 [3, 7, 1, 4]
      queue.reverse()
      print(queue)  # 역순 출력 [4, 1, 7, 3]
      ```
* 재귀 함수
    * 자기 자신을 다시 호출하는 함수
    * DFS나 BFS를 구현할 때 주로 사용한다.
    * 재귀 함수의 종료 조건을 반드시 명시한다.
    * ```Python
      def recursive_func(i):
          # 100번째 호출을 했을때 종료
          if i == 100:
              return
          print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출.')
          recursive_func(i+1)
          print(i, '번째 재귀함수를 종료합니다.')
      recursive_func(1)
      ```
    * 팩토리얼도 재귀함수로 구할 수 있으나 주의해야한다.
    * 팩토리얼과 유사하게 `점화식`을 공식 그대로 구현할 수 있다.
    * ```Python
      # 유클리드 호제법, 최대공약수 구하기
      def gcd(a, b):
          if a % b == 0:
              return b
          else:
              return gcd(b, a % b)
      print(gcd(192, 162))
      ```
* DFS
    * Depth-First Search, 깊은 부분을 우선적으로 탐색한다.
    * 스택 or 재귀함수를 이용하여 구현한다.
    * 수도 코드
        * 1: 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.
        * 2: 스택의 최상단 노드에 방문하지 않은 노드가 하나라도 있다면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
        * 3: 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
    * ```Python
      # 노드의 연결 정보를 표현
      graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
      ]

      # 노드의 방문 정보를 표현
      visited = [False] * 9
      result = []

      # 메서드 정의
      def dfs(graph, v, visited):
          # 현재 노드를 방문 처리
          visited[v] = True
          result.append(v)
          # 현재 노드와 연결된 다른 노드 재귀 방문
          for i in graph[v]:
              if not visited[i]:
                  dfs(graph, i, visited)  # 재귀가 핵심
      

      # DFS 호출
      dfs(graph, 1, visited)
      print(result) # 1 2 7 6 8 3 4 5
      ```
* BFS
    * Breadth-First Search, 너비 부분을 우선적으로 탐색한다.
    * 큐를 이용하여 구현한다.
    * 수도 코드
        * 1: 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
        * 2: 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리 한다.
        * 3: 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
    * 외우기 팁:
        * 최다니엘 BTS 보려면 줄서기 (Queue)
        * 모든경로 DFS 스택
    * ```Python
      # 노드의 연결 정보를 표현
      graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
      ]

      # 노드의 방문 정보를 표현
      visited = [False] * 9
      result = []

      # 메서드 정의
      from collections import deque

      def bfs(graph, v, visited):
          # 큐를 사용하기 위해 덱 라이브러리 사용
          queue = deque()
          # 큐에 초기값 넣기
          queue.append(v)
          # 현재 노드를 방문 처리
          visited[v] = True
          # 큐가 없을 때까지 반복 (핵심)
          while queue:
              # 큐에서 한 원소 뽑아 출력
              v = queue.popleft()  # 안에서 리셋 (핵심)
              result.append(v)
              # 아직 방문하지 않은 인접 원소 큐에 삽입, 방문처리
              for i in graph[v]:
                  if not visited[i]:
                      queue.append(i)
                      visited[i] = True
      

      # BFS 호출
      bfs(graph, 1, visited)
      print(result)  # 1 2 3 8 7 4 5 6
      ```
* [`예제`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>



### [유형5: 정렬]
* 데이터를 특정 기준에 따라 순서대로 나열
* (ex. 크기가 작은 순서로 정렬 (=오름차순))
* 선택 정렬
    * 처리되지 않은 데이터 중 가장 작은 데이터를 `선택`한다.
    * 맨 앞에 있는 데이터와 선택 데이터를 바꾼다.
    * 시간 복잡도: O(N^2)
    * ```Python
      array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

      for i in range(len(array)):
          min_idx = i # 가장 작은 원소의 인덱스
          for j in range(i+1, len(array)):
              if array[min_idx] > array[j]:
                  min_idx = j
          # 스왑 연산
          array[i], array[min_idx] = array[min_idx], array[i]
      
      print(array) # 0 1 2 3 4 5 6 7 8 9
      ```
* 삽입 정렬
    * 처리되지 않은 데이터를 하나씩 골리 적절한 위치에 `삽입`한다.
    * 첫번째 데이터는 정렬된 것으로 판단하고 삽입할 위치를 고른다.
    * 시간 복잡도: O(N^2)
    * ```Python
      array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
      
      for i in range(1, len(array)):
          for j in range(i, 0, -1):  # i부터 0까지 마이너스 이동
              if array[j] < array[j-1]:  # 지금이 앞보다 작으면
                  # 스왑 연산
                  array[j], array[j-1] = array[j-1], array[j]
              else:  # 지금이 앞보다 크면 브레이크
                  break

      print(array) # 0 1 2 3 4 5 6 7 8 9
      ```
* 퀵 정렬
    * 기준 데이터를 정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
    * 퀵 정렬의 기본 값은 첫번째 데이터를 `기준(pivot)`으로 설정한다.
    * 수도 코드
        * 1: 왼쪽에서 출발하여 기준보다 큰 데이터를 선택한다.
        * 2: 오른쪽에서 출발하여 기준보다 작은 데이터를 선택한다.
        * 3: 두 데이터의 위치가 꼬이지 않은 경우 위치를 서로 변경한다.
        * 4: 두 데이터의 위치가 엇갈리는 경우 `기준`과 작은 데이터를 서로 변경한다.
        * 5: 이제 `기준`을 중심으로 좌우로 데이터 묶음이 분할 되었다.
        * 6: 좌우의 데이터 묶음에 대하여 각각 퀵 정렬을 재귀적으로 실행한다.
    * 퀵 정렬은 표준으로 사용하는 정렬 알고리즘 이다.
    * 시간 복잡도: O(NlogN)
    * ```Python
      array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
      
      # 더 나은 구현
      def quick_sort(array):
          # 리스트가 하나 이하의 원소만 담고 있으면 종료
          if len(array) <= 1:
              return array
          pivot = array[0]  # 피벗 설정
          tail = array[1:]  # 피벗 제외 리스트

          left_side = [x for x in tail if x <= pivot]
          right_side = [x for x in tail if x > pivot]

          return quick_sort(left_side) + [pivot] + quick_sort(right_side)

      print(quick_sort(array))  # 0 1 2 3 4 5 6 7 8 9


      # 정석 구현
      def quick_sort(array, start, end):
          # 원소가 1개인 경우 종료
          if start >= end:
              return
          # 피벗은 첫 번째 원소
          pivot = start 
          left = start + 1
          right = end

          while(left <= right):
            
              # 피벗보다 큰 데이터를 찾을 때까지 반복
              while(left <= end and array[left] <= array[pivot]):
                  left += 1
            
              # 피벗보다 작은 데이터를 찾을 때까지 반복
              while(right > start and array[right] >= array[pivot]):
                  right -= 1
            
              # 엇갈렸다면 작은 데이터와 피벗을 교체
              if(left > right): 
                  array[right], array[pivot] = array[pivot], array[right]
            
              # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
              else: 
                  array [left], array[right] = array[right], array[left]
        
          # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
          quick_sort(array, start, right - 1)
          quick_sort(array, right + 1, end)

      quick_sort(array, 0, len(array) - 1)
      print(array)  # 0 1 2 3 4 5 6 7 8 9
      ```
* 계수 정렬
    * 데이터의 개수가 N, 데이터 중 최대 값이 K일 때 사용한다.
    * 특정한 조건이 만족해야 하지만 매우 빠르게 동작한다.
    * (조건: 동일한 값을 가지는 데이터가 여러 개 등장할 때)
    * 수도 코드
        * 1: 가장 작은 데이터 ~ 가장 큰 데이터 범위를 모두 담는 리스트를 생성한다.
        * 2: 인덱스가 곧 값에 해당한다고 생각하고 몇번 등장하는지 `개수`를 센다.
        * 3: 인덱스 별로 몇번 등장했는지에 대한 리스트가 생긴다.
        * 4: 출력에서 리스트의 순서대로 인덱스를 값만큼 반복하여 출력한다.
    * 시간 복잡도: O(N+K)
    * ```Python
      # 든 원소의 값이 0보다 크거나 같다고 가정
      array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
      count = [0] * (max(array) + 1)

      # 각 데이터에 해당하는 인덱스의 값 카운팅
      for i in range(len(array)):
          count[array[i]] += 1

      # 등장한 횟수 만큼 인덱스 출력
      for i in range(len(count)):
         for j in range(count[i]):
              print(f'{i} ')
      ```
    * 시간 복잡도: O(N+K)
* [`예제`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>

### [유형6: 이진 탐색]
* 이진 탐색
    * 순차 탐색: 앞에서부터 데이터 하나씩 확인
    * 이진 탐색: `정렬되어 있는 리스트`, 범위를 `절반씩 좁혀가며` 탐색
    * 이진 탐색은 `시작점, 끝점, 중간점`을 이용해 탐색 범위를 설정한다.
    * 수도 코드
        * 1: 시작점 인덱스와 끝점 인덱스를 기준으로 중간점 인덱스를 계산한다.
        * 2: 중간점의 값이 찾는 값보다 크면 중간점 이후는 버린다.
        * 3: 남은 리스트에서 앞의 과정을 재귀 반복한다. (1개 남을 때 까지)
    * 탐색 범위가 매우 클 때 사용한다.
    * 시간 복잡도: O(logN)
    * ```Python
      # 정석 구현
      def binary_search(array, target, start, end):
          if start > end:
              return None
          mid = (start + end) // 2
          # 찾은 경우
          if array[mid] == target:
              return mid
          # 중간점 보다 찾는 값이 작은 경우 왼쪽 확인
          elif array[mid] > target:
              return binary_search(array, target, start, mid-1)
          # 중간점 보다 찾는 값이 큰 경우 오른쪽 확인
          else:
              return binary_search(array, target, mid+1, end)

      n, target = list(map(int, input().split()))
      array = list(map(int, input().split()))

      # 이진 탐색 수행 결과 출력
      result = binary_search(array, target, 0, n-1)
      if result == None:
          print('There is no target.')
      else:
          print(result)
      ```
* bisect
    * 파이썬 이진탐색 유용한 라이브러리
    * bisect_left(a, x): a에 x를 삽입할 가장 왼쪽 인덱스
    * bisect_right(a, x): a에 x를 삽입할 가장 오른쪽 인덱스
    * ```Python
      # 라이브러리 소개
      from bisect import bisect_left, bisect_right

      # 값이 특정 범위에 속하는 데이터 개수 구하기
      def count_by_range(a, left_v, right_v):
          right_i = bisect_right(a, right_v)
          left_i = bisect_left(a, left_v)
          return right_i - left_i

      a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

      print(count_by_range(a, 4, 4))  # 2
      print(count_by_range(a, -1, 3))  # 6
      ```
* 파라메트릭 서치
    * 최적화 문제를 결정 문제(bool)로 바꾸어 해결하는 기법.
    * 최적화: 값을 최대한 작게하거나 크게 만드는 작업
    * 파라메트릭 서치 문제가 출제되는 경우 이진 탐색으로 해결 가능
* [`예제`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>

### [유형7: DP]
* 한번 계산한 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않는다.
* 탑다운 (하향식) 방식과 바텀업 (상향식) 방식이 있다.
* 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상 시킨다.
* 다른 알고리즘으로 풀이가 안되고 시간이 너무 걸릴 경우 DP인 경우가 많다.
* 점화식을 먼저 완성한 뒤에 DP로 구현하는 것이 좋다.
* 점화식을 모르면 못풀기 때문에 매우 기초적이고 대표적인 유형이 주로 나온다.
* 웬만하면 바텀업 DP가 출제되는 편이다.
* 결과 저장용 리스트를 DP 테이블이라고 부른다.
* 문제가 다음 조건을 만족해야 사용할 수 있다.
    * optimal substructure
        * 큰 문제를 작은 문제로 나눌 수 있다.
        * 작은 문제의 답을 모으면 큰 문제가 해결된다.
    * overlapping subproblem
        * 동일한 작은 문제를 반복적으로 해결해야 한다.
* 메모이제이션
    * DP의 탑다운 방식 중 하나이다.
    * 한번 계산한 결과를 메모리 공간에 메모하는 기법이다.
    * 값을 기록해 놓는다는 점에서 캐싱이라고도 한다.
* 피보나치 수열
    * 각 항은 앞선 항들의 합이다. (큰 문제가 작은 문제의 모움)
    * a_n = a_n-1 + a_n-2
    * a_1 = 1, a_2 = 1
    * 이를 재귀 함수로 구현할 경우 중복 호출 이슈가 있다.
    * 중복 호출을 방지하기 위해 이미 계산한 답을 저장한다.
    * ```Python
      # 일반 재귀 함수로 구현 -> O(2^N)
      def fibo(x):
          if x == 1 or x == 2:
              return 1
          return fibo(x-1) + fibo(x-2)
      

      # 탑다운 DP로 구현 (재귀) -> O(N)
      # 메모이제이션을 위한 DP 테이블 생성
      d = [0] * 100

      def fibo(x):
          # 종료 조건
          if x == 1 or x == 2:
              return 1
          # 이미 계산한 문제는 그대로 리턴
          if d[x] != 0:
              return d[x]
          # 계산해야할 문제는 점화식 사용
          d[x] = fibo(x-1) + fibo(x-2)
          return d[x]


      # 바텀업 DP로 구현 (반복문) -> O(N)
      d = [0] * 100

      d[1] = 1
      d[2] = 1
      n = 99

      for i in range(3, n+1):
          d[i] = d[i-1] + d[i-2]
      ```
* [`예제`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>

### [유형8: 최단 경로]
* 가장 짧은 경로를 찾는 알고리즘
* 각 지점은 그래프의 노드, 지점 간 경로는 그래프의 간선으로 표현한다.
* 다익스트라
    * 특정 노드에서 출발하여 다른 모든 노드로 가는 최단 경로 계산
    * 1: 출발 노드를 설정하고 최단 거리 테이블을 초기화한다.
    * 2: 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택한다.
    * 3: 해당 노드를 거쳐서 가는 비용을 계산, 최단 거리 테이블을 갱신한다.
    * 4: 2, 3 과정을 반복한다.
    * 음의 간선이 없을 때만 사용 가능 (ex. 현실 세계의 길찾기)
    * 매 상황마다 최소 비용을 선택하므로 그리디 알고리즘으로 분류된다.
    * 물론 거리 테이블을 사용해야하기 때문에 DP로도 볼 수 있다.
    * 시간 복잡도: O(V^2)
    * ```Python
      import sys
      input = sys.stdin.readline
      INF = int(1e9)  # 무한

      # 노드, 간선, 시작 노드
      n, m = map(int, input().split())
      start = int(input())

      graph = [[] for _ in range(n+1)]
      # graph[a] = [(b, c), (c, d)]  # a2b 비용=c, a2c 비용=d
      # graph[b] = [(a, c), (d, e)]  # b2a 비용=c, b2d 비용=e
      visited = [False] * (n+1)
      distance = [INF] * (n+1)

      # 간선 정보 입력
      for _ in range(m):
          a, b, c = map(int, input().split())
          graph[a].append((b, c)) # a2b 비용 = c

      # 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 반환
      def get_smallest_node():
          min_value = INF
          index = 0  # 최단 거리가 가장 짧은 노드 인덱스
          for i in range(1, n+1):
              if distance[i] < min_value and not visited[i]:
                  min_value = distance[i]
                  index = i
          return index
      
      # 다익스트라 알고리즘
      def dijkstra(start):
          # 시작 노드 초기화
          distance[start] = 0
          visited[start] = True
          # 시작 노드의 인접 노드 초기화
          for j in graph[start]:
              distance[j[0]] = j[1]
          # 시작 노드 외 나머지 노드들에 대해 반복
          for i in range(n-1):
              # 현재 최단 거리가 가장 짧은 노드
              row = get_smallest_node()
              visited[row] = True
              # 이 row 노드와 연결된 다른 노드
              for j in graph[row]:
                  # 이 row 노드를 거치는 비용
                  cost = distance[row] + j[1]
                  # row 노드를 거치는게 더 짧은 경우
                  if cost < distance[j[0]]:
                      distance[j[0]] = cost

      dijkstra(start)

      for i in range(1, n+1):
          # 도달할 수 없는 경우 무한 출력
          if distance[i] == INF:
              print('INFINITY')
          else:
              print(distance[i])
      ```
* 우선순위 큐
    * 다익스트라 알고리즘의 시간 복잡도를 개선하기 위해 사용.
    * 우선순위가 가장 높은 데이터를 가장 먼저 꺼낸다.
    * 힙(heap)을 이용하여 구현한다.
    * 최소 힙: 값이 작은 데이터가 우선순위가 높아 먼저 꺼낸다.
    * 최대 힙: 값이 큰 데이터가 우선순위가 높아 먼저 꺼낸다.
    * 파이썬의 heapq 라이브러리, heappush(), heappop()
    * ```Python
      import heapq
      
      # 오름차순 힙 정렬(heap sort, min heap)
      def heapsort(iterable):
          h = []
          result = []
          # 모든 원소를 차례대로 힙에 삽입
          for value in iterable:
              heapq.heappush(h, value)
          # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
          for _ in range(len(h)):
              result.append(heapq.heappop(h))
          return result
      
      result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
      print(result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

      # 내림차순 힙 정렬(heap sort, max heap)
      def heapsort(iterable):
          h = []
          result = []
          # 모든 원소를 차례대로 힙에 `음수로` 삽입
          for value in iterable:
              heapq.heappush(h, -value)
          # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
          for _ in range(len(h)):
              result.append(-heapq.heappop(h))  # 양수 변환
          return result
      
      result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
      print(result)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
      ```
* 다익스트라 (with 힙)
    * 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택에 활용한다.
    * 다익스트라의 기본 원리와 동일하다.
    * 가장 가까운 노드 저장을 위해 힙을 추가로 사용한다.
    * (위에 정석 구현에서 get_smallest_node 함수 대체)
    * 최단 거리가 가장 짧은 노드를 선택하므로 min heap을 사용한다.
    * 힙에 (거리, 노드) 튜플 형태로 삽입하여 구현할 수 있다.
    * 시간 복잡도: O(ElogV)
    * ```Python
      import heapq
      import sys
      input = sys.stdin.readline
      INF = int(1e9)  # 무한

      # 노드, 간선, 시작 노드
      n, m = map(int, input().split())
      start = int(input())

      graph = [[] for _ in range(n+1)]  # 0은 노드, 1은 거리
      # graph[a] = [(b, c), (c, d)]  # a2b 비용=c, a2c 비용=d
      # graph[b] = [(a, c), (d, e)]  # b2a 비용=c, b2d 비용=e
      distance = [INF] * (n+1)

      # 간선 정보 입력
      for _ in range(m):
          a, b, c = map(int, input().split())
          graph[a].append((b, c)) # a2b 비용 = c

      def dijkstra_with_heap(start):
          q = []
          # 시작 노드 초기화
          heapq.heappush(q, (0, start))
          distance[start] = 0
          # 큐가 없을 때까지 반복
          while q:
              # 최단 거리 노드 정보 꺼내기
              dist, now = heapq.heappop(q)
              # 이미 처리된 적 있는 노드라면 무시
              if distance[now] < dist:
                  continue
              # 현재 노드와 연결된 다른 노드
              for i in graph[now]:
                  cost = dist + i[1]
                  # 현재 노드를 거치는게 더 짧은 경우
                  if cost < distance[i[0]]:
                      distance[i[0]] = cost
                      heapq.heappush(q, (cost, i[0]))
      
      dijkstra_with_heap(start)

      for i in range(1, n+1):
          # 도달할 수 없는 경우 무한 출력
          if distance[i] == INF:
              print('INFINITY')
          else:
              print(distance[i])
      ```
* 플로이드
    * 모든 노드에서 다른 모든 노드로 가는 최단 경로 모두 계산한다.
    * 1: 그래프를 준비하고 최단 거리 테이블을 초기화한다.
    * 2: 1번 노드를 거쳐가는 경우로 테이블을 갱신한다. (k=1)
    * 3: 2번 노드를 거쳐가는 경우로 테이블을 갱신한다. (k=2)
    * 4: n번 노드까지 반복한다. (k=n)
    * 다익스트라 유사점: 단계 별로 거쳐가는 노드에서 수행
    * 다익스트라 다른점: 매 단계마다 노드 중 최단 거리 노드 선택을 하지 않음
    * 2차원 테이블에 최단 거리 정보를 저장, DP에 속한다.
    * 점화식 : D[a][b] = min(D[a][b], D[a][k] + D[k][b])
    * 노드의 개수가 적을 때만 사용할 수 있다.
    * 시간 복잡도: O(N^3)
    * ```Python
      INF = int(1e9)  # 무한

      n = int(input())
      m = int(input())
      graph = [[INF] * (n+1) for _ in range(n+1)]

      # 자기 자신은 0으로 초기화
      for a in range(1, n+1):
          for b in range(1, n+1):
              if a == b:
                  graph[a][b] = 0

      # 각 간선 정보 입력
      for _ in range(m):
          a, b, c = map(int, input().split())
          graph[a][b] = c  # a2b 비용 = c
      
      # 플로이드
      for k in range(1, n+1):
          for a in range(1, n+1):
              for b in range(1, n+1):
                  graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      
      for a in range(1, n+1):
          for b in range(1, n+1):
              if graph[a][b] == INF:
                  print('INFINITY')
              else:
                  print(graph[a][b])
      ```
* [`예제`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/0Basic/Algorithm/yee_co_te)
<br><br>

### [실전: 프로그래머스]
* 유형 별로 레벨 별로 LLM 추천 받기
* [`풀이`](https://github.com/HiMyNameIsDavidKim/Study/tree/main/1Python/example/Programmers)
<br><br>



### [필요 시 개발자 장고 참고]
### [유형9: 백트래킹]
### [유형10: 투포인터]
### [유형11: MST]



## `[🎯 ML baseline]`
* 불러오기
* 데이터 전처리
* EDA
    * 유형 분리, 유형 수정
    * categorical, numerical
* 모델링
    * 학습
    * 평가 (report or matric)
    * 해석 (fi, shap, ROC or 시각화)
<br><br>

### [불러오기]
* import pandas as pd
* import numpy as np
* import matplotlib.pyplot as plt
* import seaborn as sns
* plt.style.use(['seaborn-v0_8'])
* sns.set(style="darkgrid")
* df = pd.read_csv('train.csv')
* df.head(10)
<br><br>

### [데이터 전처리]
* df.shape
* df.info()
    * 시계열 변경: df['date'] = pd.to_datetime(df['date'])
* df.isnull().sum()
    * 채우기: df = df.fillna('Null')
    * 행기준 제거: df = df.dropna()
    * 열기준 제거: df = df.dropna(axis=1)
* df.describe()
<br><br>

### [EDA]
* 데이터 유형 분리
    * ```python
      cols_categorical = df.select_dtypes(include=object).columns
      cols_numerical = df.select_dtypes(exclude=object).columns
      print(f'##### categorical #####')
      [print(f'{col}: {df[col].nunique()}') for col in cols_categorical]
      print(f'##### numerical #####')
      [print(f'{col}: {df[col].nunique()}') for col in cols_numerical]
      ```
* 유형 수정
    * ```python
      cols = ['col1', 'col2']
      for col in cols:
          cols_numerical = cols_numerical.drop(col)
          cols_categorical = cols_categorical.append(pd.Index([col]))
      ```
* categorical
    * y가 이산형
        * ```python
          for i, col in enumerate(cols_categorical):
              plt.subplot(len(cols_categorical)//3, 3, i+1)
              sns.countplot(data=df, x=col, hue='y', legend=False)
              plt.title(f'{col} Count Plot')
          plt.tight_layout()
          plt.show()
          ```
    * y가 연속형
        * ```python
          for i, col in enumerate(cols_categorical):
              plt.subplot(len(cols_categorical)//3, 3, i+1)
              sns.violinplot(data=df, x=col, hue=col, y='y', inner='quartile', legend=False)
              plt.title(f'{col} Violin Plot')
          plt.tight_layout()
          plt.show()
          ```
* numerical
    * 상관계수 히트맵
        * ```python
          sns.heatmap(df[cols_numerical].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths='0.5')
          plt.title(f'Corr Heatmap')
          plt.tight_layout()
          plt.show()
          ```
    * y가 이산형
        * ```python
          for i, col in enumerate(cols_numerical):
              plt.subplot(len(cols_numerical)//3, 3, i+1)
              sns.violinplot(data=df, x='y', hue='y', y=col, inner='quartile', legend=False)
              plt.title(f'{col} Violin Plot')
          plt.tight_layout()
          plt.show()
          ```
    * y가 연속형
        * ```python
          df_temp = df.copy()
          df_temp = df_temp[cols_numerical]
          # df_temp = df_temp.sample(n=len(df_temp)//100, random_state=42)
          sns.pairplot(df_temp, kind="scatter", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
          plt.title(f'Scatter Plot')
          plt.tight_layout()
          plt.show()
          ```
<br><br>



### [모델링]
* 학습
    * ```python
      from sklearn.model_selection import train_test_split
      from sklearn.preprocessing import LabelEncoder
      import lightgbm as lgb


      LEARNING_RATE = 3e-2
      N_ESTIMATORS = 500
      THRESHOLD = 0.3

      params = {
          "learning_rate": LEARNING_RATE,
          "n_estimators": N_ESTIMATORS,
          "num_leaves": 16,
          "max_depth": 6,
          "drop_rate": 0.3,
          "seed": 42,
      }

      df_temp = df.copy()
      X = df_temp.drop('y', axis=1)
      Y = df_temp['y']

      cols_drop = ['id']
      for col in cols_drop:
          X.drop(col, axis=1, inplace=True)

      for column in X.columns:
          if X[column].dtype == object:
              le = LabelEncoder()
              X[column] = le.fit_transform(X[column])

      x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
      # x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)  # reg
      model = lgb.LGBMClassifier(**params, objective='binary', metric='binary_logloss')
      # model = lgb.LGBMClassifier(**params, objective='multiclass', metric='multi_logloss')  # multi
      # model = lgb.LGBMRegressor(**params, objective='regression', metric='mse')  # reg
      model.fit(x_train, y_train)
      ```
* 평가
    * 분류
        * ```python
          from sklearn.metrics import classification_report


          y_proba_train = model.predict(x_train)
          y_pred_train = (y_proba_train > THRESHOLD).astype(int)
          print(classification_report(y_train, y_pred_train, digits=3))

          y_proba_test = model.predict(x_test)
          y_pred_test = (y_proba_test > THRESHOLD).astype(int)
          print(classification_report(y_test, y_pred_test, digits=3))
          ```
    * 회귀
        * ```python
          from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


          y_pred_train = model.predict(x_train)
          y_pred_test = model.predict(x_test)

          print("[Train]")
          print(f'-' * 50)
          print('r^2_score: ', r2_score(y_train, y_pred_train))
          print('RMSE:', np.sqrt(mean_squared_error(y_train, y_pred_train)))
          print('MAE:', mean_absolute_error(y_train, y_pred_train))
          print('MSE:', mean_squared_error(y_train, y_pred_train))
          print(f'-' * 50)
          print("[Test]")
          print(f'-' * 50)
          print('r^2_score: ', r2_score(y_test, y_pred_test))
          print('RMSE:', np.sqrt(mean_squared_error(y_test, y_pred_test)))
          print('MAE:', mean_absolute_error(y_test, y_pred_test))
          print('MSE:', mean_squared_error(y_test, y_pred_test))
          print(f'-' * 50)
          ```
* 해석
    * feature importance
        * ```python
          palette = sns.color_palette("turbo", 20)[::-1]
          f_imp = pd.Series(model.feature_importances_, index = x_train.columns)
          f_top20 = ftr_importances.sort_values(ascending=False)[:20]
          sns.barplot(x=f_top20, y=f_top20.index, palette=palette)
          plt.show()
          ```
    * shapley value
        * ```python
          import shap


          explainer = shap.TreeExplainer(model)
          shap_values = explainer.shap_values(x_test)
          shap.summary_plot(shap_values, x_test, plot_type='bar')
          shap.summary_plot(shap_values, x_test)
          plt.show()
          ```
    * ROC Curve (bin, multi)
        * ```python
          from sklearn.metrics import roc_curve, auc
          from sklearn.preprocessing import label_binarize


          y_pred_proba = model.predict_proba(x_test)
          if y_pred_proba.ndim == 1:
              y_pred_proba = y_pred_proba.reshape(-1, 1)
          classes = model.classes_
          y_test_bin = label_binarize(y_test, classes=classes)
          n_classes = y_test_bin.shape[1]
          
          for i in range(n_classes):
              fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_proba[:, i])
              roc_auc = auc(fpr, tpr)
              plt.plot(fpr, tpr, label=f'Class {classes[i]} (AUC = {roc_auc:.2f})')

          plt.plot([0, 1], [0, 1], 'k--', lw=1)
          plt.xlabel('False Positive Rate')
          plt.ylabel('True Positive Rate')
          plt.title('ROC Curve')
          plt.legend()
          plt.show()
          ```
    * 시각화 (reg)
        * ```python
          result = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred_test})

          sns.scatterplot(x=result['Real Values'], y=result['Predicted Values'])
          lim_min = min(result['Real Values'].min(), result['Predicted Values'].min())
          lim_max = max(result['Real Values'].max(), result['Predicted Values'].max())
          plt.xlim(lim_min, lim_max)
          plt.ylim(lim_min, lim_max)
          x = [lim_min, lim_max]
          y = [lim_min, lim_max]
          plt.plot(x, y, color='red')
          plt.show()
          ```
<br><br>
