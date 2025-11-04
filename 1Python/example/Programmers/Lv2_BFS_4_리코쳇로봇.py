'''
[설명]
격자모양 게임판 위에서 말을 움직이는 게임
시작 위치 출발 후 목표 위치에 정확하게 멈추기
상하좌우 중 한 방향으로 장애물이나 가장자리까지 미끄러짐
점: 빈공간, R: 로봇 처음 위치, D: 장애물 위치, G: 목표 지점

최소이동 수는?

[아이디어]
최단 경로 = BFS, 큐
멈추지 않는 움직임에 대한 것은 별도의 함수로 구현
여기서 bfs를 사용해야하는 곳은 큐에 넣고 계속 기록하는 것
큐에 지금 위치에서 4방으로 동시에 출발시키고 거리만 계속 기록
골에 도착하면 거리 리턴

[시간복잡도]
[변수]
게임판의 상태, board
'''

from collections import deque

def solution(board):    
    n = len(board)
    m = len(board[0])
    visited = [[False for _ in range(m)] for _ in range(n)]    
    
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    # 시작점, 도착점
    ri, rj = 0, 0
    gi, gj = 0, 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                ri, rj = i, j
            if board[i][j] == 'G':
                gi, gj = i, j

    def move(i, j, direct):
        while True:
            ni = i + di[direct]
            nj = j + dj[direct]
            
            if ni < 0 or nj < 0 or ni >= n or nj >= m or board[ni][nj] == 'D':
                return i, j
            
            i, j = ni, nj
    
    queue = deque()
    queue.append((ri, rj, 0))  # i, j, dist
    visited[ri][rj] = True
    
    while queue:
        i, j, dist = queue.popleft()
        
        if i == gi and j == gj:
            return dist
        
        for k in range(4):
            ni, nj = move(i, j, k)
            
            if not visited[ni][nj]:
                queue.append((ni, nj, dist+1))
                visited[ni][nj] = True
    
    return -1