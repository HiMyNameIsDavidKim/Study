class Contact(object):
    def __init__(self, name, pnum, mail, addr):
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.addr = addr

    def print(self):
        print(f"이름: {self.name}\n전화번호: {self.pnum}\n이메일: {self.mail}\n주소: {self.addr}")

    def print_info(self):
        print(f"{self.name}, {self.pnum}, {self.mail}, {self.addr}")

    @staticmethod
    def new_contact():
        name = input("이름: ")
        phone_number = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        return Contact(name, phone_number, email, address)

    @staticmethod
    def get_contact(ls):
        [i.print_info() for i in ls]

    @staticmethod
    def delete_contact(ls, name):
        # for i, j in enumerate(ls):
        #     if j.name == name:
        #         del ls[i]

        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]

    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 연락처 종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print(" ### 등록 ### ")
                ls.append(Contact.new_contact())
            elif menu == 2:
                print(" ### 목록 ### ")
                Contact.get_contact(ls)
            elif menu == 3:
                print(" ### 삭제 ### ")
                name = input("Delete who? : ")
                Contact.delete_contact(ls, name)
            elif menu == 4:
                print(" ### End ### ")
                break
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

Contact.main()