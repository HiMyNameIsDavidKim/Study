from CVbasic_funtional.views import MenuController
from util.common import Common
LENNA = 'Lenna.png'
SOCCER = 'https://docs.opencv.org/4.x/roi.jpg'
BUILDING = 'http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png'
GIRL = 'girl.jpg'
GIRL_INCLINED = 'girl_inclined.png'
GIRL_SIDE_FACE = 'girl_side_face.jpg'
GIRL_WITH_MOM = 'girl_with_mom.jpg'
HAAR = 'haarcascade_frontalface_alt.xml'
CAT = 'cat.jpg'
FACE_TARGET = ''
FACE_OBJECT = ''

if __name__ == '__main__':
    api = MenuController()
    while True:
        menus = ['종료',
                 '원본 보기', '그레이 스케일', '엣지 검출', '직선 검출', '얼굴 검출', '소녀 모자이크', '모녀 모자이크']
        menu = Common.menu(menus)
        if menu == '0':
            api.menu_0(menus[0])
            break
        elif menu == '1': api.menu_1(menus[1], LENNA)
        elif menu == '2': api.menu_2(menus[2], SOCCER)
        elif menu == '3': api.menu_3(menus[3], SOCCER)
        elif menu == '4': api.menu_4(menus[4], BUILDING)
        elif menu == '5': api.menu_5(menus[5], HAAR, GIRL)
        elif menu == '6': api.menu_6(menus[6], HAAR, GIRL)
        elif menu == '7': api.menu_6(menus[7], HAAR, GIRL_WITH_MOM)
        else:
            print(' ### 해당 메뉴 없음 ### ')