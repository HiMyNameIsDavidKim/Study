import numpy as np
import pandas as pd

from util.common import Common

MPG_FILE = pd.read_csv('./data/mpg.csv')
MENUS = ['종료',
         '앞부분 확인', '행 열 출력', '데이터 속성 확인', '요약 통계량 확인', '문자 변수 요약 통계량 함께 출력',
         '변수명 바꾸기', '파생변수 만들기', '빈도 확인하기',
         "displ(배기량)이 4이하와 5이상 자동차의 hwy(고속도로 연비) 비교", # 144p 문제
         "아우디와 토요타 중 도시연비(cty) 평균이 높은 회사 검색",
         "쉐보레, 포드, 혼다 데이터 출력과 hwy 전체 평균",
         # mpg 150페이지 문제
         # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
         # 후 다음 문제 풀이
         "suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?",
         # mpg 153페이지 문제
         "아우디차에서 고속도로 연비 1~5위 출력하시오",
         # mpg 158페이지 문제
         "평균연비가 가장 높은 자동차 1~3위 출력하시오"]

class Mpg(object):

    @staticmethod
    def menu_0(*args):
        print(args[0])

    @staticmethod
    def menu_1(*args):
        print(args[0])
        mpg = args[1]
        return print(mpg.head())

    @staticmethod
    def menu_2(*args):
        print(args[0])
        mpg = args[1]
        return print(mpg.tail())

    @staticmethod
    def menu_3(*args):
        print(args[0])
        mpg = args[1]
        return print(mpg.shape)

    @staticmethod
    def menu_4(*args):
        print(args[0])
        mpg = args[1]
        return print(mpg.info())

    @staticmethod
    def menu_5(*args):
        print(args[0])
        mpg = args[1]
        return print(mpg.describe())

    @staticmethod
    def menu_6(*args):
        print(args[0])
        mpg = args[1]
        mpg = mpg.rename(columns={'manufacturer': 'company'})
        return print(mpg.info())

    @staticmethod
    def menu_7(*args):
        print(args[0])
        mpg = args[1]
        mpg = cal_test(mpg)
        return print(mpg.info())

    @staticmethod
    def menu_8(*args):
        print(args[0])
        mpg = args[1]
        mpg = cal_test(mpg)
        count_test = mpg['test'].value_counts()
        return count_test.plot.bar(rot=0).savefig('./save/bar_plot.png')

    @staticmethod
    def menu_9(*args):
        print(args[0])
        mpg = args[1]
        avg1 = mpg.query('displ<=4')['hwy'].mean()
        avg2 = mpg.query('displ>=5')['hwy'].mean()
        return print(f'under 4 average : {avg1}\nover 5 average : {avg2}')

    @staticmethod
    def menu_10(*args):
        print(args[0])
        mpg = args[1]
        avg1 = mpg.query('manufacturer=="audi"')['cty'].mean()
        avg2 = mpg.query('manufacturer=="toyota"')['cty'].mean()
        return print(f'audi average : {avg1}\ntoyota average : {avg2}')

    @staticmethod
    def menu_11(*args):
        print(args[0])
        mpg = args[1]
        my_mpg1 = mpg.query('manufacturer=="chevrolet"')['cty'].mean()
        my_mpg2 = mpg.query('manufacturer=="ford"')['cty'].mean()
        my_mpg3 = mpg.query('manufacturer=="honda"')['cty'].mean()
        return print(f'chevrolet average : {my_mpg1}\nford average : {my_mpg2}\nhonda average : {my_mpg3}')

    @staticmethod
    def menu_12(*args):
        print(args[0])
        mpg = args[1]
        mpg = mpg.rename(columns={'class': 'category'})
        avg1 = mpg.query('category=="suv"')['cty'].mean()
        avg2 = mpg.query('category=="compact"')['cty'].mean()
        return print(f'suv average : {avg1}\ncompact average : {avg2}')

    @staticmethod
    def menu_13(*args):
        print(args[0])
        mpg = args[1]
        audi = mpg.query('manufacturer=="audi"')['hwy']
        return print(audi.nlargest(5, keep='first'))

    @staticmethod
    def menu_14(*args):
        print(args[0])
        mpg = args[1]
        cal_test(mpg)
        model_avg = mpg[['model','total']].groupby(['model'], as_index=False).mean()
        return print(model_avg.nlargest(3, 'total' ,keep='first'))

def cal_test(mpg):
    mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
    mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')
    return mpg


if __name__ == '__main__':
    api = Mpg()
    while True:
        menu = Common.menu(MENUS)
        if menu == '0':
            api.menu_0(MENUS[0])
            break
        elif menu == '1': api.menu_1(MENUS[1], MPG_FILE)
        elif menu == '2': api.menu_2(MENUS[2], MPG_FILE)
        elif menu == '3': api.menu_3(MENUS[3], MPG_FILE)
        elif menu == '4': api.menu_4(MENUS[4], MPG_FILE)
        elif menu == '5': api.menu_5(MENUS[5], MPG_FILE)
        elif menu == '6': api.menu_6(MENUS[6], MPG_FILE)
        elif menu == '7': api.menu_7(MENUS[7], MPG_FILE)
        elif menu == '8': api.menu_8(MENUS[8], MPG_FILE)
        elif menu == '9': api.menu_9(MENUS[9], MPG_FILE)
        elif menu == '10': api.menu_10(MENUS[10], MPG_FILE)
        elif menu == '11': api.menu_11(MENUS[11], MPG_FILE)
        elif menu == '12': api.menu_12(MENUS[12], MPG_FILE)
        elif menu == '13': api.menu_13(MENUS[13], MPG_FILE)
        elif menu == '14': api.menu_14(MENUS[14], MPG_FILE)
        else:
            print(" ### 해당 메뉴 없음 ### ")