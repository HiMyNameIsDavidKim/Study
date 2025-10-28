'''
[설명]
사전: AEIOU만 사용해 만들 수 있는 길이 5 이하의 모든 단어
A -> AA -> ... -> UUUUU
주어진 단어가 몇 번째 단어?

아이디어: DFS로 해당 단어까지 돌리면서 리스트에 넣기, 역인덱싱, 방문 불필요
변수: 
주어지는 단어, word
'''

'''
[리뷰]
1. 재귀 자체를 이해 못하는건 아님
2. DFS의 핵심 아이디어가 반복되는 계산을 줄이는 것이라는 점을 모름
3. DFS의 결과를 반드시 앞단에 다시 넘겨줘야하는데 그걸 못하는중
'''

import sys
sys.setrecursionlimit(999999)


def solution(word):
    moum = 'AEIOU'
    result = []
    
    def dfs(current):
        if len(current) > 5:
            return
        result.append(current)
        for m in moum:
            dfs(current+m)
        
    dfs('')
    
    return result.index(word)


