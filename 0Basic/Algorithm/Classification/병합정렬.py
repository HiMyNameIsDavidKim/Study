def merge(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    low_arr = merge(arr[:mid])
    high_arr = merge(arr[mid:])
    result = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            result.append(low_arr[l])
            l += 1
        else:
            result.append(high_arr[h])
            h += 1
    result += low_arr[l:]
    result += high_arr[h:]
    # print(result)
    return result


import random
def randarr(n):
    arr = []
    for _ in range(n):
        arr.append(random.randrange(1, 11))
    return arr


if __name__ == '__main__':
    arr = randarr(8)
    print(arr)
    print(merge(arr))