'''
[설명]
롤케이크를 두개로 잘라 나눠 먹는다.
토핑이 일렬로 올려져 있고 종류가 다양하다.
토핑의 개수보다 동일한 가짓수 기준으로 나누고 싶다.

**토핑 종류의 개수가 동일하게 나누는 방법의 경우의 수는?**

아이디어: 완전탐색, 중복 제거를 위한 set 사용, 종류수 같아지면 기록
변수: 
토핑 리스트, topping
'''

'''
[리뷰]
1. Counter 사용법 숙지
'''


# 카운터 없으면 타임아웃
def solution(topping):
    answer = 0
    
    for i in range(len(topping)):
        cheol = set(topping[:i])
        bro = set(topping[i:])
        if len(cheol) == len(bro):
            answer += 1
    
    return answer


# 카운터 사용
from collections import Counter

def solution(topping):
    answer = 0
    
    # 오른쪽(브로) 쪽 토핑 개수 미리 세기
    cheol = set()
    bro = Counter(topping)
    
    for t in topping:
        # 철수가 t를 가져감
        cheol.add(t)
        bro[t] -= 1
        if bro[t] == 0:
            del bro[t]
            
        # 종류 수 같으면 카운트
        if len(cheol) == len(bro):
            answer += 1
    
    return answer