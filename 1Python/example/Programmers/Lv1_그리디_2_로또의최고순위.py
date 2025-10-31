'''
[설명]
로또는 1부터 45까지의 숫자중 6개를 맞히는 복권
1위 = 6개 번호 모두 일치
2위 = 5개 일치
3위 = 4개 일치
4위 = 3개 일치
5위 = 2개 일치
6위 = 그 외
로또에 낙서로 일부 번호를 알 수 없음 (=0으로 표시)

로또로 당첨이 가능했던 최고 순위와 최저 순위는?

[아이디어]
0을 날리기 (몇개인지 세기)
카운터 -> 2개 이상인거 몇개인지 (=최저 순위)
2개 더 맞춘것 계산 (=최고 순위)


[변수]
로또 번호를 담은 배열, lottos
당첨 번호를 담은 배열, win_nums
리턴 값, [최고 순위, 최저 순위]
'''
'''
[리뷰]
1. 리스트에서 요소 수 세기: lottos.count(0)
'''

from collections import Counter

def solution(lottos, win_nums):
    answer = []
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    
    c = Counter(lottos+win_nums)
    len_0 = c[0]
    del c[0]
    
    correct = 0
    for k, v in c.items():
        if v == 2:
            correct += 1
    
    return [rank[correct+len_0], rank[correct]]