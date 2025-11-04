'''
[설명]
땅은 총 N행 4열로 이루어져 있고 모든 칸에는 점수
1행부터 땅을 밟으며 한 행씩 내려온다.
각 행의 4칸 중 한 칸만 밟으며 내려온다.
특수 규칙: 같은 열을 연속해서 밟을 수 없다.

점수의 최댓값은?

[아이디어]
첫번째는 그대로 기록
이후 값은 선택할 때마다 이전에 선택할 수 있는 최댓값과 더해서 기록
행 만큼 (n번) 반복

[시간복잡도]
행 개수 100K, 열 개수 4, 총 400K -> O(N)으로 풀어야함.
그래프 형태의 DFS BFS or DP 사용 -> DP 사용

[변수]
주어진 땅, land
최대값, max_score
'''

def solution(land):
    n = len(land)
    dp = [[0 for _ in range(4)] for _ in range(n)]
    
    # 첫줄은 그대로
    for i in range(4):
        dp[0][i] = land[0][i]
    
    # DP
    for i in range(1, n):
        for j in range(4):
            ls = []
            for k in range(4):
                if k != j:
                    ls.append(dp[i-1][k])
            
            dp[i][j] = land[i][j] + max(ls)
    
    return max(dp[n-1])