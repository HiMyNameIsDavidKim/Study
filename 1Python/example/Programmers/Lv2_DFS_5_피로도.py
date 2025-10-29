'''
[설명]
일정 피로도를 사용해 던전 탐험
탐험을 위한 최소 피로도, 탐험을 마치면 사용하는 소모 피로도
하루에 한번 탐험할 수 있는 던전들이 있음
이 던전들을 최대한 많이 탐험
탐험할 수 있는 최대 던전수는?

아이디어: 모든 경로 탐색 = DFS
던전 리스트를 순회하면서 최종 탐험한 던전 몇개인지 세기
(그냥 permutation 쓰는 것도 가능함)

5개인 경우
하나 고르고 for 루프 돌면서 재귀 호출
1 -> 2 -> 3 -> 4
  -> 3 -> 4 -> 2
  -> 4 -> 2 -> 3
  
방문 처리에 대한 정보 필요함

탐색의 목적: 

변수: 
현재 피로도, k
(최소 피로도, 소모 피로도) 2차원 배열, dugeons
'''
'''
[리뷰]
1. 외부 변수 참조하는 nonlocal 사용법 숙지
2. 매번 가장 큰 값을 갱신하는 max 함수 활용법 숙지
3. DFS 재귀 다녀온 뒤 방문 처리 해제 -> 이게 백트래킹
'''

# DFS 풀이
def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(k, cnt):
        nonlocal answer  #
        answer = max(answer, cnt)

        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], cnt+1)
                visited[i] = False  #

    dfs(k, 0)
    
    return answer



# BFS 풀이 (번외)
from collections import deque

def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    # 바로 구현
    queue = deque()
    queue.append((k, 0, visited))  # 피로도, 카운팅, 방문정보
    
    while queue:
        f, cnt, visited = queue.popleft()
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if not visited[i] and f >= dungeons[i][0]:
                new_visited = visited[:]  # 리스트 복사
                new_visited[i] = True  # 새 리스트에만 방문 표시 (다른 경로는 다른 방문 패턴)
                queue.append((f - dungeons[i][1], cnt + 1, new_visited))

    return answer

