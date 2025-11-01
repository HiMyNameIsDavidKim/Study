'''
[설명]
두팀으로 나눠 진행, 상대팀 진영 먼저 파괴
상대 진영에 최대한 빨리 도착 (최단거리)
(0,0)에서 시작 (n-1,m-1)에서 끝
검은색 부분 = 0 = 벽, 흰색 부분 = 1 = 길

상대 팀이 벽을 세우면 도착 못함. (return -1)

아이디어: 최단거리 = BFS
방문 여부 체크 필수
큐에 지금 위치 넣으면서 반복
4방향 다 가보기 -> 방문x & 흰색 부분이라면 바로 직전 값 +1

변수: 
게임 맵의 상태, maps (n*m)
'''

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0))    
    visited[0][0] = True
    
    while queue:
        i, j = queue.popleft()
        
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            # 탈출 조건
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            
            if not visited[ni][nj] and maps[ni][nj] == 1:
                queue.append((ni, nj))
                visited[ni][nj] = True
                maps[ni][nj] = maps[i][j] + 1
    
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
    
    
    
    