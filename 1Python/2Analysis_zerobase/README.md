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

### [필터링 & 소팅]
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



