import pandas as pd

from mypandas.mpg import Mpg
from util.common import Common

MPG_FILE = pd.read_csv('./data/mpg.csv')

if __name__ == '__main__':
    api = Mpg()
    while True:
        menus = ['종료',
                 '앞부분 확인', '행 열 출력', '데이터 속성 확인', '요약 통계량 확인', '문자 변수 요약 통계량 함께 출력']
        menu = Common.menu(menus)
        if menu == '0':
            api.menu_0(menus[0])
            break
        elif menu == '1': api.menu_1(menus[1], MPG_FILE)
        elif menu == '2': api.menu_2(menus[2], MPG_FILE)
        elif menu == '3': api.menu_3(menus[3], MPG_FILE)
        elif menu == '4': api.menu_4(menus[4], MPG_FILE)
        elif menu == '5': api.menu_5(menus[5], MPG_FILE)
        else:
            print(" ### 해당 메뉴 없음 ### ")