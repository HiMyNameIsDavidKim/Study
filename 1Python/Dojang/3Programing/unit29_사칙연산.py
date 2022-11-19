def calc(x,y):
    a = x+y
    s = x/y
    m = x*y
    d = x/y
    return a,s,m,d


if __name__ == '__main__':
    x, y = map(int, input().split())
    a,s,m,d = calc(x,y)
    print(f'add: {a}, sub: {s}, mul: {m}, div: {d}')