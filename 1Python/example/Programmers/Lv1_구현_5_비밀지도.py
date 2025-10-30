'''
[설명]
비상금 숨겨놓는 비밀지도 숫자로 암호화됨
지도는 한변의 길이가 n인 정사각형 배열, 공백=칸, #=벽
전체 짇는 두 장의 지도를 겹쳐야함.
지도1 또는 지도2 중 하나라도 벽이면 벽이다.
정수 배열로 암호화 되어 있다. (2진수)
값을 5자리 2진수로 변경하면 0은 공백, 1은 벽

지도를 1차원 문자열 배열로 리턴
["# #", "###", "###"]


아이디어:
10진수 -> 2진수로 변경
-> n자리 인트로 만들기

두 지도 덧셈 -> 0이면 공백 아니면 #


변수:
변의 크기, n
정수배열 arr1, arr2
'''

'''
[리뷰]
1. 2진수로 바꾸는 라이브러리: bin(n)[2:]
2. n자리로 맞추기: zfill(n)
'''

def ten2two(n):
    return bin(n)[2:]


def solution(n, arr1, arr2):
    answer = []
    
    arr1 = [ten2two(i).zfill(n) for i in arr1]
    arr2 = [ten2two(i).zfill(n) for i in arr2]
    
    for i, (ar1, ar2) in enumerate(zip(arr1, arr2)):
        row = ''
        for j, (a1, a2) in enumerate(zip(ar1, ar2)):
            if a1 == '0' and a2 == '0':
                row += ' '
            else:
                row += '#'
        answer.append(row)
        
    return answer




