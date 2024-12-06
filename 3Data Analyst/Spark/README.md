# Spark

## `[스파크 개요]`

### [APACHE Spark]
* 분산 클러스터링 컴퓨팅 오픈소스 프레임워크.
* 대규모 데이터 처리용으로 설계됐다.
* 계산 부하를 여러 노드에 분담 병렬 처리한다.
* 구조: cluster manager, driver process, executors
* cluster manager
    * 사용 가능한 자원 파악한다.
    * 데이터 처리 작업을 관리하고 조율한다.
    * 사용자가 스파크 어플리케이션을 제출하는 곳 이다.
* driver process
    * 클러스터 노드 중 하나 이다.
    * 드라이버 프로그램의 명령을 executor에 할당한다.
    * 할당을 위해 분석, 배포, 스케쥴링 진행한다.
    * spark session: 스파크 어플리케이션의 통합 진입점
* executors
    * 드라이버 프로세스가 할당한 작업을 수행한다.
    * 진행 상황을 다시 드라이버 노드에 보고한다.
<br><br>

### [스파크의 데이터 처리 방식]
* partition
    * executor가 병렬로 작업을 수행하도록 하는 단계이다.
    * 파티션이라는 청크 단위로 데이터를 분할한다.
    * 클러스터의 물리적 머신에 존재하는 행의 집합이다.
    * 하나의 전체 데이터 -> 파티션 나누기 -> 각각에 executor n개 할당
* transformation
    * 데이터 변경을 원할 때 변경 방법을 알려주는 단계이다.
    * 논리적 실행 계획 '만' 세운다.
    * 실제 연산은 나중에 액션 단계에서 한다.
* lazy evaluation
    * 연산 명령을 받았을 때 즉시 데이터를 수정하지 않는다.
    * 데이터에 적용할 트랜스포메이션 자체만 실행한다.
    * (데이터를 넣지 않고 함수만 미리 계산한다.)
    * 액션 전까지 전체 데이터 흐름을 최적화한다.
* action
    * 실제 연산을 수행하기 위한 사용자 명령이다.
    * 최종 결과를 계산하고 출력하도록 지시한다.
* catalyst
    * 트랜스포메이션을 적용할 때 논리 계획이 담긴 트리 그래프를 먼저 만든다.
    * 로지컬 옵티마이저에 의해서 최적의 논리를 만들고 데이터를 반환한다.
    * (어떤 순서로 계산해야하는지 촤적화한다.)
    * 따라서 더 빠른 계산을 할 수 있다.
    * (ex. 인메모리 연산보다 네트워크 연산이 느리므로 더 늦게 진행한다.)
<br><br>

### [Pyspark]
* 파이썬에서 스파크를 사용하게 해주는 api
* 기능
    * SparkSQL 쿼리 사용 가능
    * 데이터 프레임 2차원 구조 지원
    * 판다스와 같은 문법 사용
    * 정적 데이터와 같은 방식으로 계산을 표현
    * MLlib 모델링 가능
<br><br>

### [빅데이터 확장자]
* 빅데이터 전용 파일 확장자가 있다.
* (ex. Avro, Parquet, ORC)
* spark는 Parquet을 사용한다.
* 컬럼 기반으로 데이터를 저장하기 때문에 속도가 빠르다.
* 6기가 기준 read에 3분 걸리는 파일도 0.1초만에 가능하다. 
<br><br>



## `[스파크 기본]`

### [환경 설정]
* 설치
    * ```python
      !apt-get install openjdk-8-jdk-headless
      !wget -q https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz
      !tar -xf spark-3.0.0-bin-hadoop3.2.tgz
      !pip install findspark
      !pip install kaggle --upgrade

      import os
      import findspark


      os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
      os.environ["SPARK_HOME"] = "/content/spark-3.0.0-bin-hadoop3.2"
      findspark.init()
      ```
* pyspark 시작
    * ```python
      from pyspark.sql import SparkSession

      spark = (
        SparkSession
        .builder
        .appName("pyspark_test")
        .master("local[*]")
        .getOrCreate()
      )
      ```
* 캐글 api 연결
    * ```python
      from google.colab import files

      files.upload()
      ```
    * 토큰 json 파일 업로드
    * 캐글 데이터셋 -> 다운로드 옆 점3개 -> copy api link
    * ```python
      !mkdir -p ~/.kaggle/
      !cp kaggle.json ~/.kaggle/
      !chmod 600 ~/.kaggle/kaggle.json
      !kaggle datasets download -d wethanielaw/iowa-liquor-sales-20230401  # link here
      !unzip iowa-liquor-sales-20230401.zip
      ```
<br><br>

### [spark dataframe]
* 읽어오기
    * 너무 커서 판다스로 못읽는 경우도 pyspark로 가능하다.
    * ```python
      df = spark.read.csv(
        path="Iowa_Liquor_Sales.csv", header=True, inferSchema=True
      )
      ```
* 데이터 체크
    * ```python
      df.show(10)
      df.printSchema()
      ```
* 저장하기
    * ```python
      # parquet 파일의 컬럼 이름은 공백이랑 괄호 불가능, replace 필수.
      df.write.format("parquet").save(
        path = "data_parquet",
        header=True
      )
      ```
* parquet 파일 다운로드
    * ```python
      download_list = os.listdir("./data_parquet")
      for file_name in download_list:
          if file_name[-3:] != 'crc':
              files.download("./data_parquet/" + _)
      ```
* parquet 파일 읽어오기
    * ```python
      parquet_df = spark.read.parquet("data_parquet")
      ```
* 데이터 처리
    * ```python
      from pyspark.sql import functions as F

      parquet_df.filter(F.col("City")=="MAXWELL")
      ```
<br><br>

### [spark SQL]
* 일단 데이터프레임으로 불러오고난 뒤 뷰로 등록한다.
* SQL like 코딩을 할 수 있지만 선호하는 편은 아니다.
* 뷰 등록
    * ```python
      parquet_df.createOrReplaceTempView('parquet_sql')
      ```
* 쿼리 작성
    * ```python
      sqlWay = spark.sql('''
        select *
        from parquet_sql
        where City = 'MAXWELL'
        '''
      )
      ```
<br><br>

### [spark dataframe 함수]
* 데이터 보기
    * df.show(10)
    * df.select("col1", "col2").show()
* 행 카운트
    * df.count()
* 컬럼 정보 보기
    * df.printSchema()
* 함수 import
    * from pyspark.sql import functions as F
* 컨디션 걸기
    * df.filter(F.col("col1") == "value1").select("col1").show()
* 조건문 걸기
    * ```python
      df
      .select("col1",
          F.when(F.col("col1") > 12, "A"
          ).otherwise("B").alias("as_col")
      ).show()
      ```
* null
    * null 확인
        * df.select([F.count(F.when(F.isnull(c), c)).alias(c) for c in df.columns]).show()
    * null 데이터 세부내용 보기
        * df.filter(F.col("col1").isNull()).show()
    * null 데이터 드랍 (컬럼)
        * df = df.drop("col1")
    * 다른 값으로 채우기 (첫번째 값)
        * ```python
          df = (
          df
          .withColumn(
              "CategoryName",
              F.first(
                  F.col("CategoryName"), ignorenulls=True
              ).over(W.partitionBy(F.col("Category")).orderBy(F.col("Date").desc()))
              )
          )
          ```
    * null 데이터 제거 (행)
        * df = df.filter(F.col("col1").isNotNull())
* 전체 값 리스트로 출력
    * df.select(F.collect_list('col1')).show()
* 고유한 값만 출력
    * df.select(F.collect_set('col1')).show()
* 고유한 값의 갯수
    * df.select(F.size(F.collect_set('col1'))).show()
* 윈도우 정의하고 사용
    * over로 윈도우를 정의한다.
    * W가 윈도우로 서브쿼리 같은 것이다.
    * partitionBy는 group by와 유사하다.
    * ```python
      df.withColumn("col3",
                  F.collect_set("col2")
                  .over(W.partitionBy  ("col1"))
                  ).show()
      ```
* date 형태로 변환
    * df.printSchema() 으로 확인한다.
    * date 이름인데 string인 경우 변환이 필요하다.
    * 현재 포멧이 어떤식으로 써있는지 같이 입력한다.
    * df = df.withColumn("Date", F.to_date(F.col("Date"), 'MM/dd/yyyy'))
    * to_date 처럼 to_timestamp 도 있다.
* 판다스로 변환
    * spark는 분산처리만 특화되어 시각화에는 불리하다.
    * 보통 전체를 하면 터지므로 컬럼 한두개만 판다스로 변환하여 사용한다.
    * df = df.filter(F.col("col1")=="value1").toPandas()
<br><br>

### [UDF 사용]
* User Defined Functions
* def로 함수 선언하고 udf로 만들어준 뒤 사용한다.
* 실전
    * ```python
      from pyspark.sql.functions import udf
  
      def calculate_gross_profit(unit_sales, unit_cost, sales_amt):
          gross_profit = sales_amt * (unit_sales - unit_cost)
          return gross_profit

      calculate_gross_profit_udf = udf(
      calculate_gross_profit,  # udf
      T.DoubleType()  # return type
      )

      df.withColumn(
          "gross_profit",
          calculate_gross_profit_udf(
            df.['col1'],
            df.['col2'],
            df.['col3']
          )
      )
      .select("col1", "col2", "col3", "gross_profit")
      ).show()
      ```
<br><br>

### [Plotly 시각화]
* 대시보드처럼 인터랙티브한 시각화 기능
* 설치 및 임포트
    * !pip install plotly
* 판다스에 내장시키기
    * ```python
      pd.options.plotting.backend = "plotly"
      df["col1"].hist()
      ```
* 기본 그래프
    * ```python
      import plotly.graph_objects as go


      fig = go.Figure(
      data=[go.Line(x=df["col1"], y=df["col2"])],
      layout=go.Layout(title=go.layout.Title(text="Titles"))
      )
      fig.show()
      ```
* express 그래프
    * ```python
      import plotly.express as px


      fig = px.line(x=df["col1"], y=df["col2"], title="Titles")
      fig.show()
      ```
* 라벨 호버링 기능
    * ```python
      fig.update_layout(
          hoverlabel_bgcolor="white",
          hoverlabel_font_size=10,
          hoverlabel_font_color='black',
          hoverlabel_font_family="Rockwell"
      )
      ```
* 라벨 호버링 커스텀
    * ```python
      fig.update_traces(
          hovertemplate='총 매출: %{text}달러 <br>'+
          '날짜: %{x} <br>'+
          '판매량 : %{y}개')
      ```
* 범위 설정 슬라이더
    * ```python
      fig.update_layout(xaxis=dict(rangeslider_visible=True))
      ```
* 드롭 다운 버튼, 그래프 토글
    * ```python
      fig = go.Figure()

      fig.add_trace(go.Line(
          name="BottlesSold",
          x=WAUKEE_pd["Date"],
          y=WAUKEE_pd["BottlesSold"]
      ))

      fig.add_trace(go.Line(
          name="SaleDollars",
          x=WAUKEE_pd["Date"],
          y=WAUKEE_pd["SaleDollars"]
      ))

      fig.update_layout(
          updatemenus=[
              dict(
                  type="dropdown",
                  direction="down",
                  buttons=list([
                      dict(label="Both",
                          method="update",
                          args=[{"visible": [True, True]},
                              {"title": "BottlesSold & SaleDollars"}]),
                      dict(label="BottlesSold",
                          method="update",
                          args=[{"visible": [True, False]},
                              {"title": "BottlesSold",}]),
                      dict(label="SaleDollars",
                          method="update",
                          args=[{"visible": [False, True]},
                              {"title": "SaleDollars",}]),
                  ]),
              ),
          ]
      )
    fig.show()
      ```
<br><br>




