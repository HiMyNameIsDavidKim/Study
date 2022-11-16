import googlemaps
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

CRIME_MENUS = ["Exit", #0
                "Spec",#1
                "Merge",#2
                "Interval",#3
                "Norminal",#4
                "Target",#5
                "partition",#6
                "Fit",#7
                "Predicate"#8
]
crime_meta = {'관서명', '살인 발생', '살인 검거', '강도 발생',
               '강도 검거', '강간 발생', '강간 검거', '절도 발생',
               '절도 검거', '폭력 발생', '폭력 검거'
}
crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.norminal_variables(),
    "5" : lambda t: print(" ** No Function ** "),
    "6" : lambda t: print(" ** No Function ** "),
    "7" : lambda t: print(" ** No Function ** "),
    "8" : lambda t: print(" ** No Function ** ")
}
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 31 entries, 0 to 30
Data columns (total 11 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   관서명     31 non-null     object
 1   살인 발생   31 non-null     int64 
 2   살인 검거   31 non-null     int64 
 3   강도 발생   31 non-null     int64 
 4   강도 검거   31 non-null     int64 
 5   강간 발생   31 non-null     int64 
 6   강간 검거   31 non-null     int64 
 7   절도 발생   31 non-null     object
 8   절도 검거   31 non-null     object
 9   폭력 발생   31 non-null     object
 10  폭력 검거   31 non-null     object
dtypes: int64(6), object(5)
'''

class CrimeService:
    def __init__(self):
        self.crime = pd.read_csv('./data/crime_data/crime_in_seoul.csv')
        self.cctv = pd.read_csv('./data/crime_data/cctv_in_seoul.csv')
        self.my_crime = None
        self.my_cctv = None
        self.target = None
        self.data = None
    '''
    1.스펙보기
    '''
    def spec(self):
        [(lambda x: print(f' --- 2.Spec ---\n'
                          f'--- 1)Shape ---\n{x.shape}\n'
                          f'--- 2)Features ---\n{x.columns}\n'
                          f'--- 3)Info ---\n{x.info()}\n'
                          f'--- 4)Case Top1 ---\n{x.head(1)}\n'
                          f'--- 5)Case Bottom1 ---\n{x.tail(3)}\n'
                          f'--- 6)Describe ---\n{x.describe()}\n'
                          f'--- 7)Describe All ---\n{x.describe(include="all")}'))(i)
        for i in [self.crime, self.cctv]]
    '''
    2.주소 추출
    '''
    def save_police_pos(self):
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f'관서명,지역명 : {name},{name[:-1]}')
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f'서울 시내 경찰서는 총 {len(station_names)}개 있어요.')
        print(f'--- 서울시내 경찰서 목록 ---')
        [print(i) for i in station_names]
        print(f'--- API에서 주소추출 시작 ---')

        gmaps = (lambda x: googlemaps.Client(key=x))("")
        print(gmaps.geocode('서울중부경찰서', language='ko'))
        print('--- API에서 주소추출 시작 ---')
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language='ko')
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append((_loc['location']['lat']))
            station_lngs.append((_loc['location']['lng']))
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_csv('./save/police_pos.csv',index=False)

    '''
    (option) 메타데이터 해석
    '''
    def rename_meta(self):
        self.my_crime = self.crime.rename(columns=crime_meta)
        print(" --- 2.Features ---")
        print(self.my_crime.columns)
    '''
    3~4.interval, ratio, norminal, ordinal
    '''
    def interval_variables(self):
        t = self.crime
        print(" --- 3-1.Interval ---")
        self.crime = t
        self.spec()

    def ratio_variables(self): # 해당 컬럼이 없음
        t = self.crime
        print(" --- 3-2.Ratio ---")
        self.crime = t
        self.spec()

    def norminal_variables(self):
        t = self.crime
        print(" --- 4-1.Norminal ---")
        self.crime = t
        self.spec()

    def ordinal_variables(self): # 해당 컬럼이 없음
        t = self.crime
        print(" --- 4-2.Ordinal ---")
        self.crime = t
        self.spec()