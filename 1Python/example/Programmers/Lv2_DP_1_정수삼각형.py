'''
[설명]
삼각형의 꼭대기에서 바닥까지 이어지는 경로
거쳐간 숫자의 합이 가장 큰 경우 찾기
이동 시에는 대각선 왼 or 오 가능

거쳐간 숫자의 최댓값은?

[아이디어]
최대찾기 DP
triangle 복제해서 DP로 설정
앞에서부터 쭉 업데이트, max 사용

[변수]
삼각형의 정보 배열, triangle
'''

'''
[리뷰]
1. 2차원 깊은 복사: dp = deepcopy(triangle)
'''

from copy import deepcopy

def solution(triangle):
    dp = deepcopy(triangle)
    
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j > 0:
                left = dp[i-1][j-1]
            else:
                left = 0
            if j < len(dp[i-1]):
                right = dp[i-1][j]
            else:
                right = 0
                
            dp[i][j] += max(left, right)
    
    return max(dp[-1])



