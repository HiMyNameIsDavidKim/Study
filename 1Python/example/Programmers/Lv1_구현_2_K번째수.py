'''
설명: 배열의 i번째부터 j번째까지 자르고 정렬 후 k번째 수는?
아이디어: 컷 컷 소팅 인덱싱
시간복잡도: 
변수: 
'''

def solution(array, commands):
    answer = []
    for c in commands:
        answer_ = array[c[0]-1:c[1]]
        answer_.sort()
        answer.append(answer_[c[2]-1])
    return answer