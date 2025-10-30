'''
[설명]
x를 y로 변환 연산은 3개
x에 n을 더한다.
x에 2를 곱한다.
x에 3을 곱한다.
x를 y로 변환하기 위해 필요한 최소 연산 횟수는?
불가능할 경우 -1

[아이디어]
최소 연산 = BFS, 큐 사용

세개다 해본 뒤에는 어떻게 판단?
가까워진다? -> 아님
카운팅을 튜플로 담아서 가지고 다닌다

[변수]
카운트, cnt
'''

'''
[리뷰]
1. 속도 개선을 위해 방문 처리 추가
'''

from collections import deque

def solution(x, y, n):
    answer = -1
    visited = set()
    
    queue = deque()
    queue.append((x, 0))  # 숫자, 카운트
    visited.add(x)
    
    while queue:
        i, cnt = queue.popleft()
        
        # 같으면 리턴
        if i == y:
            return cnt
        # 넘으면 컨티뉴
        if i > y:
            continue
        
        next_values = [i + n, i * 2, i * 3]
        
        for val in next_values:
            if val not in visited:
                queue.append((val, cnt+1))
                visited.add(val)
    
    return answer