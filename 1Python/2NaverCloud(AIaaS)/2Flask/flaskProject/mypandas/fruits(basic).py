import string

import numpy as np
import pandas as pd

MENUS = ['종료',
         '과일2D', '숫자2D']

def menu(ls):
    [print(f'{i}.{j}') for i, j in enumerate(ls)]
    return input('메뉴 선택 : ')

def new_fruits_2d():
    sc = ['제품', '가격', '판매량']
    ls1 = ['사과', '딸기', '수박']
    ls2 = [1800, 1500, 3000]
    ls3 = [24, 38, 13]
    dc = {sc[i]: j for i, j in enumerate([ls1, ls2, ls3])}
    df = pd.DataFrame(dc)
    return f'가격 평균 : {df["가격"].mean()}\n' \
           f'판매량 평균 : {df["판매량"].mean()}'

def new_number_2d():
    df = pd.DataFrame([range(1,11), range(11,21), range(21,31)],
                      columns=list(string.ascii_lowercase)[0:10])
    return df


if __name__ == '__main__':
    while True:
        cmd = menu(MENUS)
        if cmd == '0':
            print(MENUS[0])
            break
        elif cmd == '1':
            print(MENUS[1])
            print(new_fruits_2d())
        elif cmd == '2':
            print(MENUS[2])
            print(new_number_2d())