'''
설명:
찍는 방식 구현
전략1) 12345,12345,12345
전략2) 21232425,21232425
전략3) 3311224455,3311224455

이들 중에서 가장 많은 문제를 맞힌 사람을 배열에 담아 리턴

아이디어: 걍 구현
시간복잡도: 
변수: 
'''

'''
[리뷰]
1. 나머지 트릭을 썼다면 더 간단하게 해결 가능.

pattern1 = [1,2,3,4,5]
if answer == pattern1[idx%len(pattern1)]:
    score[0] += 1
'''


def solution(answers):
    l = len(answers)
    
    as_1 = [1, 2, 3, 4, 5] * (l//5+1)
    as_1 = as_1[:l]
    
    as_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (l//8+1)
    as_2 = as_2[:l]
    
    as_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (l//10+1)
    as_3 = as_3[:l]
    
    c_1, c_2, c_3 = 0, 0, 0
    for correct, a_1, a_2, a_3 in zip(answers, as_1, as_2, as_3):
        if correct == a_1:
            c_1 += 1
        if correct == a_2:
            c_2 += 1
        if correct == a_3:
            c_3 += 1
    
    winers = []
    num = max([c_1, c_2, c_3])
    [winers.append(idx+1) for idx, value in enumerate([c_1, c_2, c_3]) 
     if value == num]
    
    return winers