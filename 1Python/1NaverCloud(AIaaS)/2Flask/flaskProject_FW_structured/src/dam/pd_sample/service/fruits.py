from string import ascii_lowercase

import numpy as np
import pandas as pd

MENUS = ["종료","과일2D","숫자2D"]
def new_fruits_df():
    ls1 = ['제품','가격','판매량'] # 스키마
    ls2 = ['사과', '딸기', '수박'] # 제품
    ls3 = [1800, 1500, 3000] # 가격
    ls4 = [30, 40, 50] # 판매량
    ls5 = [ls2, ls3, ls4]
    df = pd.DataFrame(
        {j : ls5[i] for i, j in enumerate(ls1)})
    print(df)
    print('가격평균: '+str(df['가격'].mean()))
    print('판매량평균: '+str(df['판매량'].mean()))


def my_list(a, b):
    return list(range(a,b))
def new_number_2d():
    df = pd.DataFrame(np.array([list(range(1,11)),
                                list(range(11,21)),
                                list(range(21,31))]),
                      columns=list(ascii_lowercase)[0:10])
    print(df)

if __name__ == '__main__':

    new_fruits_df()
    menus = ['종료','과일', '숫자 2d']
    while True:
        menu = [print(f'{i}. {j}') for i, j in enumerate(menus)]
        num = input("메뉴 : ")
        if num == '0':
            break
        elif num == '1':
            new_fruits_df()
        elif num == '2':
            new_number_2d()