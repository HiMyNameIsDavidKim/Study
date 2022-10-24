from datetime import *

class Person(object):
    def __init__(self, name, pnum, addr):
        self.name = name
        self.pnum = pnum
        self.addr = addr
        self.age = self.get_age()
        self.gender = self.get_gender()

    def print(self):
        print(f"이름 : {self.name}\n주소 : {self.addr}\n나이 : {self.age}\n성별 : {self.gender}")

    def print_info(self):
        print(f"{self.name}, {self.addr}, {self.age}, {self.gender}")

    def get_age(self):
        pnum = self.pnum
        if int(pnum[0:2]) < datetime.today().year-1999:
            age = datetime.today().year-1999-int(pnum[0:2])
        elif int(pnum[0:2]) >= datetime.today().year-1999:
            age = 100-int(pnum[0:2])+datetime.today().year-1999
        return age

    def get_gender(self):
        pnum = self.pnum
        if (int(pnum[7]) == 1) or (int(pnum[7]) == 3): gender = "Male"
        elif (int(pnum[7]) == 2) or (int(pnum[7]) == 4): gender = "Female"
        return gender

    @staticmethod
    def new_intro():
        name = input("Please type your name : ")
        pnum = input("Please type your Personal Number : ")
        addr = input("Please type your address : ")
        return Person(name, pnum, addr)

    @staticmethod
    def get_intro(ls):
        [i.print_info() for i in ls]

    @staticmethod
    def delete_intro(ls, name):
        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]

    @staticmethod
    def print_menu():
        print("1. 자기소개 등록")
        print("2. 자기소개 출력")
        print("3. 자기소개 삭제")
        print("4. 자기소개 종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Person.print_menu()
            if menu == 1:
                print(" ### 등록 ### ")
                ls.append(Person.new_intro())
            elif menu == 2:
                print(" ### 목록 ### ")
                Person.get_intro(ls)
            elif menu == 3:
                print(" ### 삭제 ### ")
                name = input("Delete what? : ")
                Person.delete_intro(ls, name)
            elif menu == 4:
                print(" ### End ### ")
                break
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

Person.main()