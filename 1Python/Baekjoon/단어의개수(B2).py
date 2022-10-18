def solution(str):
    cnt = 1
    cnt += str.count(" ")
    if str[0] == " ": cnt -= 1
    if str[-1] == " ": cnt -= 1
    print(cnt)

if __name__ == "__main__":
    str = input()
    solution(str)

#한글자 들어왔을때 처리