from dataclasses import dataclass

x = 10


@dataclass
class OOP:
    x = 30

    def foo(self):
        x = self.x
        print("OOP 출력: "+str(x))


def foo():
    x = 20
    print("FP 출력: "+str(x))


def calc1():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

def calc2():
    a = 3
    b = 5
    return lambda x: a*x + b


if __name__ == '__main__':
    f = OOP()
    f.foo()
    foo()
    print("전역출력: "+str(x))
    c = calc1()
    print(c(1), c(2), c(3), c(4), c(5))
    c = calc2()
    print(c(1), c(2), c(3), c(4), c(5))