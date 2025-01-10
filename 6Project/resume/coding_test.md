# 코딩 테스트

## 📋 Contents
### 🎯 ML baseline
### 🐍 Python algorithm
### 📊 SQL query
<br><br>

## `[🎯 ML baseline]`

### [불러오기]
* import pandas as pd
* import numpy as np
* import matplotlib.pyplot as plt
* import seaborn as sns
* plt.style.use(['seaborn-v0_8'])
* df = pd.read_csv('train.csv')
* df.head(10)
<br><br>

### [데이터 전처리]
* df.shape
* df.info()
    * 시계열 변경: df['date'] = pd.to_datetime(df['date'])
* df.isnull().sum()
    * 채우기: df = df.fillna('Null')
    * 행기준 제거: df = df.dropna()
    * 열기준 제거: df = df.dropna(axis=1)
* df.describe()
<br><br>

### [EDA]
* 데이터 유형 분리
    * ```python
      cols_categorical = df.select_dtypes(include=object).columns
      cols_numerical = df.select_dtypes(exclude=object).columns
      print(f'##### categorical #####')
      [print(f'{col}: {df[col].nunique()}') for col in cols_categorical]
      print(f'##### numerical #####')
      [print(f'{col}: {df[col].nunique()}') for col in cols_numerical]
      ```
* 유형 수정
    * ```python
      cols = ['col1', 'col2']
      for col in cols:
          cols_numerical = cols_numerical.drop(col)
          cols_categorical = cols_categorical.append(pd.Index([col]))
      ```
* categorical
    * y가 이산형
        * ```python
          for i, col in enumerate(cols_categorical):
              plt.subplot(len(cols_categorical)//3, 3, i+1)
              sns.countplot(data=df, x=col, hue='y')
              plt.title(f'{col} Count Plot')
          plt.tight_layout()
          plt.show()
          ```
    * y가 연속형
        * ```python
          for i, col in enumerate(cols_categorical):
              plt.subplot(len(cols_categorical)//3, 3, i+1)
              sns.violinplot(data=df, x=col, hue=col, y='y', inner='quartile', legend=False)
              plt.title(f'{col} Violin Plot')
          plt.tight_layout()
          plt.show()
          ```
* numerical
    * 상관계수 히트맵
        * ```python
          sns.heatmap(df[cols_numerical].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths='0.5')
          plt.title(f'Corr Heatmap')
          plt.tight_layout()
          plt.show()
          ```
    * y가 이산형
        * ```python
          for i, col in enumerate(cols_numerical):
              plt.subplot(len(cols_numerical)//3, 3, i+1)
              sns.violinplot(data=df, x='y', hue='y', y=col, inner='quartile', legend=False)
              plt.title(f'{col} Violin Plot')
          plt.tight_layout()
          plt.show()
          ```
    * y가 연속형
        * ```python
          df_temp = df.copy()
          df_temp = df_temp[cols_numerical]
          # df_temp = df_temp.sample(n=len(df_temp)//100, random_state=42)
          sns.pairplot(df_temp, kind="scatter", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
          plt.title(f'Scatter Plot')
          plt.tight_layout()
          plt.show()
          ```
* 시계열
    * categorical
        * ```python
          df_temp = df.copy()
          df_temp['Date_1'] = df_temp["date"].dt.strftime("%Y-%m")

          for i, col in enumerate(cols_categorical):
              monthly_cat = df_temp.groupby(['Date_1', col]).size().unstack()
              monthly_cat.plot(kind='bar', stacked=True)
              plt.title(f'{col} Bar Plot')
              plt.tight_layout()
              plt.show()
          ```
    * numerical
        * ```python
          df_temp = df.copy()
          df_temp['Date_1'] = df_temp["date"].dt.strftime("%Y-%m")

          for i, col in enumerate(cols_numerical):
              if col = 'y':
                  continue
              df_y = df_temp.groupby('Date_1')['y'].sum().reset_index()
              df_col = df_temp.groupby('Date_1')[col].mean().reset_index()
              df_merge = pd.merge(df_y, df_col, on='Date_1')
              fig, ax1 = plt.subplots(figsize=(12, 8), dpi=80)
              ax1.bar(x=df_merge['Date_1'], height=df_merge['y'], color='gray', alpha=0.2)
              ax2 = ax1.twinx()
              ax2.plot(df_merge['Date_1'], df_merge[col], color='red', label=col)
              plt.title(f'Y Bar and {col} Line Plot')
              ax1.grid(False)
              ax2.grid(False)
              ax1.set_facecolor('white')
              ax2.set_facecolor('white')
              plt.tight_layout()
              plt.show()
          ```
<br><br>



### [모델링]
* 이진분류
* 분류
* 회귀
<br><br>



