from scrapper.domains import MusicRanking
from scrapper.views import ScrapperController
from util.common import Common

BUGS = 'https://music.bugs.co.kr/chart/track/day/total'
MELON ='https://www.melon.com/chart/index.htm'

if __name__ == '__main__':
    api = ScrapperController()
    m = MusicRanking()
    while True:
        menus = ['종료',
                 '벅스 뮤직', '멜론']
        menu = Common.menu(menus)
        if menu == '0':
            api.menu_0(menus[0])
            break
        elif menu == '1':
            m.domain = 'https://music.bugs.co.kr/chart/track/day/total'
            m.query_string = '20221101'
            m.parser = 'lxml'
            m.class_names['title', 'artist']
            m.tag_name = 'p'
            api.menu_1(m)
        else :
            print('해당 메뉴 없음. 재입력 하세요.')