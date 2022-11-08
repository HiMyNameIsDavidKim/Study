from scrapper.domains import Scrap
from scrapper.views import ScrapperController
from util.common import Common

BUGS = 'https://music.bugs.co.kr/chart/track/day/total?chartdate='
MELON = 'https://www.melon.com/chart/index.htm?dayTime='

if __name__ == '__main__':
    api = ScrapperController()
    scrap = Scrap()
    while True:
        menus = ['종료',
                 '벅스 뮤직', '멜론']
        menu = Common.menu(menus)
        if menu == '0':
            api.menu_0(menus[0])
            break
        elif menu == '1':
            scrap.domain = BUGS
            scrap.query_string = '20221102'
            scrap.parser = 'lxml'
            scrap.class_names = ['title', 'artist']
            scrap.tag_name = 'p'
            api.menu_1(menus[1], scrap)
        elif menu == '2':
            scrap.domain = MELON
            scrap.query_string = '2022110809'
            scrap.parser = 'lxml'
            scrap.class_names = ['ellipsis rank01', 'ellipsis rank02']
            scrap.tag_name = 'div'
            api.menu_2(menus[2], scrap)
        else :
            print('해당 메뉴 없음. 재입력 하세요.')