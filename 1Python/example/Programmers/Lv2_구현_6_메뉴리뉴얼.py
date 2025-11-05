'''
[설명]
단품 메뉴 조합해서 코스요리로 재구성
손님들이 가장 많이 함께 주문한 단품 메뉴를 코스메뉴로
코스메뉴는 최소 2가지 이상의 단품
최소 2회 이상 주문된 세트만 선택

새로 추가할 코스요리의 메뉴 구성은?

[아이디어]
[시간 복잡도]
[변수]
손님들이 주문한 단품 메뉴들, orders
추가하고 싶은 코스요리 단품 갯수 배열, course
'''

'''
[리뷰]
1. 딕셔너리에서 벨류 기준으로 최대값 구하기: max(counter.values())
'''

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # 각 course 길이에 대해 처리
    for c in course:
        candidates = []

        # 각 손님의 주문에서 해당 길이의 조합 생성
        for order in orders:
            combi = combinations(sorted(order), c)  # 알파벳 순 정렬 후 조합
            candidates.extend([''.join(combi_elem) for combi_elem in combi])

        # 카운트
        counter = Counter(candidates)

        # 2회 이상 주문되고, 가장 많이 주문된 조합만 선택
        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for key, count in counter.items():
                    if count == max_count:
                        answer.append(key)

    # 사전 순 정렬
    answer.sort()

    return answer
