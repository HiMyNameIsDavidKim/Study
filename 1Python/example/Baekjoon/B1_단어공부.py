def solution(str):
    str = str.upper()
    dc = {}
    cnt_list = []
    answer = ""
    for i in str:
        if i == ' ': pass
        elif i not in dc: dc[i] = 1
        elif i in dc: dc[i] += 1
    for k,v in dc.items():
        cnt_list.append(v)
    for k,v in dc.items():
        if v == max(cnt_list): 
            if answer == "": answer = k
            else: answer = "?"
    print(answer)

if __name__ == "__main__":
    str = input()
    solution(str)