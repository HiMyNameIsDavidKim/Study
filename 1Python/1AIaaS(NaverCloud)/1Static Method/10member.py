"""
아이디, 비번, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발하시오.
"""

class Member(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name

    def print(self):
        pass

    @classmethod
    def new_member(self):
        pass

    @classmethod
    def get_member(self):
        pass

    @classmethod
    def delete_member(self):
        pass

    @staticmethod
    def print_menu():
        print("1.회원가입")
        print("2.목록")
        print("3.회원탈퇴")
        print("0.종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print("### 가입 ###")
                ls.append(Member.new_member())
            elif menu == 2:
                print("### 목록 ###")
                Member.get_member()
            elif menu == 3:
                print("### 탈퇴 ###")
                Member.delete_member()
            elif menu == 0:
                print("### 종료 ###")
                break
            else:
                print("없는 메뉴 입니다. 다시 입력 해주세요.")

Member.main()