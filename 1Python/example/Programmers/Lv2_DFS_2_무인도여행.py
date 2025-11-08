'''
[설명]
무인도 여행 지도, 바다와 무인도 정보 표시
격자로 구성 각 칸은 X(바다) 혹은 1~9(무인도)
상하좌우로 연결되는 땅들은 하나의 무인도
상하좌우로 연결된 한 땅 무인도 숫자 합 = 머물 수 있는 날짜
섬마다 며칠씩 머물 수 있는가? (오름차순 소팅 후 리턴)

아이디어: 
[
"X591X",
"X1X5X",
"X231X",
"1XXX1"
]

di, dj 만들기
범위 밖 못나가게 방지
연결된거 이악물고 찾기 = DFS

변수: 
지도 배열, maps
총 식량, yummy: int = 0
현재 위치, (i, j): tuple = (0, 0)
'''

'''
[리뷰]
1. 재귀 깊이 해제 라이브러리: sys.setrecursionlimit(10000)
2. if문 1개당 리턴 있어야함.
3. 각 리턴에 주석 달면 알기 좀 쉬움.
'''


import sys

sys.setrecursionlimit(10000)

def solution(maps):
    answer = []
    len_i = len(maps)
    len_j = len(maps[0])
    visited = [[False for _ in range(len_j)] for _ in range(len_i)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    def dfs(i, j):
        yummy = 0

        if i < 0 or j < 0 or i > len_i-1 or j > len_j-1:
            return yummy  # 범위 밖 0 리턴
        
        if not visited[i][j] and maps[i][j] != 'X':
            visited[i][j] = True
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                yummy += dfs(ni, nj)
            return int(maps[i][j]) + yummy  # 현재 칸의 음식 + 주변 칸의 음식
        
        return yummy  # 방문한 땅 or 'X' 땅은 0 리턴
    
    for i in range(len_i):
        for j in range(len_j):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(dfs(i, j))
    
    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer