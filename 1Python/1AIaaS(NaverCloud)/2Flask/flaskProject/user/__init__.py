from user.bmi import Bmi
from user.contact import Contact
from user.grade import Grade
from user.person import Person
from util.common import Common

while True:
    ls =[]
    menu = Common.print_menu(["종료", "Bmi", "Contact", "Grade", "Person"])
    if menu == 0:
        print(" ### 종료 ###")

    elif menu == 1:
        while True:
            submenu = Common.print_menu(["종료", "BMI 등록", "BMI 출력", "BMI 삭제"])
            if submenu == 0:
                print(f" ### 종료 ### ")
                break
            elif submenu == 1:
                print(f" ### BMI 등록 ### ")
                ls.append(Bmi.new_bmi())
            elif submenu == 2:
                print(f" ### BMI 출력 ### ")
                Common.get_data(ls)
            elif submenu == 3:
                print(f" ### BMI 삭제 ### ")
                name = input("Delete what? : ")
                Common.delete_data(ls, name)
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

    elif menu == 2:
        while True:
            submenu = Common.print_menu(["종료", "연락처 등록", "연락처 출력", "연락처 삭제"])
            if submenu == 0:
                print(f" ### 종료 ### ")
                break
            elif submenu == 1:
                print(f" ### 연락처 등록 ### ")
                ls.append(Contact.new_contact())
            elif submenu == 2:
                print(f" ### 연락처 출력 ### ")
                Common.get_data(ls)
            elif submenu == 3:
                print(f" ### 연락처 삭제 ### ")
                name = input("Delete what? : ")
                Common.delete_data(ls, name)
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

    elif menu == 3:
        while True:
            submenu = Common.print_menu(["종료", "성적 등록", "성적 출력", "성적 삭제"])
            if submenu == 0:
                print(" ### End ### ")
                break
            elif submenu == 1:
                print(" ### 등록 ### ")
                ls.append(Grade.new_grade())
            elif submenu == 2:
                print(" ### 목록 ### ")
                Common.get_data(ls)
            elif submenu == 3:
                print(" ### 삭제 ### ")
                name = input("Delete what? : ")
                Common.delete_data(ls, name)
            else:
                print("없는 메뉴입니다. 다시 선택하세요")

    elif menu == 4:
        while True:
            submenu = Common.print_menu(["종료", "개인정보 등록", "개인정보 출력", "개인정보 삭제"])
            if submenu == 0:
                print(" ### End ### ")
                break
            elif submenu == 1:
                print(" ### 등록 ### ")
                ls.append(Person.new_intro())
            elif submenu == 2:
                print(" ### 목록 ### ")
                Common.get_data(ls)
            elif submenu == 3:
                print(" ### 삭제 ### ")
                name = input("Delete what? : ")
                Common.delete_data(ls, name)
            else:
                print("없는 메뉴입니다. 다시 선택하세요")
    else:
        print("없는 메뉴입니다. 다시 선택하세요")