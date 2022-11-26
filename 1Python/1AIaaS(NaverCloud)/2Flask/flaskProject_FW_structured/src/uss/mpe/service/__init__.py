from src.uss.mpe.service.bmi import Bmi
from src.cmm.com.service.common import Common

ls = []
while True:
    menu = Common.menu(["종료","BMI","주소록","성적표","개인정보"])
    if menu == 0:
        print("### 앱 종료 ###")
        break
    elif menu == 1:
        print("### BMI ###")
        submenu = Common.menu(["종료", "BMI등록", "BMI목록", "BMI삭제"])
        if submenu == 0: break
        elif submenu == 1:
            biman = Bmi.new_bmi()
            ls.append(biman)
        elif submenu == 2:
            Bmi.result(ls)
        elif submenu == 2:
            name = input("삭제할 이름: ")
            Bmi.del_bmi(ls, name)
    elif menu == 2:
        print("### 주소록 ###")
    elif menu == 3:
        print("### 성적표 ###")
    elif menu == 4:
        print("### 개인정보 ###")
    else:
        print("잘못된 메뉴 번호 입니다.")
