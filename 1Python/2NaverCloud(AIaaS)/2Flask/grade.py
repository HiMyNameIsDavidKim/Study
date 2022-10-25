class Grade(object):
    def __init__(self, kr, en, ma):
        self.kr = kr
        self.en = en
        self.ma = ma
        self.grade = self.calc_grade()

    def print(self):
        print(f"국어 : {self.kr}\n영어 : {self.en}\n수학 : {self.ma}\n학점 : {self.grade}")

    def print_info(self):
        print(f"{self.kr}, {self.en}, {self.ma}, {self.grade}")

    def calc_grade(self):
        avg = round((self.kr + self.en + self.ma)/3)
        grade = ""
        if avg >= 90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        elif avg >= 50: grade = "E"
        elif avg < 50: grade = "F"
        return grade


    @staticmethod
    def new_grade():
        kr = int(input("Please input your Korean score : "))
        en = int(input("Please input your English score : "))
        ma = int(input("Please input your Math score : "))
        return Grade(kr, en, ma)

    @staticmethod
    def get_grade(ls):
        [i.print_info() for i in ls]

    @staticmethod
    def delete_grade(ls, name):
        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]

    @staticmethod
    def print_menu():
        print("1. 학점 등록")
        print("2. 학점 출력")
        print("3. 학점 삭제")
        print("4. 학점 종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                print(" ### 등록 ### ")
                ls.append(Grade.new_grade())
            elif menu == 2:
                print(" ### 목록 ### ")
                Grade.get_grade(ls)
            elif menu == 3:
                print(" ### 삭제 ### ")
                name = input("Delete what? : ")
                Grade.delete_grade(ls, name)
            elif menu == 4:
                print(" ### End ### ")
                break
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

Grade.main()