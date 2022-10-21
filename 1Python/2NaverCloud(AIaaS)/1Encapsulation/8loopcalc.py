def print_menu():
    pass


class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/": result = num1 / num2
        elif op == "%": result = num1 % num2
        else: result = "Input Error."
        print(f"{num1} {op} {num2} = {result}")

    @staticmethod
    def main():
        ls = []
        while True:
            menu = print_menu()
            if menu == 0: break
            elif menu == 1: pass
        num1 = int(input("First Number : "))
        op = input("Please choose Operator(+,-,*,/,%) : ")
        num2 = int(input("Second Number : "))
        calculator = Calculator(num1, op, num2)
        calculator.calc()
        
Calculator.main()