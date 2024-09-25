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
    * df_ans = df.groupby(['col1','col2'], as_index=False).size()
* 그룹별 특정 값의 기초통계 값
    * agg 함수 사용
    * df_ans = df.groupby('col1')['col2'].agg(['mean','var','max','min'])
* 피벗 테이블
    * unstack 함수 사용
    * df_ans = df.groupby(['col1', 'col2']).price.mean().unstack()
<br><br>

### [Apply와 Map]
* 매핑이 간단하면 map-람다 사용
* 조건이 복잡해지면 함수 선언하고 apply 사용
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







