'''
[설명]
같은 시간대 게임 이용 m명 늘면 서버 1대 추가
n*m명 이상 (n+1)*m명 미만이면 n대 증설
한번 증설하면 k 시간동안 운영하고 반납
10시 k=5 이면 10~15시 까지 운영

최소 몇번 증설해야하나?

[아이디어]
필요한 서버 수 먼저 기록
증설해야할 타이밍 정하기 -> 증설하는 타이밍과 증설된 서버 시뮬레이션

[시간 복잡도]
[변수]
시간대별 게임 이용자의 수 1차원 배열, players
서버 1대로 감당할 수 있는 최대 이용자 수, m
서버 1대가 운영 가능한 시간, k
'''


def solution(players, m, k):
    cnt = 0
    needs = [0] * len(players)
    simul = [0] * len(players)
    
    for i in range(len(players)):
        if players[i] >= m:
            needs[i] = players[i] // m
    
    for i in range(len(needs)):
        if needs[i] > 0 and needs[i] > simul[i]:
            num_add = needs[i] -simul[i]
            cnt += num_add
            for j in range(k):
                if i+j < len(needs):
                    simul[i+j] += num_add
    return cnt
