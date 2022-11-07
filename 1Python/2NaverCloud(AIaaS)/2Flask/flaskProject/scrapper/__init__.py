from scrapper.views import ScrapperController
from util.common import Common

if __name__ == '__main__':
    api = ScrapperController()
    while True:
        menus = ['종료',
                 '벅스뮤직']
        menu = Common.menu(menus)
        if menu == '0':
            api.menu_0(menus[0])
            break
        elif menu == '1': api.menu_1(arg='https://music.bugs.co.kr/chart/track/day/total')
        else :
            print('해당 메뉴 없음. 재입력 하세요.')