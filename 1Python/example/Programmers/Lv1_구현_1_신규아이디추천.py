'''
설명:
유저들의 아이디 생성, 아이디 규칙에 맞지 않을 경우 확인
입력된 아이디와 유사하면서 규칙에 맞는 아이디 추천
규칙 1) 아이디 길이 3이상 15이하
규칙 2) 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표
규칙 3) 마침표는 처음과 끝에 사용 불가, 연속 사용 불가
아이디어: 구현
시간복잡도:
변수:
'''

'''
[리뷰]
1. lower() 라이브러리
2. strip('.') 라이브러리
3. endwith() 가 아니라 endswith() 이니 주의.
'''

def solution(new_id):
    able = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        '-', '_', '.'
    ]
    
    # 1단계
    answer = new_id.lower()
    
    # 2단계
    answer_ = ''
    for k, v in enumerate(answer):
        if v in able:
            answer_ += v
    answer = answer_
    
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계
    answer = answer.strip('.')
    
    # 5단계
    if len(answer) == 0:
        answer = 'a'
        
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]
        
    # 7단계
    if len(answer) <= 2:
        answer = answer + answer[-1] * (3-len(answer))
    
    
    return answer

