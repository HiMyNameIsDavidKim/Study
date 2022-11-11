import pandas as pd

MW_FILE = pd.read_csv('./data/midwest.csv')
MENUS = ['종료',
         '메타데이터 출력',
         'poptotal, popasian 변수를 total, asian으로 이름 변경',
         '전체 인구 대비 아시아 인구 백분을 변수 추가',
         '아시아 인구 백분의 전체 평균 초과 = large, 이하 = small로 분류',
         'large, small 빈도표와 빈도막대그래프 작성']


def ctr_menu(ls):
    [print(f'{i}. {j}') for i, j in enumerate(ls)]
    return input('메뉴를 선택하세요 : ')


class Midwest(object):

    def __init__(self):
        self.mw = MW_FILE

    def cmd_1(self, *args):
        print(args[0])
        df = self.mw
        return df.columns

    def cmd_2(self, *args):
        print(args[0])
        df = self.mw
        df = self.del_pop(df)
        return df.columns

    def cmd_3(self, *args):
        print(args[0])
        df = self.mw
        df = self.del_pop(df)
        df = self.cal_asian_ratio(df)
        return df

    def cmd_4(self, *args):
        print(args[0])
        df = self.mw
        df = self.del_pop(df)
        df = self.cal_asian_ratio(df)
        df = self.avg_clf(df)
        return df

    def cmd_5(self, *args):
        print(args[0])
        df = self.mw
        df = self.del_pop(df)
        df = self.cal_asian_ratio(df)
        df = self.avg_clf(df)
        large = len(df.loc[df['classify']=='large'])
        small = len(df.loc[df['classify']=='small'])
        print(f'{large}, {small}')


    @staticmethod
    def del_pop(df) -> object:
        df.rename(columns={'poptotal': 'total'}, inplace=True)
        df.rename(columns={'popasian': 'asian'}, inplace=True)
        return df

    @staticmethod
    def cal_asian_ratio(df) -> object:
        df['asian_ratio'] = (df['asian']/df['total'])*100
        return df

    @staticmethod
    def avg_clf(df) -> object:
        avg = df['asian_ratio'].mean()
        df['classify'] = ['large' if i>avg else 'small' for i in df['asian_ratio']]
        return df


if __name__ == '__main__':
    mw = Midwest()
    while True:
        cmd = ctr_menu(MENUS)
        if cmd == '0':
            print(MENUS[0])
            break
        elif cmd == '1': print(mw.cmd_1(MENUS[1]))
        elif cmd == '2': print(mw.cmd_2(MENUS[2]))
        elif cmd == '3': print(mw.cmd_3(MENUS[3]))
        elif cmd == '4': print(mw.cmd_4(MENUS[4]))
        elif cmd == '5': print(mw.cmd_5(MENUS[5]))
        else :
            print('존재하지 않는 메뉴입니다. 다시 선택하세요.')