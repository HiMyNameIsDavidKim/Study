class Contact(object):
    def __init__(self, name, pnum, mail, addr):
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.addr = addr

    def print(self):
        print(f"{self.name} {self.pnum} {self.mail} {self.addr}")

    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        return int(input("메뉴 선택 : "))

    @staticmethod
    def new_contact():
        name = input("이름 : ")
        pnum = input("연락처 : ")
        mail = input("이메일 :")
        addr = input("주소 : ")
        return Contact(name, pnum, mail, addr)

    @staticmethod
    def print_result(ls):
        print("### 연락처 ###")
        print("**********************")
        print("이름 연락처 이메일 주소")
        print("**********************")
        for i in ls:
            i.print()
        print("**********************")
    @staticmethod
    def delete(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print("연락처 등록")
                ls.append(Contact.new_contact())
            elif menu == 2:
                print("연락서 출력")
                Contact.print_result(ls)
            elif menu == 3:
                print("연락서 삭제")
                Contact.delete(ls, input("삭제할 이름 : "))
            elif menu == 4:
                print("종료")
                break
            else: print("잘못된 입력")

Contact.main()