'''
[설명]
n개의 송전탑이 전선을 통해 연결
전선들 중 하나를 끊어서 네트워크를 2개로 분할
두 전력망이 갖는 송전탑 개수를 최대한 비슷하게

1개를 끊어서 송전탑 개수의 차이는? (최소값)

[아이디어]
최소값 = BFS, 큐
하나씩 끊어보며 결과 저장
결과를 저장할 때 트리 크기 = BFS
2개라고 생각하고 BFS 각각 구하기 -> 차이 저장
최소값 리턴

BFS 내부는
하나 물고 쭉쭉 이어나가면서 네트워크 덩어리 크기 체크
방문 여부 필수


[변수]
송전탑 개수, n
전선 정보, wires
'''

'''
[리뷰]
1. 그래프 안줄때 그래프 만들기: defaultdict(list)
2. 두개의 BFS 돌리는게 아님. 하나로 BFS 돌리면서 끊은 전선 제외.
   -> 전체 사이즈에서 하나의 BFS 사이즈 빼기.
'''

from collections import deque, defaultdict

def solution(n, wires):
    answer = float('inf')
    
    graph = defaultdict(list)  #
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start, blocked_edge):
        visited = [False] * (n+1)
        a, b = blocked_edge
        
        queue = deque()
        queue.append(start)
        visited[start] = True
        cnt = 1
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if node == a and neighbor == b: continue
                if node == b and neighbor == a: continue
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    cnt += 1
        return cnt
        
    for a, b in wires:
        size1 = bfs(a, (a, b))
        size2 = n-size1
        diff = abs(size1-size2)
        answer = min(answer, diff)
    
    return answer