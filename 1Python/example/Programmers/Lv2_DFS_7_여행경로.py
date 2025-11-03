'''
[설명]
주어진 항공권 모두를 이용해 여행경로 짜기
항상 ICN에서 출발
티켓을 이어서 방문 공항 경로를 완성
만약에 가능한 경로가 2개면 알파벳 순서가 앞서는 경로 선택
항상 모든 도시 방문 가능

방문하는 공항 경로는?

[아이디어]
모든 경로 탐색 = DFS, 스택
거의 구현에 가까운 재귀호출
0번 티켓 실행 -> 도착지를 현재위치로 저장
도착지가 출발지인 티켓 찾기
해당 티켓 실행


[시간복잡도]
공항 수 3~10k개

[변수]
항공권 정보 담긴 2차원 배열, tickets
방문 공항 경로, travel
'''

'''
[리뷰]
1. 탈출 조건이 생각보다 빡센 케이스.
-> '경로가 2개 이상이면 알파벳 순서' 라고는 했지만 그게 정답이라고는 안했음.
-> 그 방향으로 갔을 때 막힌 경우가 존재하므로 이것도 탈출해야함.
'''


def solution(tickets):
    def dfs(now, travel, tickets):
        if len(tickets) == 0:
            return travel
        
        candidate = []
        for i in range(len(tickets)):
            if tickets[i][0] == now:
                candidate.append([tickets[i][1], i])
        
        if not candidate:
            return None
        
        candidate.sort()
        
        for next_airport, idx in candidate:
            new_now = tickets[idx][1]
            new_tickets = tickets[:]
            new_tickets.pop(idx)
            travel.append(new_now)
            result = dfs(new_now, travel, new_tickets)
            if result:
                return result
            travel.pop()
    
    return dfs("ICN", ["ICN"], tickets)
