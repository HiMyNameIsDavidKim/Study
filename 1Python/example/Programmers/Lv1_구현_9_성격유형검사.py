'''
[설명]
4개 지표로 성격 유형을 구분한다.
각 지표에서 2개 유형중 1개로 결정된다.
성격 유형은 총 16개
RT / CF / JM / AN

검사지에 총 n개의 질문 -> 7개의 선택지
각 질문은 1가지 지표로 성격 유형 점수
"NA" 라고 했을때 예시
비동의 (네오 3 2 1 -> 0 -> 어피치 1 2 3) 동의
각 지표에서 더 높은 점수를 받은 유형으로 판단
유형의 점수가 같을 경우 사전 순으로 빠른 성격 선택

최종 성격유형은?

[아이디어]
딕셔너리 구조로 점수 담기

[시간 복잡도]
O(n)

[변수]
질문마다 판단하는 지표 1차 문자열 배열, survey
질문마다 선택지를 담은 1차 정수 배열, choices
'''

def solution(survey, choices):
    answer = ''
    scores = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }
    
    for s, c in zip(survey, choices):
        if c == 1:
            scores[s[0]] += 3
        elif c == 2:
            scores[s[0]] += 2
        elif c == 3:
            scores[s[0]] += 1
        elif c == 4:
            pass
        elif c == 5:
            scores[s[1]] += 1
        elif c == 6:
            scores[s[1]] += 2
        elif c == 7:
            scores[s[1]] += 3
        
    if scores["R"] >= scores["T"]:
        answer += "R"
    else:
        answer += "T"
    if scores["C"] >= scores["F"]:
        answer += "C"
    else:
        answer += "F"
    if scores["J"] >= scores["M"]:
        answer += "J"
    else:
        answer += "M"
    if scores["A"] >= scores["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer