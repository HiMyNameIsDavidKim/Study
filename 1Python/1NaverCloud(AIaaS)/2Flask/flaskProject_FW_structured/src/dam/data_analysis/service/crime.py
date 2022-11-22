from dataclasses import dataclass

import googlemaps
import numpy as np
import pandas as pd
from sklearn import preprocessing
import folium
CRIME_MENUS = ["Exit", #0
                "Show Spec",#1
                "Save Police Position",#2.
                "Save CCTV Population",#3
                "Save Police Normalization",#4
                "Save US Unemployment Map",#5
                "Save Seoul Crime Map",#6
                ]

crime_menu = {
    "1" : lambda t: t.show_spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.save_cctv_pop(),
    "4" : lambda t: t.save_police_norm(),
    "5" : lambda t: t.save_us_unemployment_map(),
    "6" : lambda t: t.save_seoul_crime_map(),
}
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''

@dataclass
class MyChoroplethVO:
    geo_data = "",
    data = object,
    name = "",
    columns = [],
    key_on = "",
    fill_color = "",
    fill_opacity = 0.0,
    line_opacity = 0.0,
    legend_name = "",
    bins = None,
    location = [],
    zoom_start = 0,
    save_path = ''

def MyChoroplethService(vo):
    map = folium.Map(location=vo.location, zoom_start=vo.zoom_start)
    folium.Choropleth(
        geo_data=vo.geo_data,
        data=vo.data,
        name=vo.name,
        columns=vo.columns,
        key_on=vo.key_on,
        fill_color=vo.fill_color,
        fill_opacity=vo.fill_opacity,
        line_opacity=vo.line_opacity,
        legend_name=vo.legend_name
    ).add_to(map)
    map.save(vo.save_path)

class Crime:

    def __init__(self):
        self.crime = pd.read_csv('../../ml/data/crime_in_seoul.csv')
        cols = ['절도 발생','절도 검거','폭력 발생', '폭력 검거']
        self.crime[cols] = self.crime[cols].replace(',', '', regex=True).astype(int)  # regex=True
        self.cctv = pd.read_csv('../../ml/data/cctv_in_seoul.csv')
        self.pop = pd.read_excel('./data/pop_in_seoul.xls',usecols=["자치구","합계","한국인","등록외국인","65세이상고령자"], skiprows=[0,2])
        self.ls = [self.crime, self.cctv, self.pop]
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']
        self.us_states = './data/us-states.json'
        self.us_unemployment = pd.read_csv('../../ml/data/us_unemployment.csv')
        self.kr_states = './data/kr-state.json'
        print(self.kr_states)
    '''
    1.스펙보기 
    id = SERIALNO  
    Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', '강간 검거', '절도 발생',
       '절도 검거', '폭력 발생', '폭력 검거'],
      dtype='object')
    Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object'
    '''

    def show_spec(self): # 1
        [(lambda x: print(f"--- 1.Shape ---\n{x.shape}\n"
                               f"--- 2.Features ---\n{x.columns}\n"
                               f"--- 3.Info ---\n{x.info}\n"
                               f"--- 4.Case Top1 ---\n{x.head(1)}\n"
                               f"--- 5.Case Bottom1 ---\n{x.tail(3)}\n"
                               f"--- 6.Describe ---\n{x.describe()}\n"
                               f"--- 7.Describe All ---\n{x.describe(include='all')}"))(i)
         for i in self.ls]

    def save_police_pos(self): # 2
        crime = self.crime
        station_names = []
        for name in crime['관서명']:
            print(f"지역이름: {name}")
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(f" 서울시내 경찰서는 총 {len(station_names)}개 이다")
        [print(f"{str(i)}") for i in station_names]

        gmaps = (lambda x: googlemaps.Client(key=x))("AIzaSyAaD1o_2faFQ_D8aOHBGBOhvFOuuH7iE88")
        print(gmaps.geocode("서울중부경찰서", language='ko'))
        print(" ### API에서 주소추출 시작 ### ")
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language='ko')
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        # 구와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        crime.to_pickle('./save/police_pos.pkl')
        print(pd.read_pickle('../../ml/save/police_pos.pkl'))

    def save_cctv_pop(self): # 3
        cctv = self.cctv
        pop = self.pop
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)
        pop.rename(columns={
            pop.columns[0]: '구별',
            pop.columns[1]: '인구수',
            pop.columns[2]: '한국인',
            pop.columns[3]: '외국인',
            pop.columns[4]: '고령자'
        }, inplace=True)
        pop.drop(index=26,inplace=True)
        pop['외국인비율'] = pop['외국인'].astype(int) / pop['인구수'].astype(int) * 100
        pop['고령자비율'] = pop['고령자'].astype(int) / pop['인구수'].astype(int) * 100
        cctv.drop(["2013년도 이전","2014년","2015년","2016년"], axis=1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on="구별")
        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])
        print(f'고령자비율과 CCTV의 상관계수 {str(cor1)} \n'
              f'외국인비율과 CCTV의 상관계수 {str(cor2)} ')
        """
         고령자비율과 CCTV 의 상관계수 [[ 1.         -0.28078554]
                                     [-0.28078554  1.        ]] 
         외국인비율과 CCTV 의 상관계수 [[ 1.         -0.13607433]
                                     [-0.13607433  1.        ]]
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        고령자비율 과 CCTV 상관계수 [[ 1.         -0.28078554] 약한 음적 선형관계
                                    [-0.28078554  1.        ]]
        외국인비율 과 CCTV 상관계수 [[ 1.         -0.13607433] 거의 무시될 수 있는
                                    [-0.13607433  1.        ]]                        
        """
        cctv_pop.to_pickle('./save/cctv_pop.pkl')
        print(pd.read_pickle('../../ml/save/cctv_pop.pkl'))

    def save_police_norm(self): # 4
        police_pos = pd.read_pickle('../../ml/save/police_pos.pkl')
        police = pd.pivot_table(police_pos,index="구별",aggfunc=np.sum)
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
        """
        스케일링은 선형변환을 적용하여
        전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        """
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        """
        정규화 normalization
        많은 양의 데이터를 처리함에 있어 데이터의 범위(도메인)를 일치시키거나
        분포(스케일)를 유사하게 만드는 작업
        """
        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns, index=police.index)
        police_norm[self.crime_rate_columns] = police[self.crime_rate_columns]
        police_norm['범죄'] = np.sum(police_norm[self.crime_rate_columns], axis=1)
        police_norm['검거'] = np.sum(police_norm[self.crime_columns], axis=1)
        # police_norm.reset_index(drop=False, inplace=True) # pickle 저장직전 인덱스 해제
        police_norm.to_pickle('./save/police_norm.pkl')
        print(pd.read_pickle('../../ml/save/police_norm.pkl'))

    def save_us_unemployment_map(self): # 5
        mc = MyChoroplethVO()
        mc.geo_data = self.us_states
        mc.data = self.us_unemployment
        mc.name = "choropleth"
        mc.columns = ["State","Unemployment"]
        mc.key_on = "feature.id"
        mc.fill_color = "YlGn"
        mc.fill_opacity = 0.7
        mc.line_opacity = 0.5
        mc.legend_name = "Unemployment Rate (%)"
        mc.bins = list(mc.data["Unemployment"].quantile([0, 0.25, 0.5, 0.75, 1]))
        mc.location = [48, -102]
        mc.zoom_start = 5
        mc.save_path = "../../ml/save/unemployment.html"
        MyChoroplethService(mc)

    def save_seoul_crime_map(self): # 6
        mc = MyChoroplethVO()
        mc.geo_data = self.kr_states
        mc.data = self.get_seoul_crime_data()
        mc.name = "choropleth"
        mc.columns = ["State", "Crime Rate"]
        mc.key_on = "feature.id"
        mc.fill_color = "PuRd"
        mc.fill_opacity = 0.7
        mc.line_opacity = 0.2
        mc.legend_name = "Crime Rate (%)"
        mc.location = [37.5502, 126.982]
        mc.zoom_start = 12
        mc.save_path = "../../ml/save/seoul_crime_rate.html"
        MyChoroplethService(mc)

    def get_seoul_crime_data(self):
        police_norm = pd.read_pickle('../../ml/save/police_norm.pkl')
        return tuple(zip(police_norm.index, police_norm['범죄']))
        # police_norm.index 는 '구별'
'''
미국 주가 콜롬비아, 푸에르토-리코(준주) 포함시
콜롬비아('id': '11'-> 인덱스 8),
푸에르토리코('id': '72' -> 인덱스 51)는 준주라서 제거해야함
'''
def set_json_from_df(fname):
    df = pd.read_json(fname)
    df.drop(df.index[[8,51]], inplace=True)
    df.to_json("./save/us-states.json", orient='index')

def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = Crime()
    while True:
        menu = my_menu(CRIME_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            crime_menu[menu](t)
            '''
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")
            '''


