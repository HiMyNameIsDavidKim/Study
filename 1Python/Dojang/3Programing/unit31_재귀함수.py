def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    n = int(input())
    print(fib(n))

'''
0과 1로 시작하며 -> 구현
바로 앞 두 수의 합이다 -> 구현
'''