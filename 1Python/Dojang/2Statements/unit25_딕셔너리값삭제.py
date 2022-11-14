keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

y = {}
for k,v in x.items():
    if (x[k] != 30) and (k != 'delta'): y[k] = v
print(y)