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
* 입력 데이터가 많은 경우
    * data = sys.stdin.readline().rstrip()
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

