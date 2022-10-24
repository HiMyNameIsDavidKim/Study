class Bmi(object):
    def __init__(self, name, m, kg, index):
        self.name = name
        self.m = m
        self.kg = kg
        self.index = index

    def print(self):
        print(f"이름 : {self.name}\n키 : {self.m}\n몸무게 : {self.kg}\nBMI : {self.index}")

    def print_info(self):
        print(f"{self.name}, {self.m}, {self.kg}, {self.index}")

    @staticmethod
    def get_index(kg, m):
        bmi = kg / (m ** 2)
        if bmi >= 35: index = "고도 비만"
        elif bmi >= 30: index = "중도 비만"
        elif bmi >= 25: index = "경도 비만"
        elif bmi >= 23: index = "과체중"
        elif bmi >= 18.5: index = "정상"
        elif bmi < 18.5: index = "저체중"
        return index

    @staticmethod
    def new_bmi():
        name = input("이름 : ")
        m = float(input("키 : "))
        kg = int(input("몸무게 : "))
        index = Bmi.get_index(kg, m)
        return Bmi(name, m, kg, index)

    @staticmethod
    def get_bmi(ls):
        [i.print_info() for i in ls]

    @staticmethod
    def delete_bmi(ls, name):
        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]

    @staticmethod
    def print_menu():
        print("1. BMI 등록")
        print("2. BMI 출력")
        print("3. BMI 삭제")
        print("4. BMI 종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                print(" ### 등록 ### ")
                ls.append(Bmi.new_bmi())
            elif menu == 2:
                print(" ### 목록 ### ")
                Bmi.get_bmi(ls)
            elif menu == 3:
                print(" ### 삭제 ### ")
                name = input("Delete who? : ")
                Bmi.delete_bmi(ls, name)
            elif menu == 4:
                print(" ### End ### ")
                break
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

Bmi.main()