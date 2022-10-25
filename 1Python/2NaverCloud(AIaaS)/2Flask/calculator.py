class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2
        self.result = self.get_result()

    def print(self):
        print(f"첫번째 수 : {self.num1}\n연산자 : {self.op}\n두번째 수 : {self.num2}\n계산값 : {self.result}")

    def print_info(self):
        print(f"{self.num1} {self.op} {self.num2} = {self.result}")

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
    def get_cal(ls):
        [i.print_info() for i in ls]

    @staticmethod
    def delete_cal(ls, name):
        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]

    @staticmethod
    def print_menu():
        print("1. 계산값 등록")
        print("2. 계산값 출력")
        print("3. 계산값 삭제")
        print("4. 계산값 종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Calculator.print_menu()
            if menu == 1:
                print(" ### 등록 ### ")
                ls.append(Calculator.new_cal())
            elif menu == 2:
                print(" ### 목록 ### ")
                Calculator.get_cal(ls)
            elif menu == 3:
                print(" ### 삭제 ### ")
                name = input("Delete what? : ")
                Calculator.delete_cal(ls, name)
            elif menu == 4:
                print(" ### End ### ")
                break
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

Calculator.main()