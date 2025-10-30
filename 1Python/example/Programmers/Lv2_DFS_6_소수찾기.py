'''
[설명]
한자리 숫자가 적힌 종이 조각 붙여 소수 만들기
0, 1, 1 -> [11, 101]
종이 조각으로 만들 수 있는 소수 몇개?

아이디어:
소수 판별 알고리즘
모든 가능한 숫자 리스트 만들기
하나 추가하고 남은 애들 중에 재귀호출
켰다 껐다 백트래킹

변수:
각 종이 조각에 적힌 숫자, numbers
'''

'''
[리뷰]
1. DFS 문제는 가끔 순열으로 풀린다.
2. 순열 함수(리스트, 순열 길이): permutations(numbers, num)
3. 소수 판별 함수 외우기 (기억 안나면 그냥 냅다 다 나눠도 되긴 함)
'''

import math
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 홀수만 검사, 제곱근까지만 확인
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    visited = [False] * len(numbers)
    ls = []
    ls_num = set([])
    
    for i in range(len(numbers)):
        ls += list(permutations(numbers, i+1))
    
    for ls_ in ls:
        value = ''
        for i in ls_:
            value += i
        ls_num.add(int(value))
        
    ls_num = list(ls_num)

    for i in ls_num:
        if is_prime(i):
            answer += 1
    
    return answer
