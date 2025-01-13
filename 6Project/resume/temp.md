# 임시

## `[임시 보관함]`

### EDA 시계열
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