'''
[설명]
n개의 음이 아닌 정수를 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버
타겟 넘버를 만들 수 있는 모든 경우의 수는?

[아이디어]
모든 경로 탐색하기 -> DFS
숫자 하나씩 꺼내면서 하나는 덧셈 재귀호출, 하나는 뺄셈 재귀호출
각 재귀호출에서 타겟에 도달하면 answer에 1 더하기
덧셈 뺄셈 재귀 각각 호출되기 때문에 모든 perms 커버 가능

[변수] 
사용할 숫자 배열, numbers
타겟 넘버, target
'''

'''
[리뷰]
문제 도식화를 제대로 안하고 시작해서 이해가 안된 것.

        시작(0)
       /      \
    +1         -1
   /  \       /  \
+1+1  +1-1  -1+1  -1-1

처음부터 한번에 전체 숫자 sum을 하려고 생각했는데 그러면 안됨.
한 숫자씩 더하고 길이가 끝났을 때 타겟 넘버와 같은지 확인해야 함.
'''

def solution(numbers, target):
    answer = 0
    
    def dfs(i, current_sum):
        nonlocal answer
        
        # 탈출 조건
        if i == len(numbers):
            # 반드시 끝날때 비교
            if current_sum == target:
                answer += 1
                return
            return
        
        dfs(i+1, current_sum+numbers[i])
        dfs(i+1, current_sum-numbers[i])
    
    dfs(0, 0)
    return answer