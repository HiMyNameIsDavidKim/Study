from ml.stroke import STROKE_MENUS, stroke_menu
from ml.stroke import StrokeService

def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')


if __name__ == '__main__':
    t = StrokeService()
    while True:
        menu = my_menu(STROKE_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")