import sys

def solution(n):
    my_x = []
    my_y = []
    for _ in range(n):
        j,k = map(int, sys.stdin.readline().strip().split())
        my_x.append(j)
        my_y.append(k)

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    solution(n)