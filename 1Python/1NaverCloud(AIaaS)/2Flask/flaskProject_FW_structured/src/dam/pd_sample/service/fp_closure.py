from dataclasses import dataclass

@dataclass
class OOP:
    x = 30

    def foo(self):
        x = self.x
        print("OOP 출력: "+str(x))
x = 10
def foo():
    global x
    x = x + 20
    print("FP 출력: "+str(x))


def A():
    x = 10
    y = 100

    def B():
        x = 20

        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)

        C()

    B()


A()

x = 1


def A():
    x = 10

    def B():
        x = 20

        def C():
            global x  #
            x = x + 30
            print(x)

        C()

    B()


A()


def Calc():
    a = 3
    b = 5
    t = 0
    def mul_add(x):
        nonlocal t
        t =  t + (a * x + b)
        print("클로저 1 결과: "+str(t))

    def mul_add_2(x):
        nonlocal t
        t = t + (a * x - b)
        print("클로저 2 결과: " + str(t))

    return {"덧셈1":mul_add,"덧셈2":mul_add_2}

if __name__ == '__main__':
    f = OOP()
    f.foo()
    foo()
    print("전역출력: " + str(x))
    A()
    c = Calc()
    print("클로저1: "+str(c["덧셈1"](2))) # 예상치 11
    print("클로저2: " + str(c["덧셈2"](2)))  # 예상치 1






