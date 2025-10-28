'''
[설명]
네트워크는 컴퓨터 간 연결된 형태
연결되어 있으면 1개의 덩어리
네트워크의 개수는?


아이디어: 연결 정보 = DFS, 네트워크 덩어리 크기 측정, 리스트 담기
변수:
컴퓨터 개수, n
연결 정보 배열, computers
'''

'''[리뷰]
1. 여전히 이해도 매우 부족.
2. 주석 참고.
3. 음료수 얼려먹기 기초 예제의 T/F 리턴, answer +=1 개념 이해 필요.
'''

# 내가 푼 풀이, 직관성 떨어짐
def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def dfs(node):
        visited[node] = True
        
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)  # 연결된건 다 방문 처리 해버리기
            answer += 1  # 덩어리 +1개
    
    return answer


# 가장 많이 푼 풀이, 큐 BFS 처럼 스택 DFS를 돌림, 훨씬 직관적임
# 그러나 여전히 answer +=1 하는 부분이 있음. (=이해 못한 부분)
# 그냥 원래 풀이로 하는게 나음.
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer
