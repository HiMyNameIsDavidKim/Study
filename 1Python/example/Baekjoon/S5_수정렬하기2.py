import sys

def solution(n):
    my_list = []
    for _ in range(n):
        arg = int(sys.stdin.readline().strip())
        my_list.append(arg)
    my_list.sort()
    [print(i) for i in my_list]

n = int(sys.stdin.readline().strip())
solution(n)