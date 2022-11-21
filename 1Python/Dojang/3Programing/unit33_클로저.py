def countdown(n):
    return n

if __name__ == '__main__':
    n = int(input())
    c = countdown(n)
    for i in range(n):
        print(c, end=' ')