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
            elif menu == 1:
                print("등록")
            elif menu == 2:
                print("목록")
            elif menu == 3:
                print("검색")
            elif menu == 4:
                print("수정")
            elif menu == 5:
                print("삭제")
            else: print("There is no menu. Please type again.")

        
Calculator.main()