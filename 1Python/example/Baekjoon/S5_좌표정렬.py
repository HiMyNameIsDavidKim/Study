import sys

def solution(n):
    my_df = []
    for _ in range(n):
        j,k = map(int, sys.stdin.readline().strip().split())
        my_df.append([j,k])
    my_df.sort()
    [print(f'{j} {k}') for [j,k] in my_df]

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    solution(n)