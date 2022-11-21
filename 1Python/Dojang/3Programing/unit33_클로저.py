def countdown(n):
    a = -1
    def lamb():
        nonlocal a
        a += 1
        return n-a
    return lamb

if __name__ == '__main__':
    n = int(input())
    c = countdown(n)
    for i in range(n):
        print(c(), end=' ')