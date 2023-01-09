def insert(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
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
    print(insert(arr))