class Calculator(object): #클래스, (object)를 써줌으로써 클래스 객체가 된다.
    def __init__(self, num1, op, num2):
        self.num1 = num1 #디스크에 있는 num1에 메모리에 있는 num1을 입력해라.
        self.op = op
        self.num2 = num2

    def calc(self): #메서드
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if op == "+": result = num1 + num2 #클래스 안에서는 언제나 셀프로 해줘야함.
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/": result = num1 / num2
        elif op == "%": result = num1 % num2
        else: result = "Input Error."
        print(f"{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    num1 = int(input("First Number : "))
    op = input("Please choose Operator(+,-,*,/,%) : ")
    num2 = int(input("Second Number : "))
    calculator = Calculator(num1, op, num2)
    calculator.calc()
    