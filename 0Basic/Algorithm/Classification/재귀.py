"""
카운트 다운.
"""
def countdown(n):
    if n <= 0:
        print('발사!')
    else:
        print(n)
        countdown(n-1)

countdown(3)



"""
n개 원소의 합 출력.
sum5 = 1 + sum4
sum4 = 3 + sum3
sum3 = 5 + sum2
sum2 = 7 + sum1
sum1 = 9
"""
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1, 3, 5, 7, 9]))



"""
n개의 원소 중 4개를 고르는 모든 경우의 수 출력.
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                result.append([i, j, k, l])
"""
def pick(n, picked, to_pick):
    if to_pick == 0:
        print(picked)

    if picked == []: 
        i = 0
    else: 
        i = picked[-1] + 1

    for j in range(i, n):
        picked.append(j)
        pick(n, picked, to_pick-1)
        picked.pop(-1)
        
print(pick(7, [], 4))