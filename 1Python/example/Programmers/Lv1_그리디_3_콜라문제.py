'''
[설명]
콜라 빈병 2개 -> 콜라 1병 줌
20병 -> 19병 받음
빈병 a개를 주면 콜라 b병 줄 때

빈병 n개를 갖다주면 몇병을 받을 수 있을까?

[아이디어]
반복, n%a + ((n//a) * b)
실행 조건은 n//a > 0


[변수]
빈병, a -> 뉴콜라, b
빈병, n -> 뉴콜라, result
'''


def solution(a, b, n):
    answer = 0
    while n >= a:
        cola = ((n//a) * b)
        answer += cola
        n = n%a + cola
        
    return answer