import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

MPG_MENUS = ["종료",
         "스펙보기", # 1.
         "변수 한글변경", # 2.
         "연비 시각화", # 3.
         "배기량 비교", #4.
         "시내주행 연비비교", #5.
         "고속주행 연비비교", #6.
         "suv/컴팩 중 시내주행평균연비가 높은쪽 출력", #7
         "아우디차에서 고속주행 연비 1~5위 출력", #8.
         "평균연비가 가장 높은 자동차 1~3위 출력" #9.
         ]
mpg_meta = {
    "manufacturer": "회사",
    "model": "모델",
    "displ": "배기량",
    "year": "연식",
    "cyl": "실린더",
    "trans": "차축",
    "drv": "오토",
    "cty": "시내주행",
    "hwy": "고속주행",
    "fl": "연료",
    "class": "차종"
}
mpg_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.visualize(),
    "4" : lambda t: t.compare_displ(),
    "5" : lambda t: t.find_high_cty(),
    "6" : lambda t: t.find_highest_hwy(),
    "7" : lambda t: t.which_cty_in_suv_compact(),
    "8" : lambda t: t.find_top5_hwy_in_audi(),
    "9" : lambda t: t.find_top3_avg(),
}
'''
Data columns (total 12 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Unnamed: 0    234 non-null    int64  
 1   manufacturer : 회사  234 non-null    object 
 2   model : 모델        234 non-null    object 
 3   displ : 배기량         234 non-null    float64
 4   year : 연식         234 non-null    int64  
 5   cyl : 실린더          234 non-null    int64  
 6   trans : 차축        234 non-null    object 
 7   drv : 오토          234 non-null    object 
 8   cty : 시내연비          234 non-null    int64  
 9   hwy : 시외연비          234 non-null    int64  
 10  fl : 연료            234 non-null    object 
 11  class : 차종         234 non-null    object 
dtypes: float64(1), int64(5), object(6)
'''
class MpgService:

    def __init__(self):
        self.mpg = pd.read_csv('data/mpg.csv')
        self.my_mpg = None

    '''
    1.스펙보기
    '''
    def spec(self):
        print(" --- 1.Shape ---")
        print(self.mpg.shape)
        print(" --- 2.Features ---")
        print(self.mpg.columns)
        print(" --- 3.Info ---")
        print(self.mpg.info())
        print(" --- 4.Case Top1 ---")
        print(self.mpg.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.mpg.tail(3))
        print(" --- 6.Describe ---")
        print(self.mpg.describe())
        print(" --- 7.Describe All ---")
        print(self.mpg.describe(include='all'))

    '''
    2.한글 메타데이터
    '''
    def rename_meta(self):
        self.my_mpg = self.mpg.rename(columns=mpg_meta)
        print(" --- 2.Features ---")
        print(self.my_mpg.columns)

    '''
    3.연비 시각화  (mpg 129페이지)
    (1) test 변수 생성 
    (2) 시내주행과 고속주행 변수를 머지(merge)하여 종합연비변수를 생성
    (3) 종합연비가 20이상이면 pass 미만이면 fail 저장
    (4) 종합연비 빈도표 만들기
    (5) 종합연비 막대그래프 그리기
    '''
    def visualize(self): # No.8
        t = self.my_mpg
        t['종합연비'] = (t['시내주행'] + t['고속주행'])/2
        t['종합연비'] = np.where(t['종합연비']>=20, 'pass', 'fail')
        t['종합연비'].value_counts().plot.bar(rot=0)
        plt.savefig('./save/bar_graph.png')
    '''
    4.배기량이 4이하와 5이상 자동차의 고속주행연비 비교 (p.144)
    '''
    def compare_displ(self):
        print(f"배기량이 4 이하 고속주행: {self.my_mpg.query('배기량 <= 4')['고속주행'].mean():.2f}" )
        print(f"배기량이 5 이상 고속주행: {self.my_mpg.query('배기량 >= 5')['고속주행'].mean():.2f}")
    '''
    5.시내주행 연비 평균이 가장 높은 회사는? (p.150)
    '''
    def find_high_cty(self):
        print(f"아우디의 평균 도시연비: %0.2f"% self.my_mpg.query('회사 == "audi"')['시내주행'].mean())
        print(f"토요타의 평균 도시연비: %0.2f"% self.my_mpg.query('회사 == "toyota"')['시내주행'].mean())
    '''
    6.고속주행 연비 평균이 가장 높은 회사는? (p.150)
    '''
    def find_highest_hwy(self):
        all_avg = self.my_mpg.query('회사 in ["chevrolet","ford","honda"]')
        print(f"세 회사의 평균 도시연비:{all_avg['고속주행'].mean():.2f}" )

        # 메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
        # 후 다음 문제 풀이

    '''
    7.suv / 컴팩 자동차 중 어떤 자동차의 도시연비 평균이 더 높은가?? (p.150)
    메타데이터가 category, cty 데이터는 해당 raw 데이터인 객체생성
    '''
    def which_cty_in_suv_compact(self):
        print("suv 자동차의 시내주행: %0.2f"%
              self.my_mpg.query("차종 == 'suv'")['시내주행'].mean())  # clazz가 suv인 행만 추출한 다음 cty 호출 후 그 객체의 평균구함
        print("compact 자동차의 시내주행: %0.2f"% self.my_mpg.query("차종 == 'compact'")['시내주행'].mean())

    '''
    8.고속주행 연비 평균이 가장 높은 회사는? (p.153)
    '''
    def find_top5_hwy_in_audi(self):
        a = self.my_mpg.query("회사 == 'audi'")
        b = a.sort_values(['고속주행'], ascending=False).head()
        print(b.head(1))
    '''
    9.고속주행 연비 평균이 가장 높은 회사는? (p.158)
    '''
    def find_top3_avg(self):
        pass


