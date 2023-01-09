def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    low, equal, high = [], [], []
    for i in arr:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        else:
            equal.append(i)
    # print(arr)
    return quick(low) + equal + quick(high)



import random
def randarr(n):
    arr = []
    for _ in range(n):
        arr.append(random.randrange(1, 11))
    return arr


if __name__ == '__main__':
    arr = randarr(11)
    print(arr)
    print(quick(arr))