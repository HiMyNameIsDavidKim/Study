from canny_funtional.views import MenuController
from util.common import Common
LENNA = 'Lenna.png'
SOCCER = 'https://docs.opencv.org/4.x/roi.jpg'
BUILDING = 'http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png'

if __name__ == '__main__':
    api = MenuController()
    while True:
        menus = ['종료', '원본 보기', '그레이 스케일', '엣지 검출', '직선 검출']
        menu = Common.menu(menus)
        if menu == '0':
            api.menu_0(menus[0])
            break
        elif menu == '1': api.menu_1(menus[1], LENNA)
        elif menu == '2': api.menu_2(menus[2], SOCCER)
        elif menu == '3': api.menu_3(menus[3], SOCCER)
        elif menu == '4': api.menu_4(menus[4], BUILDING)
        else:
            print(' ### 해당 메뉴 없음 ### ')