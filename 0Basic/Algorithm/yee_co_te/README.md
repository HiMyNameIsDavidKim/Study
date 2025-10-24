# 알고리즘 코딩 테스트 예제
* 이것이 취업을 위한 코딩 테스트다 with Python (나동빈)
* [깃허브 링크](https://github.com/ndb796/python-for-coding-test)
<br><br>



## `[파이썬 문법]`

### [자료형]
* 컴퓨터는 2진수를 사용하기 때문에 정확하게 0.9를 표현할 수 없다.
    * 해결법: round() 함수를 활용하고 소숫점 몇자리 까지만 보증한다.
* 나누기 연산자
    * /: 나눈 결과 (실수형)
    * %: 나머지
    * //: 몫
* 2차원 리스트 초기화
    * ls = [[0]*m for _ in range(n)]
* 문자열은 특정 인덱스의 값만 수정할 수 없다. (immutable)
* 튜플 사용법
    * 서로 다른 성질의 데이터를 묶어서 관리할 때
    * 데이터의 나열을 해싱의 키 값으로 사용할 때 (리스트로는 불가)
    * 리스트보다 메모리를 적게 사용해야 할 때
* 딕셔너리
    * 해시 테이블을 이용하므로 조회나 수정에서 O(1) 시간 복잡도를 가진다.
* 집합 자료형
    * 중복이 불가능하고 순서가 없다.
    * 딕셔너리처럼 {} 안에 넣지만 콤마로만 넣는 자료형이다.
    * 마찬가지로 조회나 수정에서 O(1) 시간 복잡도를 가진다.
    * set()함수에 리스트 넣으면 집합으로 바뀐다. (그래서 중복 제거 가능)
    * 수학에서 쓰는 합집합, 교집합, 차집합 연산이 가능하다.
<br><br>

### [표준 입력 방식]
* input(): 한 줄의 문자열을 입력 받는다.
* map(): 리스트의 모든 원소에 각각 특정 함수를 적용한다.
* 공백을 기준으로 입력
    * a, b, c = map(int, input().split())
    * list(map(int, input().split()))
* 그래프 입력
    * graph = []
    * [graph.append(list(map(int, input()))) for i in range(n)]
* 입력 데이터가 많은 경우
    * data = sys.stdin.readline().rstrip()
* ord(): 문자의 값을 아스키 코드 형태로 변환한다.
    * ord('A')  # 65
    * ord('B')  # 66
    * ord('C')  # 67
    * ord('a')  # 97
    * ord('0')  # 48
<br><br>

### [유용한 함수]
* 람다 표현식: 함수를 한줄로 적을 수 있다.
    * result = (lambda a, b: a+b)(3, 7)
    * result = list(map(lambda a, b: a+b, ls1, ls2))
* itertools: 순열, 조합
    * permutations(ls, 3)
    * combinations(ls, 3)
* collections: 덱, 카운터(등장 횟수)
    * counter = Counter(ls)로 객체 선언 후 counter['a']로 호출.
* math: gcd(최대 공약수), lcm(최소 공배수)
    * math.gcd(21, 14)
    * math.lcm(21, 14)
<br><br>



## `[유형1: 그리디]`

### [거스름돈 문제]
* 설명
    * 
* 아이디어
    * 가장 큰 화폐 단위부터 거슬러 준다.
    * 정당성: 큰 단위가 항상 작은 단위의 배수이기 때문이다.
* 시간 복잡도: x
* 변수: n, result
* ```python
  n = 1260
  result = 0
  coin_types = [500, 100, 50, 10]

  for coin in coin_types:
      result += n // coin
      n %= coin

  print(result)
  ```
<br><br>

### [1이 될 때까지]
* 설명
    * 
* 아이디어
    * 무조건 나눠보고 나머지가 나오면 1을 뺀다.
    * 정당성: 나누는게 줄어드는 속도가 더 빠르다.
    * 트릭1: k가 큰 것을 대비하여 한번에 빼준다.
* 시간 복잡도: x
* 변수: n, k, result, target
* ```python
  n, k = map(int, input().split())
  result = 0

  while True:
      target = (n // k) * k
      result += (n - target)
      n = target

      if n < k:
          break

      result += 1
      n //= k

  result += (n - 1)
  print(result)
  ```
<br><br>

### [곱하기 혹은 더하기]
* 설명
    * 
* 아이디어
    * 0 혹은 1일 때에만 더하기를 하고 나머지는 곱한다.
    * 정당성: 곱하는게 커지는 속도가 더 빠르다.
* 시간 복잡도: x
* 변수: ls, result
* ```python
  ls = input()
  result = 0

  for num in ls:
      if num <= 1 or result <= 1:
          result += num
      else:
          result *= num
  
  print(result)
  ```
<br><br>

### [모험가 길드]
* 설명
    * 
* 아이디어
    * 오름차순 정렬 후 공포도가 낮은 모험가부터 길드를 만들어 출발한다.
    * 정당성: 오름차순일 경우 항상 최소한의 모험가 수로 결성된다.
* 시간 복잡도: 
* 변수: n, ls, cnt, result
* ```python
  n = int(input())
  ls = list(map(int, input().split()))
  ls.sort()

  result = 0
  cnt = 0

  for i in ls:
      cnt += 1
      if cnt >= i:
        result += 1
        cnt = 0
  
  print(result)
  ```
<br><br>



## `[유형2: 구현]`

### [상하좌우]
* 설명
    * NxN 크기 공간에서 (1,1) 위치부터 출발 최종 위치는 어디인가.
    * 계획서를 받아서 문자대로 이동 (상 하 좌 우 = U D L R)
    * 공간을 벗어나는 움직임은 무시된다.
* 아이디어
    * 
* 시간 복잡도: 
* 변수: n, x, y, plans, dx, dy, move_types
* ```python
  n = int(input())
  x, y = 1, 1
  plans = input().split()
  
  # L, R, U, D에 따른 이동 방향
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  move_types = ['L', 'R', 'U', 'D']

  # 이동 계획 하나씩 확인
  for plan in plans:
      # 이동 후 좌표 구하기
      for i in range(len(move_types[i])):
          if plan == move_types[i]:
              nx = x + dx[i]
              ny = y + dy[i]
      # 공간 벗어나는 경우 무시
      if nx < 1 or ny < 1 or nx > n or ny > n:
          continue
      # 이동 수행
      x, y = nx, ny

  print(x, y)
  ```
<br><br>

### [시각]
* 설명
    * 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 확인
    * 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하기
* 아이디어
    * 
* 시간 복잡도: 
* 변수: h, count
* ```python
  h = int(input())
  
  count = 0
  for i in range(h+1):
      for j in range(60):
          for k in range(60):
              if '3' in str(i) + str(j) + str(k):
                 count += 1
  print(count)
  ```
<br><br>

### [왕실의 나이트]
* 설명
    * 왕실 정원은 체스판과 같은 8x8 좌표 평면이다. (컬럼abc, 행123)
    * 나이트는 L자 형태로만 이동할 수 있다. (수평2+수직1, 수직2+수평1)
    * 정원 밖으로 나갈 수 없다.
    * 나이트가 이동할 수 있는 모든 경우의 수는 몇개인가.
* 아이디어
    * 
* 시간 복잡도: 
* 변수: row, col, steps, result
* ```python
  input_data = input()
  row = int(input_data[1])
  col = int(ord(input_data[0])) - int(ord('a')) + 1
  
  # 나이트 이동 가능 8방향
  steps = [(-2,-1), (-1,-2), (-2,1), (-1,2),
      (2,-1), (1,-2), (2,1), (1,2)]
  
  # 8방 이동 가능 여부 확인
  result = 0
  for step in steps:
      # 이동 원하는 위치 확인
      next_row = row + step[0]
      next_col = col + step[1]
      # 이동 가능할 경우 카운트
      if next_row >= 1 and next_row <= 8 
        and next_col >= 1 and next_col <= 8:
          result += 1
          
  print(result)
  ```
<br><br>



## `[유형3 & 4: DFS & BFS]`

### [음료수 얼려 먹기]
* 설명
    * NxM 크기의 얼음틀. 구멍=0, 칸막이=1
    * 구멍이 붙어 있는 경우 서로 연결된 것으로 간주한다.
    * 생성되는 아이스크림의 총 개수 (덩어리)를 구하라.
* 아이디어
    * 자리를 다 돌면서 1로 채우는 것과 같다.
    * 구멍인 노드를 던져주며 DFS를 사용한다.
* 시간 복잡도: 
* 변수: 
* ```python
  n, m = map(int, input().split())

  graph = []
  for i in range(n):
      graph.append(list(map(int, input())))

  # 모든 노드에 대하여 음료수 채우기
  result = 0
  for i in range(n):
      for j in range(m):
          # 현재 위치에서 DFS 수행
          if dfs(i, j) == True:
              result += 1

  print(result)

  
  # DFS로 특정 노드와 연결된 모든 노드 방문
  def dfs(x, y):
      # 범위 벗어나면 즉시 종료
      if x <= -1 or x >= n or y <= -1 or y >= m:
          return False
      # 현재 노드를 아직 방문하지 않았다면
      if graph[x][y] == 0:
          # 방문처리
          graph[x][y] = 1
          # 상하좌우 위치 모두 재귀 호출
          dfs(x-1, y)
          dfs(x, y-1)
          dfs(x+1, y)
          dfs(x, y+1)
          return True
      return False
  ```
<br><br>

### [미로 탈출]
* 설명
    * NxM 크기의 직사각형 형태의 미로에 갇혔다.
    * 미로에는 괴물이 있고 피해가야 하며, 한번에 한칸만 이동한다.
    * 입구와 출구는 (1,1) -> (N, M) 이다.
    * 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
    * 탈출을 위해 움직여야하는 최소 칸의 개수를 구하라.
* 아이디어
    * 최단거리 즉 BFS 이다.
    * 모든 노드의 최단 거리 값을 기록한다.
* 시간 복잡도: 
* 변수: 
* ```python
  from collections import deque

  n, m = map(int, input().split())

  graph = []
  for i in range(n):
      graph.append(list(map(int, input())))
  
  # 방향 정의 (상하좌우)
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  print(bfs(0, 0))

  # BFS 구현
  def bfs(x, y):
      # 큐 구현
      queue = deque()
      queue.append((x, y))
      # 큐가 없을 때까지 반복
      while queue:
          x, y = queue.popleft()
          # 현 위치에서 4방향 확인
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              # 미로 밖은 무시
              if nx < 0 or nx >= n or ny < 0 or ny >= m:
                  continue
              # 괴물인 경우 무시
              if graph[nx][ny] == 0:
                  continue
              # 처음 방문하는 경우 최단 거리 기록
              if graph[nx][ny] == 1:
                  graph[nx][ny] = graph[x][y] + 1
                  queue.append((nx, ny))
              # 목적지까지 최단 거리 반환
              if nx == n-1 and ny == m-1:
                  return graph[n-1][m-1]
  ```
<br><br>



## `[유형5: 정렬]`


