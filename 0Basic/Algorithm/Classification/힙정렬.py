# 힙트리 어레이 모양
# 할아버지 / 아버지 / 아들 순으로 정렬됨. 자식은 1, 2, 4, 8로 늘어남.
# ex) [할아버지, 아버지1, 아버지2, 아들1-1, 아들1-2, 아들2-1, 아들2-2]

def heap(arr):
    # 힙트리 구성
    for i in range(len(arr)):
        c = i
        while c != 0:
            r = (c-1)//2 # 아버지가 누군지 찾기 위해 몫을 구함.
            if arr[r] < arr[c]:
                arr[r], arr[c] = arr[c], arr[r]
            c = r
            # print(arr)
    # 힙정렬 구동
    for j in range(len(arr)-1, -1, -1):
        arr[0], arr[j] = arr[j], arr[0]
        r = 0
        c = 1
        while c < j:
            c = 2*r + 1 # 첫째아들
            if (c < j - 1) and (arr[c] < arr[c+1]):
                c += 1 # 둘째아들이 더 크면 둘째아들
            if (c < j) and (arr[r] < arr[c]):
                arr[r], arr[c] = arr[c], arr[r]
            r = c
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
    print(heap(arr))