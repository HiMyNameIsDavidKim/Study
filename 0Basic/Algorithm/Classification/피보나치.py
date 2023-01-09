def fibo_basic(x):
    if x == 1 or x == 2:
        return 1
    return fibo_basic(x-1) + fibo_basic(x-2)


# 재귀로 구현할 경우 같은 계산을 수없이 반복한다.
# ex) f(3) = f(2) + f(1)
#     f(3) = (f(1) + f(0)) + f(1) : f(1)을 2번 연산함.
# 동적 프로그래밍은 한번 계산한 것은 다시 계산하지 않도록 결과를 메모하며 진행한다.
# d를 추출해보면 계산할 때마다 빈종이에 메모하듯 저장된다.
d = [0] * 50
def fibo_dynamic(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_dynamic(x-1) + fibo_dynamic(x-2)
    return d[x]



if __name__ == '__main__':
    n = int(input("input number : "))
    print(fibo_basic(n))
    print(fibo_dynamic(n))