def comb(arr, n):
    result = []
    if n > len(arr):
        return f'잘못된 입력입니다.'
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result


def per(arr, n):
    result = []
    if n > len(arr):
        return f'잘못된 입력입니다.'
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for j in per(ans, n-1):
                result.append([arr[i]] + j)
    return result


if __name__ == '__main__':
    print(comb([1,2,3,4], 2))
    print(per([1,2,3,4], 2))