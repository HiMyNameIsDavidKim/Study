def prime_number_generator(start, stop):
    x = []
    rep = stop - start + 1
    for i in range(rep):
        num = start+i
        x.append(num)
    yield from x

if __name__ == '__main__':
    start, stop = map(int, input().split())
    g = prime_number_generator(start, stop)
    print(type(g))
    for i in g:
        print(i, end= ' ')