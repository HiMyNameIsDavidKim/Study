def solution(st):
    rr = int(st[0])
    ss = st[2:]
    pp = f""
    for i in range(0,len(ss)):
        pp += ss[i]*rr
    return pp

if __name__ == "__main__":
    rep = int(input())
    print_sol = f""
    for j in range(0,rep):
        st = input()
        print_sol += solution(st)
        if j == rep-1 : break
        print_sol += f"\n"
    print(print_sol)