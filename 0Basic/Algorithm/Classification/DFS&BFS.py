from collections import deque

"""
아래 그래프를 완전탐색.
        A
    B       C
    D       G H I
    E F         J

"""
graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']



## 재귀 사용
def dfs_recursive(graph, start, visited = []):
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return print(visited)

# dfs_recursive(graph, 'A')



## 스택 큐 사용
def dfs_stack(graph, root):
    visited = []
    stack = [root]
    
    while(stack):
        node = stack.pop()
        
        if(node not in visited):
            visited.append(node)
            stack.extend(graph[node])
    return print(visited)

dfs_stack(graph,'A')

def bfs_que(graph, root):
    visited = []
    queue = deque([root])
    
    while(queue):
        node = queue.pop()
        
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])
    return print(visited)

bfs_que(graph,'A')



# 리스트 사용
def dfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop() # 마지막 요소 삭제

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return print(visited)

dfs(graph, 'A')

def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited[0] # 첫 요소 삭제
        del need_visited[0]
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return print(visited)

bfs(graph, 'A')