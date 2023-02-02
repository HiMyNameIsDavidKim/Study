import sys

def solution(n):
    count = 0
    while n >= 0:
        if n % 5 == 0:
            count += int(n // 5)
            print(count)
            break

        n -= 3
        count += 1
    
    else:
        print(-1)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    solution(n)