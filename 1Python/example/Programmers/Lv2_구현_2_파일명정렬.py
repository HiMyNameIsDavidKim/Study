'''
[설명]
파일 저장소 서버 관리
이름 순으로 정렬된 파일 정렬 필요
기존 방법은 10이 9보다 먼저 표현되는 문제
파일명에 포함된 숫자를 반영한 정렬 기능 필요

규칙1: 영어 대소문자, 숫자, 공백, 마침표, 빼기 부호
규칙2: 영문으로 시작, 숫자 하나 이상 포함
규칙3: HEAD, NUMBER, TAIL 구조
HEAD는 반드시 1글자 이상의 문자
NUMBER는 1~5글자의 연속된 숫자 (0~99999)
TAIL은 나머지 부분으로 랜덤

HEAD는 사전 순으로 정렬 (대소문자 구분 x, lower sort)
HEAD가 같을 경우 NUMBER의 숫자순 정렬 (int)
HEAD와 NUMBER가 같을 경우 원래 입력 순서 유지

아이디어: (head, number, tail) 튜플로 바꾸기
시간 복잡도:
변수: 
파일명 배열, files
head, number, tail
'''

'''
[리뷰]
1. 숫자인지 확인하는 라이브러리 isdigit() 활용
'''


def solution(files):
    answer = []
    for i, file in enumerate(files):
        num_start = 0
        
        while not file[num_start].isdigit(): # 
            num_start += 1
            
        num_end = num_start
        
        while num_end < len(file) and file[num_end].isdigit():
            num_end += 1
        
        head = file[:num_start].lower()
        number = int(file[num_start:num_end])
        
        answer.append((head.lower(), int(number), i, file))
        
    answer.sort(key = lambda x:(x[0], x[1], x[2]))    
    return [i[3] for i in answer]
