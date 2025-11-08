'''
[설명]
대회에 N명 참가 후 토너먼트 진행
1번부터 N번을 차례대로 배정
1vs2, 3vs4, ..., N-1vsN 게임 진행
이긴 사람은 다음 라운드
다시 1번부터 N번 배정 또 토너먼트 진행
첫 라운드 A번 참가자는 B번 참가자와 몇번에 만나는지 궁금
A와 B 참가자는 항상 이긴다고 가정

[아이디어]
일반적인 구현 문제
n 길이 짜리 리스트 만들기
나머지 원소는 ''로 만들고
A와 B 원소는 A랑 B로 만들기
꺼내면서 토너먼트 하게 만들기
while문 쓰고 만났을때 break

[시간복잡도]
x

[변수]
게임 참가자 수, N
참가번호, A B
몇번째 라운드에서 만나는지, answer
'''

'''
[리뷰]
1. 오타 주의...
'''

def solution(n,a,b):
    answer = 0
    ls = []
    
    for i in range(n):
        if i == a-1:
            ls.append('A')
        elif i == b-1:
            ls.append('B')
        else:
            ls.append('')
            
    flag = True
    while flag:
        ls_ = []
        answer += 1
        for i, j in zip(ls[::2], ls[1::2]):
            if i == j:
                ls_.append('')
            else:
                cat = i+j
                if cat == 'AB' or cat == 'BA':
                    flag = False
                    return answer
                else:
                    ls_.append(cat.strip())
        ls = ls_
            
    return answer


