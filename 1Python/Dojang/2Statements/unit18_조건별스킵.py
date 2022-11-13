start, stop = map(int, input().split())

i = start
while True:
    if i == stop:
        break
    if list(str(i))[-1] == '3':
        i += 1
        continue
    print(i, end=' ')
    i += 1