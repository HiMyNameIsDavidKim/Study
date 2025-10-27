# 알고리즘 코딩 테스트 예제
* 이것이 취업을 위한 코딩 테스트다 with Python (나동빈)
* [깃허브 링크](https://github.com/ndb796/python-for-coding-test)
* 추가 공부: 
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

### [기초: 거스름돈 문제]
* 설명
    * 사용하는 동전의 최소 개수는?
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

### [기초: 1이 될 때까지]
* 설명
    * 어떤 수 N이 1이 될 때까지 다음 두 과정 중 하나 반복 수행
    * 1.. N에서 1을 뺀다.
    * 2.. N을 K로 나눈다.(N이 K로 나누어떨어질 때만 선택 가능)
    * 1이 될 때까지 수행해야 하는 최소 횟수는?
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

### [기초: 곱하기 혹은 더하기]
* 설명
    * 0부터 9까지의 숫자로 이루어진 문자열 S
    * 숫자 사이에 '×' 또는 '+' 연산자를 넣을 수 있다.
    * 만들 수 있는 가장 큰 수는?
* 아이디어
    * 0 혹은 1일 때에만 더하기를 하고 나머지는 곱한다.
    * 정당성: 곱하는게 커지는 속도가 더 빠르다.
* 시간 복잡도: x
* 변수: ls, result
* ```python
  ls = input()
  result = 0

  for num in ls:
      num = int(num)
      if num <= 1 or result <= 1:
          result += num
      else:
          result *= num
  
  print(result)
  ```
<br><br>

### [기초: 모험가 길드]
* 설명
    * N명의 모험가가 있고, 각 모험가는 공포도를 가진다.
    * 공포도가 X인 모험가는 반드시 X명 이상으로 구성된 그룹에 참여
    * 여행을 떠날 수 있는 그룹 수의 최댓값은?
* 아이디어
    * 오름차순 정렬 후 공포도가 낮은 모험가부터 길드를 만들어 출발한다.
    * 정당성: 오름차순일 경우 항상 최소한의 모험가 수로 결성된다.
* 시간 복잡도: x
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

### [기초: 상하좌우]
* 설명
    * NxN 크기 공간에서 (1,1) 위치부터 출발 최종 위치는 어디인가.
    * 계획서를 받아서 문자대로 이동 (상 하 좌 우 = U D L R)
    * 공간을 벗어나는 움직임은 무시된다.
* 아이디어
    * 
* 시간 복잡도: 
* 변수: n, i, j, plans, di, dj, move_types
* ```python
  n = int(input())
  i, j = 1, 1
  plans = input().split()
  
  # L, R, U, D에 따른 이동 방향
  di = [0, 0, -1, 1]
  dj = [-1, 1, 0, 0]
  move_types = ['L', 'R', 'U', 'D']

  # 이동 계획 하나씩 확인
  for plan in plans:
      # 이동 후 좌표 구하기
      for k in range(len(move_types)):
          if plan == move_types[k]:
              ni = i + di[k]
              nj = j + dj[k]
      # 공간 벗어나는 경우 무시
      if ni < 1 or nj < 1 or ni > n or nj > n:
          continue
      # 이동 수행
      i, j = ni, nj

  print(i, j)
  ```
<br><br>

### [기초: 시각]
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

### [기초: 왕실의 나이트]
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
      if (next_row >= 1 and next_row <= 8 
        and next_col >= 1 and next_col <= 8):
          result += 1
          
  print(result)
  ```
<br><br>



## `[유형3 & 4: DFS & BFS]`

### [기초: 음료수 얼려 먹기]
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

### [기초: 미로 탈출]
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
      # 큐에 초기값 넣기
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

### [기초: 두 배열의 원소 교체]
* 설명
    * 두개의 배열 A와 B는 N개의 자연수 원소로 구성
    * 최대 K번의 바꿔치기 연산이 가능 (A원소 B원소 바꾸기)
    * 목표는 A의 모든 원소 합이 최대가 되는 것이다.
    * 최대 값을 출력
* 아이디어
    * 둘 다 정렬한 뒤 순서에 맞게 비교하고 작으면 바꾸기
* 시간 복잡도: 
* 변수: 
* ```python
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  a.sort()
  b.sort(reverse=True)

  for i in range(k):
      if a[i] < b[i]:
          a[i], b[i] = b[i], a[i]
      else:
          break

  print(sum(a))
  ```
<br><br>



## `[유형6: 이진 탐색]`

### [기초: 떡볶이 떡 만들기]
* 설명
    * 떡볶이 떡의 길이가 일정하지 않다.
    * 한 봉지 안에 들어가는 떡 총 길이는 같게 맞춘다.
    * 절단기에 높이 H를 지정하여 떡을 한번에 절단한다.
    * 높이가 H보다 큰 떡은 잘리고 작은 떡은 잘리지 않는다.
    * 손님 요청 길이가 M일 때, 최소 M만큼의 떡을 얻으려면 H의 최댓값은?
* 아이디어
    * 적절한 높이를 찾을 때 까지 이진 탐색을 반복
    * 해당 높이가 조건에 만족하는지 보고 탐색 범위 좁히기 (파라메트릭 서치)
* 시간 복잡도: 
* 변수: 
* ```python
  n, m = list(map(int, input().split(' ')))
  array = list(map(int, input().split()))

  start = 0
  end = max(array)

  result = 0
  while(start <= end):
      total = 0
      mid = (start + end) // 2

      # 잘랐을 때 손님 떡 길이 계산
      for x in array:
          if x > mid:
              total += x - mid
      
      # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 탐색)
      if total < m:
          end = mid - 1
    
      # 떡의 양이 충분한 경우 더 적게 자르기 (오른쪽 탐색)
      else:
          start = mid + 1
          # result를 기록
          result = mid
  print(result)
  ```
<br><br>

### [기초: 정렬된 배열에서 특정 수 개수 구하기]
* 설명
    * N개 길이의 수열이 오름차순으로 정렬되어 있다.
    * x가 등장하는 횟수는?
* 아이디어
    * bisect 라이브러리 사용
* 시간 복잡도: O(logN) 이하 필수
* 변수: 
* ```Python
  from bisect import bisect_left, bisect_right

  # 값이 특정 범위에 속하는 데이터 개수 구하기
  def count_by_range(a, left_v, right_v):
      right_i = bisect_right(a, right_v)
      left_i = bisect_left(a, left_v)
      return right_i - left_i

  n, x = map(int, input().split())
  array = list(map(int, input().split()))

  count = count_by_range(array, x, x)
  print(count)
  ```
<br><br>



## `[유형7: DP]`

### [기초: 개미 전사]
* 설명
    * 개미 전사는 메뚜기 마을 식량창고 공격
    * 식량창고는 일직선으로 이어져 있다.
    * 선택적으로 약탈, 인접한 식량창고 공격 불가
    * 최대 약탈에 성공한 경우 식량은?
* 아이디어
    * i번째 창고까지만 있다고 가정한 후 최댓값 계속 구하기
    * i-1번째와 i-2번째 2개만 고려하고 DP 사용
    * a_i = max(a_i-1, a_i-2 + k)
    * 바텀업 DP 사용
* 시간 복잡도: 
* 변수: 
* ```python
  n = int(input())
  array = list(map(int, input().split()))

  d = [0] * 100

  d[0] = array[0]
  d[1] = max(array[0], array[1])
  for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

  print(d[n-1])
  ```
<br><br>

### [기초: 1로 만들기]
* 설명
    * 정수에 사용할 수 있는 연산 4가지
    * 1: 5으로 나누어 떨어지면 5로 나눈다.
    * 2: 3으로 나누어 떨어지면 3으로 나눈다.
    * 3: 2로 나누어 떨어지면 2로 나눈다.
    * 4: 1을 뺀다.
    * 연산 4개를 적절히 사용해 값을 1로 만들 때 연산의 최솟값은?
* 아이디어
    * 다른 연산을 섞는게 5로 나누는 것보다 나을 수 있다.
    * 단순 그리디가 아니라 DP임.
    * 이미 수행한 연산은 다 저장해두고 추후에 꺼내서 사용.
    * 예를들어 10이면 5가 했던 연산에 2만 나누면 됨. (+1) 
    * a_i = min(a_i-1, a_i/2, a_i/3, a_i/5) + 1
* 시간 복잡도: 
* 변수: 
* ```python
  x = int(input())

  d = [0] * 30001
  
  # 바텀업 DP
  for i in range(2, x+1):
      # 1 빼는 경우
      d[i] = d[i-1] + 1
      # 2로 나누는 경우
      if i % 2 == 0:
          d[i] = min(d[i], d[i//2] + 1)
      # 3로 나누는 경우
      if i % 3 == 0:
          d[i] = min(d[i], d[i//3] + 1)
      # 5로 나누는 경우
      if i % 5 == 0:
          d[i] = min(d[i], d[i//5] + 1)

  print(d[x])
  ```
<br><br>

### [기초: 효율적인 화폐 구성]
* 설명
    * N가지 종류의 화폐가 있다.
    * 화폐의 개수를 최소로 사용해 M원이 되도록 한다.
    * 화폐는 각각 무제한 사용 가능하다.
    * M원을 만들기 위한 최소한의 화폐 개수는?
* 아이디어
    * 작은 금액부터 차례대로 최소 화폐를 계산해서 저장
    * a_i-k 가 존재하는 경우, a_i = min(a_i, a_i-k +1)
    * a_i-k 가 존재하지 않는 경우, a_i = INF
    * 화폐 종류 별로 반복 수행하면 더 작은 값으로 갱신 가능함
* 시간 복잡도: 
* 변수: 
* ```python
  n, m = map(int, input().split())
  array = []
  for i in range(n):
      array.append(int(input()))
  
  d = [10001] * (m+1)

  d[0] = 0
  # 화폐 종류 별로 반복
  for i in range(n):
      # 화폐 종류와 동일한 값부터 m까지 반복
      for j in range(array[i], m+1):
          # (i-k)원을 만드는 방법이 존재하는 경우
          if d[j-array[i]] != 10001:
              d[j] = min(d[j], d[j-array[i]]+1)
  
  if d[m] == 10001:
      print(-1)
  else:
      print(d[m])
  ```
<br><br>

### [기초: 금광]
* 설명
    * n x m 크기의 금광이 있고 각 칸은 금이 들어있다.
    * 맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있다.
    * 이후 m-1번에 걸쳐 오른위, 오른, 오른아래 3가지 방향으로 간다.
    * 채굴자가 얻을 수 있는 금의 최대 크기는?
* 아이디어
    * 왼쪽에서 오는 각각의 최적 솔루션을 계산한다.
    * 그 값들 중에 가장 큰거랑 본인을 더한다.
    * dp[i][j] = array[i][j] + max(
        dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]
    )
* 시간 복잡도: 
* 변수: array[i][j] i행j열의 금의 양, dp[i][j] i행j열까지 최댓값
* ```python
  for tc in range(int(input())):
      n, m = map(int, input().split())
      array = list(map(int, input().split()))

      dp = []
      index = 0
      for i in range(n):
          dp.append(array[index:index+m])
          index += m
    
      # 바텀업 DP
      for j in range(1, m):  # 열
          for i in range(n):  # 행
              # 왼위
              if i == 0: left_up = 0  # 0번째 줄은 위에서 못
              else: left_up = dp[i-1][j-1]
              # 왼아래
              if i == n-1: left_down = 0  # 마지막 줄은 아래서 못
              else: left_down = dp[i+1][j-1]
              # 왼
              left = dp[i][j-1]
              dp[i][j] = dp[i][j] \
                + max(left_up, left_down, left)
      
      result = 0
      for i in range(n):
          result = max(result, dp[i][m-1])
      print(result)
  ```
<br><br>

### [기초: 병사 배치하기]
* 설명
    * 전투력을 가진 N명의 병사 무작위로 나열
    * 전투력이 높은 병사가 앞에 오도록 내림차순 배치 (앞병사 전투력 높음)
    * 열외라는 기능이 있으며, 남아있는 병사가 최대가 되어야 함
    * 병사의 순서를 바꾸는게 아니라 열외만 시켜서 내림차순 완성
    * 남아있는 병사의 수가 최대이려면 열외 시켜야하는 병사의 수는?
* 아이디어
    * DP 대표 유형, LIS(Longest Increasing Subsequence)
    * 가장 긴 증가하는 부분 수열 유형을 변형시킨 것
    * 모든 원소를 확인하며 array[j] < array[i]에서 점화식 실행
    * d[i] = max(d[i], d[j] + 1)
    * dp 테이블을 모두 갱신한 뒤에 마지막 값을 출력
* 시간 복잡도: 
* 변수: 병사 수 n, 각 전투력 리스트
* ```python
  n = int(input())
  array = list(map(int, input().split()))

  array.reverse()

  dp = [1] * n
  
  # LIS 알고리즘 수행
  for i in range(1, n):
      for j in range(0, i):
          if array[j] < array[i]:
              dp[i] = max(dp[i], dp[j] + 1)

  print(n - max(dp))
  ```
<br><br>



## `[유형8: 최단 경로]`

### [기초: 전보]
* 설명
    * 어떤 나라는 N개의 도시가 있다.
    * 전보를 보내서 다른 도시로 메시지를 전달한다.
    * 도시 X에서 Y로 향하는 통로가 있어야만 가능하다.
    * 도시 C에 위급 상황이 발생, 최대한 많은 도시로 메시지를 보낸다.
    * C에서 출발하여 최대한 많이 퍼지는 상황이다.
    * 메시지 받는 모든 도시 개수는? 메시지를 받는 데 걸리는 시간은?
* 아이디어
    * 한 도시에서 다른 도시까지의 최단 거리 문제
    * 우선순위 큐를 이용한 다익스트라
* 시간 복잡도: 
* 변수: 
* ```python
  import heapq
  import sys

  input = sys.stdin.readline
  INF = int(1e9)

  def dijkstra(start):
      q = []
      # 시작 노드로 가기 위한 최단 거리 초기화
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
  
  n, m, start = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  distance = [INF] * (n+1)

  for _ in range(m):
      a, b, c = map(int, input().split())
      graph[a].append((b, c))
  
  dijkstra(start)

  # 도달할 수 있는 노드의 개수
  count = 0
  max_distance = 0
  for d in distance:
      if d != INF:
          count += 1
          max_distance = max(max_distance, d)

  print(count - 1, max_distance)
  ```
<br><br>

### [기초: 미래 도시]
* 설명
    * N개의 회사가 도로를 통해 연결되어 있다.
    * 방문판매원 A는 1번 회사에서 X번 회사에 물건을 판매한다.
    * 연결된 회사는 양방향으로 이동할 수 있고 비용은 1이다.
    * 소개팅을 위해 중간에 있는 K번 회사에 방문해야 한다.
    * 방문 판매원이 이동하는 최소 시간은?
* 아이디어
    * 시간이 충분하므로 플로이드로 풀어보자.
    * 모든 노드 to 모든 노드 최단 거리 계산 후 출력
    * 1toK + KtoX
* 시간 복잡도: 
* 변수: 
* ```python
  INF = int(1e9)

  n, m = map(int, input().split())
  graph = [[INF] * (n+1) for _ in range(n+1)]

  # 자기자신 비용 0으로 초기화
  for a in range(1, n+1):
      for b in range(1, n+1):
          if a == b:
              graph[a][b] = 0

  # 간선 정보 입력
  for _ in range(m):
      a, b = map(int, input().split())
      graph[a][b] = 1
      graph[b][a] = 1

  x, k = map(int, input().split())

  # 플로이드
  for k in range(1, n+1):
      for a in range(1, n+1):
          for b in range(1, n+1):
              graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

  distance = graph[1][x] + graph[x][k]

  if distance >= INF:
        print(-1)
  else:
      print(distance)
  ```
<br><br>



## `[유형9: 백트래킹]`
## `[유형10: 투포인터]`
## `[유형11: MST]`

### [EX]
* 설명
    * 
* 아이디어
    * 
* 시간 복잡도: 
* 변수: 
* ```python
  ```
<br><br>
