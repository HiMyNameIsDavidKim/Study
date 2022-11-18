import googlemaps
import folium
import pandas as pd
import numpy as np
import json
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

CRIME_MENUS = ["Exit", #0
                "Spec",#1
                "Save police position",#2
                "Save cctv pop",#3
                "Save police norm",#4
                "Folium example",#5
                "Save seoul folium",#6
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
    "3" : lambda t: t.save_cctv_pop(),
    "4" : lambda t: t.save_police_norm(),
    "5" : lambda t: t.folium_example(),
    "6" : lambda t: t.save_seoul_folium(),
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
        self.pop = pd.read_excel('./data/crime_data/pop_in_seoul.xls', sheet_name='YainSoft_Excel1',
                                 usecols=['자치구', '합계', '한국인', '등록외국인', '65세이상고령자'], skiprows = [0,2,3])
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
        self.my_crime = None
        self.my_cctv = None
        self.my_pop = None
        self.target = None
        self.data = None
        self.ls = [self.crime, self.cctv, self.pop]
        self.us_states = './data/us-states.json'
        self.us_unemployment = pd.read_csv('./data/us_unemployment.csv')
        self.kr_states = './data/kr-state.json'
        print(self.kr_states)
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
        for i in self.ls]
    '''
    2.주소 추출
    '''
    def save_police_pos(self):
        cols = ['절도 발생', '절도 검거', '폭력 발생', '폭력 검거']
        self.crime[cols] = self.crime[cols].replace(',','',regex=True).astype(int)
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f'관서명,지역명 : {name},{name[:-1]}')
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f'서울 시내 경찰서는 총 {len(station_names)}개 있어요.')
        print(f'--- 서울시내 경찰서 목록 ---')
        [print(i) for i in station_names]

        gmaps = (lambda x: googlemaps.Client(key=x))("AIzaSyBRTgavFkgMT33WCn1x5r81D7_-DV38wVc")
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
        crime.loc[19,'구별'] = '강서구'
        # crime.to_csv('./save/police_pos.csv',index=False)
        crime.to_pickle('./save/police_pos.pkl')
    '''
    3.cctv 상관관계 확인
    '''
    def save_cctv_pop(self):
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)
        pop.rename(columns=
                   {pop.columns[0]: '구별',
                    pop.columns[1]: '인구수',
                    pop.columns[2]: '한국인',
                    pop.columns[3]: '외국인',
                    pop.columns[4]: '고령자',
                    }, inplace=True)
        print('*'*100)
        pop.drop(index=25, inplace=True)
        pop['외국인비율'] = pop['외국인'].astype(int)/pop['인구수'].astype(int)*100
        pop['고령자비율'] = pop['고령자'].astype(int)/pop['인구수'].astype(int)*100
        cctv.drop(['2013년도 이전','2014년','2015년','2016년'], axis=1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on='구별')
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        '''
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계            
        '''
    '''
    4.노멀라이제이션
    '''
    def save_police_norm(self):
        police_pos = pd.read_pickle('./save/police_pos.pkl')
        police = pd.pivot_table(police_pos,index='구별',aggfunc=np.sum)
        police['살인검거율'] = (police['살인 검거'].astype(int) / police['살인 발생'].astype(int)) * 100
        police['강도검거율'] = (police['강도 검거'].astype(int) / police['강도 발생'].astype(int)) * 100
        police['강간검거율'] = (police['강간 검거'].astype(int) / police['강간 발생'].astype(int)) * 100
        police['절도검거율'] = (police['절도 검거'].astype(int) / police['절도 발생'].astype(int)) * 100
        police['폭력검거율'] = (police['폭력 검거'].astype(int) / police['폭력 발생'].astype(int)) * 100
        police.drop(columns={'살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거'}, axis=1, inplace=True)
        for i in self.crime_rate_columns:
            police.loc[police[i] > 100, 1] = 100 # 데이터값의 기간 오류로 100을 넘으면 100으로 계산
        police.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        x = police[self.crime_rate_columns].values
        min_max_scalar = preprocessing.MinMaxScaler()
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        police_norm = pd.DataFrame(x_scaled,columns=self.crime_columns,index=police.index)
        police_norm[self.crime_rate_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns], axis=1)
        # police_norm.reset_index(drop=False,inplace=True)
        police_norm.to_pickle('./save/police_norm.pkl')
    '''
    5.폴리움 지도 그리기
    '''
    def folium_example(self):
        us_unemployment = self.us_unemployment
        url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
        geo_data = f"{url}/us-states.json"
        state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
        data = pd.read_csv(state_unemployment)
        bins = list(us_unemployment["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))
        map = folium.Map(location=[48, -102], zoom_start=5)
        folium.Choropleth(
            geo_data=geo_data, # us_states,
            data=data, #us_unemployment,
            name="choropleth",
            columns=["State","Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name='Unemployment Rate (%)',
            bins=bins
        ).add_to(map)
        map.save("./save/unemployment.html")

    def save_seoul_folium(self):
        geo_data = self.kr_states
        data = self.create_folium_data()
        map = folium.Map(location=[37.5502, 126.982], zoom_start=12)
        folium.Choropleth(
            geo_data=geo_data,  # us_states,
            data=data,  # us_unemployment,
            name="choropleth",
            columns=["State", "Crime Rate"],
            key_on="feature.id",
            fill_color="PuRd",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Crime Rate (%)'
        ).add_to(map)
        map.save("./save/crime_rate.html")

    def create_folium_data(self):
        police_pos = pd.read_pickle('./save/police_pos.pkl')
        police_norm = pd.read_pickle('./save/police_norm.pkl')
        temp = police_pos[self.arrest_columns] / police_pos[self.arrest_columns].max()
        police_pos['검거'] = np.sum(temp, axis=1)
        return tuple(zip(police_norm['구별'], police_norm['범죄']))
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