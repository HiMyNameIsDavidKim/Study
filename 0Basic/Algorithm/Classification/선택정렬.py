def select(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                t = arr[j]
                arr[j] = arr[min]
                arr[min] = t
                # print(arr)
    return arr

import random
def randarr(n):
    arr = []
    for _ in range(n):
        arr.append(random.randrange(1, 11))
    return arr


if __name__ == '__main__':
    arr = randarr(10)
    print(arr)
    print(select(arr))