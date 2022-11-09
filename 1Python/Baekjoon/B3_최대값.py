def solution():
    m = max(arr)
    count = 1
    for k in arr:
        if k == m:
            print(m)
            print(count)
            break
        count += 1

if __name__ == "__main__":
    arr = []
    for i in range(9):
        num = int(input("input number : "))
        arr.append(num)
    solution()