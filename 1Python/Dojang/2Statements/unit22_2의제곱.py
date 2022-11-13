start, stop = map(int, input().split())

for i in range(start, stop+1):
    print(f'{2**i}', end=' ')