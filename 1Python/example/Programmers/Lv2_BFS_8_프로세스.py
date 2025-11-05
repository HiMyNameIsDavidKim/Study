'''
[설명]
운영체제가 다음 규칙에 따라 프로세스를 관리
특정 프로세스가 몇 번째로 실행되는지 알아내기

1.실행 대기 큐에서 대기중인 프로세스 하나 꺼내기
2. 실행 대기 큐에서 중요도가 더 높은 프로세스가 있으면 프로세스를 다시 큐에 넣음
3. 만약 없으면 방금 꺼낸 프로세스 실행 -> 종료

[아이디어]
큐에 쌓고 맥스 비교 후 실행 구현

[시간 복잡도]
복잡도고 나발이고 무조건 그대로 구현해야 함

[변수]
중요도 순서가 담긴 배열, priorities
몇번째로 실행되는지 알고싶은 프로세스의 인덱스, location
'''


from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque()
    [queue.append((idx, value)) for idx, value in enumerate(priorities)]
    ls_sorted = priorities[:]
    ls_sorted.sort()
    
    while queue:
        idx, value = queue.popleft()
        if value >= ls_sorted[-1]:
            ls_sorted.pop()
            answer += 1
            if idx == location:
                return answer
        else:
            queue.append((idx, value))
