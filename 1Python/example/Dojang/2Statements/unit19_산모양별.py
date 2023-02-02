r = int(input())

for i in range(1,(r*2)):
    if i % 2 == 0:
        continue
    print(' '*int(round(r*2-i)/2), '*'*i, sep='')

'''
2 1 2
1 3 1
0 5 0

(5-1)/2 = 2
(5-3)/2 = 1
라운드 걸어야함
'''