# Python (분석)

## `[판다스]`

### [기본 함수]
* 상위 5개 행 출력
    * df.head()
* 행과 열의 갯수 출력
    * df.shape
* 전체 컬럼명 출력
    * df.columns
* 데이터프레임의 인덱스 구성 확인
    * df.index
    * 0부터 시작해서 스텝 사이즈가 1이 디폴트
* null 갯수 확인
    * df.isnull().sum()
* 모든 null 채우기
    * df = df.fillna(method='ffill').fillna(method='bfill')
* 전체 컬럼 데이터 개수와 타입 체크
    * df.info()
* numerical 변수 통계값 확인
    * df.describe()
* 한글 포함된 csv 로드
    * df = pd.read_csv(path, encoding='euc-kr')
* 컬럼의 고유값 확인
    * 개수 출력
        * df['col'].nunique()
    * 이름 출력
        * df['col'].unique()
* inf 데이터 처리
    * df['col'].replace([np.inf, -np.inf], np.nan)
<br><br>

### [특정 행과 열의 값]
* r(행), c(열)에 대한 값을 리턴
    * df.iloc[r,c]
    * 6번째 컬럼의 모든 행을 가져와서 데이터 타입 확인
        * df.iloc[:,5].dtype
    * 6번째 컬럼의 3번째 값
        * df.iloc[2,5]
* 실제로는 df['col'] 형태를 더 많이 사용
<br><br>

### [iloc와 loc]
* 인덱스의 순서로 불러올 때는 iloc
* 값으로 불러올 때는 loc
<br><br>

### [데이터 유형별 출력]
* 리스트로 나누기
    * categorical_list = [i for i in df.columns if df[i].dtypes == 'O']
    * numeric_list = [i for i in df.columns if df[i].dtypes != 'O']
* numerical 변수
    * df.select_dtypes(exclude=object).columns
* categorical 변수
    * df.select_dtypes(include=object).columns
<br><br>

### [filtering & sorting]
* 값을 기준으로 필터링
    * col 컬럼의 값이 3인 데이터 추출 후 head 출력
        * df[df['col']==3].head()
    * 정렬까지 하고 출력
        * reset_index 함수 사용
        * df.loc[df['col']==3].head().reset_index(drop=True)
* df에서 바로 타입 변환
    * 스트링 변환 후 실수 변환까지 하기
        * str 함수로 바로 변환 가능
        * astype로 타입 변환 가능
        * df['new_price'] = df['item_price'].str[1:].astype('float')
* and or 사용
    * loc 안에 넣고 & | 사용
    * df_ans = df.loc[(df.item_name =='Chicken Salad Bowl') & (df.new_price <= 9)]
    * df_ans = df.loc[(df.item_name =='Steak Salad') | (df.item_name =='Bowl')]
* 정렬
    * sort_values 함수 사용
    * df_ans = df.sort_values('new_price').reset_index(drop=True)
    * df_ans = df.sort_values('new_price',ascending=False).reset_index(drop=True)
* 내용 포함하는 데이터 소팅
    * contains 함수 사용
    * df_ans = df.loc[df.item_name.str.contains('Chips')]
    * not 사용 가능 (앞에 ~ 표시)
    * df_ans = df.loc[~df.choice_description.str.contains('Vegetables')]
    * 첫글자로 찾기
    * df_ans = df[df.item_name.str.startswith('N')]
    * 리스트 주고 찾기
    * df_ans = df.loc[df.new_price.isin(ls)]
* 짝수 홀수 번째 컬럼
    * 짝수, df_ans = df.iloc[:,::2]
    * 홀수, df_ans = df.iloc[:,1::2]
* 중복 제거
    * drop_duplicates 함수 사용
    * 기준 컬럼 제시
    * 첫번째 행만 사는 것이 디폴트
    * df = df.drop_duplicates('item_name')
    * 마지막 행만 살리기
    * df = df.drop_duplicates('item_name',keep='last')
* 평균 이상 필터링
    * df_ans = df.loc[df.new_price >= df.new_price.mean()]
* 데이터값 수정
    * loc 사용
    * [조건, 입력할 컬럼] = 입력할 값
    * df.loc[df.item_name =='Izze','item_name'] = 'Fizzy Lizzy'
    * df.loc[df.choice_description.isnull(),'choice_description'] ='NoData'
<br><br>

### [grouping]
* 빈도수 출력
    * value_counts 함수 사용
    * size 함수도 동일 기능
    * df_ans = df.host_name.value_counts().sort_index()
    * null을 세지 않으니 주의
    * null도 세고 싶을 경우 dropna=True
* 컬럼 2개를 기준으로 빈도수 출력
    * groupby 사용
    * df_ans = df.groupby([col1, col2]).size().unstack(fill_value=0)
* 그룹별 특정 값의 기초통계 값
    * agg 함수 사용
    * df_ans = df.groupby('col1')['col2'].agg(['mean','var','max','min'])
* 피벗 테이블
    * unstack 함수 사용
    * 그룹한 컬럼 중에 마지막 컬럼을 좌측에서 상단으로 이동
    * df_ans = df.groupby(['col1', 'col2']).price.mean().unstack()
    * df_ans = df.groupby(['col1', 'col2, 'col3']).price.mean().unstack()
    * 마지막 컬럼 말고 다른 컬럼도 이동 가능
    * df_ans = df.groupby(['col1', 'col2', 'col3]).price.mean().unstack(1)
<br><br>

### [Apply와 Map]
* 매핑이 간단하면 map-람다 사용
* 조건이 복잡해지면 함수 선언하고 apply 사용
* 커스텀 함수 사용해서 변환
    * 커스텀 함수 선언 후 사용
    * df['Date'].apply(remove_p)
    * 짧은 경우 람다 사용
    * df['Date'].apply(lambda x: x.replace(' p)', '')
* 딕셔너리로 매핑
    * map 함수 사용
    * 람다함수 사용
    * df['mapped_col'] = df.col1.map(lambda x: dic[x])
    * apply 함수 사용
    * 함수 하나 선언해서 사용하는 것
    * df['mapped_col']  =df.col1.apply(changeCategory)
* 구간 컬럼 정의 후 카운트
    * 매핑 후 카운트
    * df['ages']  = df.col1.map(lambda x: x//10 *10)
    * df_ans = df['ages'].value_counts().sort_index()
<br><br>

### [Time series]
* 시계열 데이터 다루기
* 타입 조회 시 datetime64로 표시
* 스트링에서 datetime 타입으로 변경
    * to_datetime 함수 사용
    * df.col1 = pd.to_datetime(df.col1)
* 년도의 유니크값 모두 출력
    * dt.year 함수 사용
    * unique 함수도 사용
    * df_ans = df.col1.dt.year.unique()
* 요일별로 매핑
    * 월요일:0 ~ 일요일:6
    * dt.weekday 함수 사용
    * df['weekday'] = df.col1.dt.weekday
* 년도-월 기준으로 평균값
    * 1995-11 처럼 형태 변경
    * dt.to_period('M') 함수 사용
    * df_ans = df.groupby(df.col1.dt.to_period('M')).mean(numeric_only=True)
* 일주일 간격 이동평균
    * rolling 함수 사용
    * 데이터 개수 적어서 간격 설정 가능
    * df_ans= df[['RPT','VAL']].rolling(7).mean()
* 영어 요일 나타내기
    * dt.day_name 함수 사용
    * df['weekday'] = df.col1.dt.day_name()
<br><br>

### [Pivot]
* pivot
    * pivot 함수 사용
    * index, columns, values 3가지 파라미터
    * 인덱스가 세로축, 컬럼이 가로축, values가 값
    * col1에 따른 col2별 col3의 값을 구하라.
    * df_ans = target.pivot(index='col1',columns='col2',values='col3')
    * col3의 평균
    * df_ans = target.pivot(index='col1',columns='col2',values='col3',aggfunc='mean')
* values가 없을 때 pivot
    * pivot_table 함수 사용
    * col2의 갯수
    * df_ans = target.pivot_table(index='col1',columns='col2',aggfunc='size').fillna(0)
<br><br>

### [Concat, Merge]
* 위아래 좌우로 합칠 때는 concat
* join의 개념을 사용할 때는 merge
* concat
    * concat 함수 사용
    * axis, 0은 행 기준인 위아래, 1은 열 기준인 좌우
    * axis 기본값은 0
    * df_ans = pd.concat([df1,df2], axis=0)
* 둘 다 있는 컬럼만 concat
    * join='inner' 사용
    * df_ans = pd.concat([df3,df4], join='inner')
* 모든 컬럼 concat
    * join='outer' 사용
    * 없는 값은 null로 채워짐
    * df_ans = pd.concat([df3,df4], join='outer').fillna(0)
* 한 컬럼을 키로 사용해 merge
    * merge 함수 사용
    * on 파라미터로 키 설정
    * df_ans = pd.merge(df5,df6,on='col1',how='inner')
    * df_ans = pd.merge(df5,df6,on='col1',how='outer').fillna(0)
<br><br>

### [Statistics 기초 통계값]
* 컬럼의 갯수 세기
    * value_counts 함수 사용
    * df['names'].value_counts()
* 유니크값 갯수 세기
    * df['names'].nunique()
* 가장 많이 등장하는 값
    * names[names.Count == names.Count.max()]
* 중앙값
    * names[names.Count == names.Count.median()]
* 표준편차
    * names.Count.std()
* 기초 통계값
    * names.describe()
<br><br>

### [Series and DataFrame]
* 데이터 프레임 만들기
    * pd.DataFrame({
        'col1', [1, 2, 3, 4, 5],
        'col2', [1, 2, 3, 4, 5],
        'col3', [1, 2, 3, 4, 5],
    })
* 컬럼 순서 변경
    * 순서 바꿔서 컬럼 넣고 다시 선언
    * df = df[['name', 'type', 'hp', 'evolution','pokedex']]
* 새 컬럼 생성
    * df['col4'] = [1, 2, 3, 4, 5]
* hp가 40 이상인 데이터
    * df[df['hp'] >= 40]
* 원하는 컬럼만 출력
    * df[['name', 'type']]
* df 복제
    * df.copy() 사용
    * 같다고 선언하면 연결되서 에러 날 수 있음
* 값 수정
    * loc 함수 사용
    * df.loc[[0],'col1'] = np.nan
<br><br>

### [Deleting]
* 컬럼명 할당
    * df.columns 사용
    * df.columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class']
* 컬럼 하나 지우기
    * 원본은 보존해야 하므로 새로 선언
    * df_ans = df[['sepal_length',	'sepal_width',	'petal_length',	'petal_width']]
* null 있는 행, 열 삭제
    * df_ans = df.dropna(how='any')
<br><br>

### [데이터 변환]
* 화씨 섭씨 변환
    * df['Temp']= (df['Temp']-32) / 1.8
* 날짜 변환
    * 스트링에서 데이트 타입으로 변환
        * df['Date'] = pd.to_datetime(df['Date'])
    * 날짜 + 시간 합쳐서 데이트 타입으로 변환
        * df_core_store['Date_merge'] = df['date'].astype(str) + ' ' + df['time'].astype(str)
        * df_core_store['Date_merge'] = pd.to_datetime(df_core_store['Date_merge'])
    * 년 월 분할
        * df_core_store['year'] = df_core_store['Date_merge'].dt.year
        * df_core_store['month'] = df_core_store['Date_merge'].dt.month
    * 월데이터 보기 힘들때 변환
        * df = df.replace({'January' : '01.January',
            'February' : '02.February',
            'March' : '03.March',
            'April' : '04.April',
            'May' : '05.May',
            'June' : '06.June',
            'July' : '07.July',
            'August' : '08.August',
            'September' : '09.September',
            'October' : '10.October',
            'November' : '11.November',
            'December' : '12.December'})
<br><br>



## `[시각화]`

### [seaborn]
* 히스토그램
    * ttbill = sns.histplot(df.total_bill)
    * ttbill.set(xlabel = 'Value', ylabel = 'Frequency', title = "Total Bill")
* 조인트 플랏
    * (히스토그램 + 스캐터 플랏) 한번에 표시
    * sns.jointplot(x ="total_bill", y ="tip", data = df)
* 디스트리뷰션 플랏
    * (히스토그램 + KDE 플랏) 한번에 표시
    * KDE는 밀도 추정치를 시각화
    * 연속형 데이터 맨 처음 볼 때 자주 사용
    * 기초 통계량 같이 보도록 describe와 함께 사용
    * sns.displot(df['col'])
* 페어 플랏
    * 스캐터 플랏 한번에 모두 표시
    * 연속형 변수만 가능
    * sns.pairplot(df)
* 히트맵
    * 히트맵 표시
    * sns.heatmap(df_yield[numeric_columns].corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
* 스트립 플랏
    * 이산형 변수를 x축에 두고 y축에 연속형 변수에 뿌려보는 그래프
    * 여러 집단의 연속형 변수 비교
    * sns.stripplot(x = "day", y = "total_bill", data = df)
    * 카테고리 2개 활용 가능
    * 색을 다르게 표시
    * sns.stripplot(x = "tip", y = "day", hue = "sex", data = df)
* 박스 플랏
    * 스트립 플랏이랑 동일한 역할 그래프
    * 중앙값, IQR 같은 기술통계량 박스로 표시
    * 박스 밖에 찍힌 것들은 outlier
    * sns.boxplot(x = "day", y = "total_bill", hue = "time", data = df);
* 스캐터 플랏
    * 산점도 분포 확인
    * sns.scatterplot(x='Temp', y='Sales', data=df)
    * plt.gcf().set_size_inches(7, 7)
* 피벗 플랏
    * 년도별 카테고리별 점유율 변화에 유용
    * ax = df.plot(kind='barh', stacked=True, title="years amt", rot=0)
    * for p in ax.patches:
    *   left, bottom, width, height = p.get_bbox().bounds
    *   ax.annotate("%.1f"%(width*100), xy=(left+width/2, bottom+height/2), ha='center', va='center', color='black')
* 테이블 그라데이션 표시
    * 플랏 말고 테이블 상태에서 overview 가능
    * df.style.background_gradient(cmap='Blues', subset=['col1'])
* GPS 데이터 시각화
    * 스캐터 플랏 사용하기
    * plt.scatter(df['Lon'], df['Lat'], s=1, alpha=0.5)
* 두개 그래프 나란히 표시
    * FacetGrid 클래스 사용
    * 두개 집단 연속형 변수 비교
    * col에 기준 컬럼 넣기
    * 히스토그램
        * g = sns.FacetGrid(df, col = "time")
        * g.map(plt.hist, "tip")
    * 스캐터 플랏
        * g = sns.FacetGrid(df, col = "sex", hue = "smoker")
        * g.map(plt.scatter, "total_bill", "tip", alpha =.7)
* 두개 그래프 한 평면에 표시
    * lmplot 함수 사용
    * 스캐터 플랏
        * 회귀선 끄려면 fit_reg=False
        * lm = sns.lmplot(x = 'Age', y = 'Fare', data = df, hue = 'Sex', fit_reg=False)
<br><br>

### [plt]
* 파이 차트
    * males = (df['Sex'] == 'male').sum()
    * females = (df['Sex'] == 'female').sum()
    * proportions = [males, females]
    * plt.pie(
    * proportions,
    * labels = ['Males', 'Females'],
    * shadow = False,
    * colors = ['blue','red'],
    * explode = (0.15 , 0),
    * startangle = 90,
    * autopct = '%1.1f%%'
    * )
    * plt.show()
<br><br>



## `[모델링]`

### [sklearn]
* 사이킷런
* X, Y 분할
    * X=df_merge.drop(['y'], axis=1)
    * Y=df_merge['y']
* 데이터셋 분할
    * x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y)
* 모델 난수 고정
    * rfc = RandomForestClassifier(random_state=42)
* 학습
    * rfc.fit(x_train, y_train)
* 예측
    * y_pred_train = rfc.predict(x_train)
    * y_pred_test = rfc.predict(x_test)
* 성능 확인
    * 이진분류 모델, light gbm 모델
        * print(classification_report(y_train, y_pred_train))
        * print(classification_report(y_test, y_pred_test))
        * AUROC score 평가
        * ROC 커브 분석
    * 회귀 모델, 선형회귀 모델
        * mse_train = mean_absolute_error(y_train, y_pred_train)
        * print('mse_train(mse): ', mse_train)
        * rmse_train = (np.sqrt(mse_train))
        * print('rmse_train(rmse): ', rmse_train)
        * r2_train = r2_score(y_train, y_pred_train)
        * print('rmse_train(r2): ', r2_train)
        * print('')
        * mse_test = mean_absolute_error(y_test, y_pred_test)
        * print('mse_test(mse): ', mse_test)
        * rmse_test = (np.sqrt(mse_test))
        * print('rmse_test(rmse): ', rmse_test)
        * r2_test = r2_score(y_test, y_pred_test)
        * print('rmse_test(r2): ', r2_test)
* 하이퍼 파라미터 자동 튜닝
    * grid_cv = GridSearchCV(rf_clf, param_grid = params, cv = 3, n_jobs = -1, scoring='recall')
    * grid_cv.fit(x_train, y_train)
    * print(f'The best params: {grid_cv.best_params_}')
    * print(f'The best score: {grid_cv.best_score_:.4f}')
* 중요 변수 파악
    * ftr_importances_values = rfc.feature_importances_
    * ftr_importances = pd.Series(ftr_importances_values, index = x_train.columns)
    * ftr_top20 = ftr_importances.sort_values(ascending=False)[:20]
    * sns.barplot(x=ftr_top20, y=ftr_top20.index)
    * plt.show()
* 피클 모델 save read
    * saved_model = pickle.dumps(model)
    * model_from_pickle = pickle.loads(saved_model)
* PCA 차원축소
    * pca = PCA(n_components = 2)
    * principalComponents = pca.fit_transform(x)
    * principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
* AUROC score 출력
    * y_pred_train_proba = rfc.predict_proba(x_train)[:, 1]
    * y_pred_test_proba = rfc.predict_proba(x_test)[:, 1]
    * roc_score_train = roc_auc_score(y_train, y_pred_train_proba)
    * roc_score_test = roc_auc_score(y_test, y_pred_test_proba)
    * print("roc_score_train :", roc_score_train)
    * print("roc_score_test :", roc_score_test)
* ROC 커브 그리기
    * roc_curve_plot(y_test, y_pred_test_proba)
* 표준화 
    * x = StandardScaler().fit_transform(x)
* 정규화
    * rfm['Recency'] = minmax_scale(rfm['Recency'], axis=0, copy=True)
* 레이블 인코더 사용
    * 카테고리컬 데이터에 주로 사용
    * LabelEncoder 클래스 사용
<br><br>



