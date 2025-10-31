'''
[설명]
단 한명의 선수 빼고 모든 선수가 마라톤 완주
완주하지 못한 선수 이름은?
(동명이인이 있음을 주의하라)

[아이디어]
빼기
카운터 쓰고 홀수개인 것 찾기

[변수]
마라톤 참여 선수 배열, participant
완주한 선수 배열, completion
'''

'''
[리뷰]
1. 리스트 빼기는 안되는데 카운터 빼기는 가능
'''

from collections import Counter

def solution(participant, completion):
    answer = ''
    c = Counter(participant + completion)
    
    for k, v in c.items():
        if v % 2 == 1:
            answer = k
    return answer
