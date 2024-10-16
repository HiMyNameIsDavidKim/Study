# Big Query

## `[구글 빅쿼리 개요]`

### [데이터 웨어하우스]
* 빅쿼리는 GCP의 클라우드 기반 데이터 웨어하우스
* 서비스에 연결된 데이터 베이스에 쿼리를 날리면 문제가 발생할 수 있다.
* 데이터 베이스를 데이터 웨어하우스에 모아서 문제를 방지한다.
* 서비스에 직접적으로 연결되지 않도록 방지한다.
* SQL 문법을 기반으로 데이터 웨어하우스 조작이 가능하다.
<br><br>

### [환경 설정]
* GCP 콘솔 접속
* 왼쪽 위 선 3개 클릭 -> 빅쿼리 클릭
* 크기 순서: 프로젝트 - 데이터셋 - 테이블
* 프로젝트 만들기
* SQL 쿼리 클릭
* select 'Hello BigQuery!';
* 쿼리 저장(기존) 클릭 -> 이름 변경 -> 저장
    * 탐색기 패널에 저장된 쿼리에서 확인 가능
<br><br>

### [빅쿼리 인터페이스]
* 쿼리 여러개 실행하면 각각 따로 보기 가능
* 마우스로 드래그해서 블록 지정한 쿼리만 실행 가능
* 탭을 추가하며 쿼리 작성 가능하며 화면분할 사용 가능
* 왼쪽에 탐색기 패널 -> 프로젝트 ID 왼쪽 삼각형 클릭 -> 쿼리와 테이블 관리
<br><br>

### [데이터셋과 테이블 만들기]
* 왼쪽에 탐색기 패널 -> 프로젝트 ID 오른쪽 점 3개 -> 데이터셋 만들기 클릭
* 데이터셋 ID 입력, 위치유형 리전, 서울 리전
* 만들기 클릭
* 탐색기 패널 -> 만든 데이터셋 클릭
* 테이블 만들기 클릭 -> 테이블로 만들 소스 업로드 -> 파일 선택 -> 찾아보기
* 테이블 이름 설정, 스키마 자동감지 체크, 테이블 만들기 클릭
* 탐색기 패널 -> 만든 테이블 클릭 -> 미리보기 -> 데이터 확인하기
<br><br>

### [빅쿼리 날짜 다루기]
* DATE
    * 2024-01-01
    * 연월일 표시
* DATETIME
    * 2024-01-01T01:01:01
    * 시간까지 표시
* TIMESTAMP
    * 2024-01-01 01:01:01 UTC
    * 타임존까지 표시
* TIME
    * 01:01:01
    * 시간만 표시
* 4개 모두 서로 다른 날짜 타입이다.
* 각 날짜 타입을 함수로 바로 변환이 가능하다.
* 날짜에서 일부 추출하기
    * 형태를 바꾸고 싶을 때 사용
    * EXTRACT('추출할 부분' FROM '날짜 컬럼')
    * 연월일, 요일, 주, 분기, 시간 등 모두 추출 가능
* 날짜에서 일부만 남기기
    * 형태는 유지하면서 값을 통일하고 싶을 때 사용
    * DATE_TRUNC('날짜', '남기는 부분')
    * DATETIME_TRUNC('날짜', '남기는 부분')
    * TIMESTAMP_TRUNC('날짜', '남기는 부분')
<br><br>

### [유용한 함수 정리]
* 빅쿼리는 행기반이 아니라 열기반으로 저장한다.
* 따라서 빅쿼리에서는 컬럼이 중요하다.
* 필요없는 컬럼 빼고 다 불러오기
    * select * except('제외할 컬럼')
* 몇개 컬럼은 연산하거나 이름 바꾸고 불러오기
    * select * replace('대체할 컬럼' as '새 컬럼명')
* 데이터 타입 변경
    * cast('컬럼명' as '데이터 타입')
    * cast는 에러나면 멈춘다.
    * 에러날 때 null로 채우려면 safe_cast
    * safe_cast('컬럼명' as '데이터 타입')
    * 이외에도 safe 붙은 함수들은 에러 시 null 채운다.
    * 특히 safe_divide()가 유용하다.
<br><br>



## `[실습: 지표 개발, 지표 분석, 지표 관리]`

### [이커머스 데이터셋]
* 캐글 출처 브라질 이커머스 기업 Olist 데이터셋
* 데이터셋이 8개로 쪼개져 있어서 조인이 필요하다.
* 8개 중에 4개 주로 사용 (주문, 주문상품, 제품, 고객)
<br><br>

### [이커머스 비즈니스 지표]
* 큰 지표에서 작은 지표로 쪼개어 확인한다.
    * ex. 매출이 떨어진다 -> 매출 중에 x1 문제 -> x1을 구성하는 x2 문제
* 이커머스 지표
    * 이커머스 플랫폼의 매출은 총 거래액이 아니라 수수료만 이다.
    * 총 거래액 (=소비자가 결제한 전체 금액)
    * 플랫폼은 판매자에게 판매대금을 주고 수수료를 받는다.
    * 이 수수료만 이커머스 플랫폼의 매출이다.
    * 이번에 다룰 지표: 매출, 주문건수, 건당금액
* 매출 지표 분석
    * 매출 = 주문 건수 * 건당 주문 금액
    * 매출의 증가가 둘 중에 뭐 때문인지 확인해야 한다.
    * 특정 월 매출 급증 -> (주문건수 or 건당금액) 중 이유를 찾아야 한다.
* 주문건수 지표 분석
    * 주문건수 = 고객 수 * 주문 빈도
    * 주문건수의 증가가 둘 중에 뭐 때문인지 확인해야 한다.
* 건당금액 지표 분석
    * 건당금액 = 제품 수 * 제품 평균 가격
    * 건당금액의 증가가 둘 중에 뭐 때문인지 확인해야 한다.
* 정리
    * 매출 = (고객수 * 주문빈도) * (제품수 * 평균가격)
    * 매출을 올리려면 4개 중에 어떤 것을 올릴지 생각해야 한다.
<br><br>

### [실전 쿼리]
* 매출 가져오기
    * 매출, 주문건수, 건당금액 가져오기
    * select sum(price) as order_amt, count(distinct order_id) as order_cnt, sum(price)/count(distinct order_id) as amount_per_order from `olist.olist_order_items`;
* 주문건수 가져오기
    * 테이블 조인하기
    * select ord.order_id, ord.customer_id, cust.customer_unique_id from `olist.olist_orders` as ord left join `olist.olist_customers` as cust on ord.customer_id = cust.customer_id;
    * 주문건수, 고객수, 주문빈도 가져오기
    * select count(distinct ord.order_id) as `주문건수`, count(distinct cust.customer_unique_id) as `주문고객수`, count(distinct ord.order_id)/count(distinct cust.customer_unique_id) as `주문빈도` from `olist.olist_orders` as ord left join `olist.olist_customers` as cust on ord.customer_id = cust.customer_id;
* 건당금액 가져오기
    * 건당금액, 제품수, 평균가격 가져오기
    * select sum(price) as `총 매출`, count(distinct order_id) as `총 주문수`, count(order_item_id) as `총 판매상품수`, sum(price) / count(distinct order_id) as `주문당평균가격`, count(order_item_id)/count(distinct order_id) as `평균판매상품수`, sum(price)/count(order_item_id) as `제품개당평균가격` from `olist.olist_order_items` as ord;
<br><br>

### [종합 쿼리]
* 실전 쿼리에서 구했던 지표들을 한번에 종합하여 집계하여 표시
* 조인해서 합친 다음 조건을 통해서 원하는 컬럼만 보도록 만든다.
* 중요한 것은 차근차근 하나씩 해나가야 에러가 안난다.
* 1번: 건당금액, 제품수 구하기
    * with tb as (
        select
            item.order_id,
            sum(item.price) as ord_amt,
            count(item.order_item_id) as prd_cnt
        from `olist.olist_order_items` as item
        group by item.order_id
    )
    * 결과를 임시 테이블에 담기
* 2번: 주문 정보 테이블에 1번의 결과와 고객 유니크 ID 붙이기
    * , base as (
        select
            ord.order_id,
            ord.customer_id,
            cust.customer_unique_id,
            tb.ord_amt,
            tb.prd_cnt
        from `olist.olist_orders` as ord
        left join `olist.olist_customers` as cust
            on ord.customer_id = cust.customer_id
        inner join tb
            on ord.order_id = tb.order_id
    )
* 3번: 2번 결과 집계하기
    * select
        sum(ord_amt) as `총매출`,
        count(distinct order_id) as `총주문수`,
        sum(prd_cnt) as `총판매상품수`,
        sum(ord_amt) / count(distinct order_id) as `주문당평균가격`,
        sum(prd_cnt) / count(distinct order_id) as `평균판매상품수`,
        sum(ord_amt) / sum(prd_cnt) as `제품개당평균가격`,
        count(distinct customer_unique_id) as `주문고객수`,
        count(distinct order_id) / count(distinct customer_unique_id) as `주문빈도`
    from base;
<br><br>

### [날짜별 지표 쿼리]
* 연도별 집계하기
    * 2번 셀렉트에 extract(year from ord.order_approved_at) as ord_year, 추가
    * 3번 셀렉트에 ord_year 추가
    * 3번 맨아래에 group by ord_year와 order by ord_year 적기 
<br><br>



## `[실습: 대시보드 데이터 만들기]`

### [데이터셋 준비]
* 쿼리 수정
* 1번
    * with tb as (
        select
            item.order_id,
            sum(item.price) as ord_amt,
            count(item.order_item_id) as prd_cnt
        from `olist.olist_order_items` as item
        group by item.order_id
    )
* 2번
    * , base as (
        select
            date(ord.order_approved_at) as ord_date,
            ord.order_id,
            ord.customer_id,
            cust.customer_unique_id,
            tb.ord_amt,
            tb.prd_cnt,
        from `olist.olist_orders` as ord
        left join `olist.olist_customers` as cust
            on ord.customer_id = cust.customer_id
        inner join tb
            on ord.order_id = tb.order_id
        where True
            and order_status in ('delivered', 'shipped')
            and order_approved_at is not null
    )
* 3번
    * select
        ord_date,
        round(sum(ord_amt), 2) as ord_amt,
        count(distinct order_id) as ord_cnt,
        sum(prd_cnt) as prd_cnt,
        round(ifnull(safe_divide(sum(ord_amt), count(distinct order_id)), 0), 2) as avg_ord_amt,
        round(ifnull(safe_divide(sum(prd_cnt), count(distinct order_id)), 0), 2) as avg_prd_cnt,
        round(ifnull(safe_divide(sum(ord_amt), count(distinct prd_cnt)), 0), 2) as avg_price,
        count(distinct customer_unique_id) as cust_cnt,
        round(ifnull(safe_divide(count(distinct order_id), count(distinct customer_unique_id)), 0), 2) as cust_freq
    from base
    group by ord_date
    order by ord_date
* 결과 저장 -> 구글시트 저장
<br><br>






