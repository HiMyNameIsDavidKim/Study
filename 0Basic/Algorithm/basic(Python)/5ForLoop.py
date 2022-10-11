def solution() :
    money = 1660
    count = 0
    a = [500, 100, 50, 10]
    for i in a :
        count = money // i
        money %= i
        print(f"{i}원짜리 {count}개")

if __name__ == "__main__" :
    solution()






