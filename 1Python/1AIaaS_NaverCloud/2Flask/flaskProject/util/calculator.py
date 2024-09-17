from util.common import Common


class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2
        self.result = self.get_result()

    def __str__(self):
        return f"{self.num1}, {self.op}, {self.num2}, {self.result}"

    def get_result(self):
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/": result = num1 / num2
        elif op == "%": result = num1 % num2
        else: result = "Input Error."
        return result

    @staticmethod
    def new_cal():
        num1 = int(input("첫번째 수 : "))
        op = input("연산자 : ")
        num2 = int(input("두번째 수 : "))
        return Calculator(num1, op, num2)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print_menu()
            if menu == 1:
                print(" ### 등록 ### ")
                ls.append(Calculator.new_cal())
            elif menu == 2:
                print(" ### 목록 ### ")
                Common.get_data(ls)
            elif menu == 3:
                print(" ### 삭제 ### ")
                name = input("Delete what? : ")
                Common.delete_data(ls, name)
            elif menu == 0:
                print(" ### End ### ")
                break
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

Calculator.main()