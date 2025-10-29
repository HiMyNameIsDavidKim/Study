'''
[설명]
1~n 번으로 분류되는 개인정보 n개
약관 종류가 여러가지, 유효기간이 있음
유효기간이 지나면 반드시 파기
1월 5일 수집 -> 내년 1월 5일 파기
오늘 날짜로 파기해야할 개인정보 번호는?

아이디어:
전부 다 '일'으로 변경
개인정보 수집일 + 약관 유효기간 -> 파기일 계산
파기일 안 넘은거 어펜드

변수: 
오늘 날짜, today
약관 유효기간 배열, terms, ["A 6", ...]
개인정보 배열, privacies, ["2021.05.02 A", ...]
'''

'''
[리뷰]
1. 염병 떨지 말고 그냥 split() 으로 자르기.
2. 마지막에 부등호 헷갈리면 대입해보기.
'''

def convert(ymd):
    y = int(ymd[:4])
    m = int(ymd[5:7])
    d = int(ymd[8:10])
    return y*12*28 + m*28 + d

def add_month(days, m):
    return days + m*28

def solution(today, terms, privacies):
    answer = []
    dict_terms = {}
    for t in terms:
        alpha, m = t.split()
        dict_terms[alpha] = int(m)
    
    for idx, p in enumerate(privacies):
        ymd, kind = p.split()
        if convert(today) >= add_month(convert(ymd), dict_terms[kind]):
            answer.append(idx+1)
    
    return answer









