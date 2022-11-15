import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
OKLAHOMA_MENUS = ["Exmit", #0
                "Spec",#1
                "Rename",#2
                "Interval",#3
                "Norminal",#4
                "Target",#5
                "partition",#6
                "Fit",#7
                "Predicate"]#8
oklahoma_meta = {
    'ACCESS', 'ACR', 'AGEP', 'BATH', 'BDSP', 'BLD', 'CONP', 'COW', 'ELEP',
       'FESRP', 'FKITP', 'FPARC', 'FSCHP', 'FTAXP', 'GASP', 'HHL', 'HHT',
       'HINCP', 'LANX', 'MAR', 'MV', 'NRC', 'R18', 'R65', 'RAC1P', 'RMSP',
       'RWAT', 'SCH', 'SCHL', 'SEX', 'VALP', 'VALP_B1'
}
oklahoma_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: print(" ** No Function ** "),
    "3" : lambda t: t.interval_variables(),
    "4" : lambda t: t.norminal_variables(),
    "5" : lambda t: t.target(),
    "6" : lambda t: t.partition(),
    "7" : lambda t: t.fit(),
    "8" : lambda t: print(" ** No Function ** "),
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

class OklahomaService:
    def __init__(self):
        self.oklahoma = pd.read_csv('./data/comb32.csv')
        self.oklahoma_DC1 = pd.read_csv('./data/2017DC1.csv')
        self.my_oklahoma = None
        self.target = None
        self.data = None
    '''
    1.스펙보기
    '''
    def spec(self):
        # pd.set_option('display.max_columns', None)
        # pd.set_option('display.max_rows', None)
        print(" --- 1.Shape ---")
        print(self.oklahoma.shape)
        print(" --- 2.Features ---")
        print(self.oklahoma.columns)
        print(" --- 3.Info ---")
        print(self.oklahoma.info())
        print(" --- 4.Case Top1 ---")
        print(self.oklahoma.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.oklahoma.tail(3))
        print(" --- 6.Describe ---")
        print(self.oklahoma.describe())
        print(" --- 7.Describe All ---")
        print(self.oklahoma.describe(include='all'))
    '''
    2.한글 메타데이터
    '''
    def rename_meta(self):
        self.my_oklahoma = self.oklahoma.rename(columns=oklahoma_meta)
        print(" --- 2.Features ---")
        print(self.my_oklahoma.columns)
    '''
    3~4.interval, ratio, norminal, ordinal
    '''
    def interval_variables(self):
        t = self.oklahoma
        interval = ['AGEP', 'BDSP', 'CONP', 'ELEP', 'GASP', 'HINCP', 'NRC', 'RMSP', 'VALP']
        print(f'범주형변수 데이터타입\n {t[interval].dtypes}')
        print(f'범주형변수 결측값\n {t[interval].isnull().sum()}')
        print(f'결측값 있는 변수\n {t[interval].isna().any()[lambda x: x]}')

        self.oklahoma = t
        self.spec()
        print(" ### 프리프로세스 종료 ### ")
        self.oklahoma.to_csv("./save/okla_pre.csv")

    def ratio_variables(self): # 해당 컬럼이 없음
        pass

    def norminal_variables(self):
        pass

    def ordinal_variables(self): # 해당 컬럼이 없음
        pass
    '''
    5.타깃
    '''
    def partition(self):
        self.my_oklahoma = self.oklahoma_DC1
        df = self.my_oklahoma
        self.data = df.drop(['VALP_B1'], axis=1)
        self.target = df['VALP_B1']
    '''
    6.파티션
    '''
    def partition(self):
        data = self.data
        target = self.target
        undersample = RandomUnderSampler(sampling_strategy=0.333, random_state=2)
        data_under, target_under = undersample.fit_resample(data, target)
        print(target_under.value_counts(dropna=True))
        X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.5, random_state=42)
        print(" --- Partition is completed ---")
        print(X_train.shape)
        print(y_train.shape)
        return X_train, X_test, y_train, y_test
    '''
    7.핏
    '''
    def fit(self):
        rf = RandomForestClassifier(n_estimators=100, random_state=0)
        X_train, X_test, y_train, y_test = self.partition()
        self.model = rf.fit(X_train, y_train)
    '''
    8.예측
    '''
    def predicate(self):
        model = self.model
        X_train, X_test, y_train, y_test = self.partition()
        self.pred = model.predict(X_test)
        print(f'Accuracy on training set: {model.score(X_train,y_train):.5f}')
        print(f'Accuracy on training set: {model.score(y_test,self.pred):.5f}')