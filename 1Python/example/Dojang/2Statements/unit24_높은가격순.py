x = list(map(int, input().split(';')))

x.sort(reverse=True)
for i in x:
    print(f'{i:>9,}')