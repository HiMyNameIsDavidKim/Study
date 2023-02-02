import sys


def solution(str_ps):
    if str_ps in ')(':
        ind = str_ps.index(')(')
        print(ind)


if __name__ == '__main__':
    str_ps = sys.stdin.readline().strip()
    solution(str_ps)