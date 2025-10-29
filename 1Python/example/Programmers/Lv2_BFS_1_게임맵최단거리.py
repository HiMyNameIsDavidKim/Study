'''
[설명]
두팀으로 나눠 진행, 상대팀 진영 먼저 파괴
상대 진영에 최대한 빨리 도착 (최단거리)
(0,0)에서 시작 (n-1,m-1)에서 끝
검은색 부분 = 0 = 벽, 흰색 부분 = 1 = 길

상대 팀이 벽을 세우면 도착 못함. (return -1)

아이디어: 최단거리 = BFS
방문 여부 체크 필수
큐에 지금 위치 넣으면서 방문 안했고 1이면 앞에 값을 더해주기

변수: 
게임 맵의 상태, maps (n*m)
'''


from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    def bfs():
        queue = deque()
        queue.append((0, 0))
        visited[0][0] = True
        
        while queue:
            i, j = queue.popleft()
            
            if i == n-1 and j == m-1:
                return maps[i][j]
            
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                
                if 0 <= ni < n and 0 <= nj < m:
                    if not visited[ni][nj] and maps[ni][nj] == 1:
                        maps[ni][nj] = maps[i][j] + 1
                        queue.append((ni, nj))
                        visited[ni][nj] = True
        return -1
    
    return bfs()

