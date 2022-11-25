-- 문제 1    
-- 삼성블루윙즈 팀아이디는 무엇인가 ?

select team_id
from team
where team_name like ('삼성블루윙즈')
;

-- 문제 2
-- 전체 축구팀의 목록을 출력하시오
-- 단, 팀명을 오름차순으로 정렬하시오.

select *
from team
order by team_id
;
  
-- 문제 3
-- 포지션의 종류를 모두 출력하시오
-- 단, 중복은 제거합니다.

select distinct position
from player
;

-- 문제 4
-- mysql 에서 case 문 이용해서 다음 문제를 해결하세요
-- 포지션의 종류를 모두 출력하시오
-- 단, 중복은 제거합니다. 
-- 포지션이 없으면 신입으로 기재

select distinct
	case
		when position like '' then '신입'
		else position
	end as position
from player
;

-- 추가 문제
-- 다음 조건을 만족하는 선수명단을 출력하시오
-- 소속팀이 삼성블루윙즈이거나, 드래곤즈에 소속된 선수들이어야 하고
-- 포지션이 미드필더(MF:Midfielder)이어야 한다.
-- 키는 170 센티미터 이상이고 180 이하여야 한다.

select player_name
from player
where (team_id like 
		(select team_id
		from team
		where team_name like ('삼성블루윙즈')) 
	or team_id like
		(select team_id
		from team
		where team_name like ('드래곤즈')))
	and position like 'MF'
	and (height between 170 and 180)
;

-- 조인 문제1
-- 2012년 3월 17일 경기에
-- 포항 스틸러스 소속 골키퍼(GK)
-- 선수, 포지션,팀명 (연고지포함),
-- 스타디움, 경기날짜를 구하시오
-- 연고지와 팀이름은 간격을 띄우시오(수원[]삼성블루윙즈)

select 
	p.player_name, p.POSITION,
	concat(t.region_name, ' ', t.team_name) as reigo_team,
	st.stadium_name, s.sche_date
from `SCHEDULE` as s
	inner join team as t using(stadium_id)
	inner join player as p using(team_id)
	inner join stadium as st using(hometeam_id)
where s.sche_date like '20120317'
	and t.region_name like '포항'
	and p.POSITION like 'GK'
;

-- 조인 문제 2
-- 포지션이 MF 인 선수들의 소속팀명 및  선수명, 백넘버 출력

select t.team_name, p.player_name, p.back_no
from player as p
	inner join team as t using(team_id)
where p.POSITION like 'MF'
;

-- 조인 문제 3
-- 가장 키큰 선수 5명 소속팀명 및  선수명, 백넘버 출력, 
-- 단 키  값이 없으면 제외

select t.team_name, p.player_name, p.back_no
from player as p
	join team as t using(team_id)
order by height desc
limit 5
;

-- 조인 문제 4
-- 2012년 5월 한달간 경기가 있는 경기장  조회

select st.stadium_name
from `SCHEDULE` as s
	join stadium as st using(stadium_id)
where s.sche_date like '201205%'
;

-- 서브쿼리 문제 1
-- 수원을 연고지로 하는팀의 골키퍼는
-- 누구인가 ?

select player_name
from player
where position like 'GK'
	and team_id like (select team_id
						from team
						where region_name like '수원')
;

-- 서브쿼리 문제 2
-- 수원 연고팀에서 키가 170 이상 선수
-- 이면서 성이 고씨인 선수는 누구인가

select player_name
from player
where player_name like '고%'
	and height >= 170
	and team_id like (select team_id
						from team
						where region_name like '수원')
;

-- 문제 7
-- 포항팀 선수들 이름과
-- 키와 몸무게 목록을 출력하시오
-- 키와 몸무게가 없으면 "0" 표시하시오
-- 키와 몸무게는  내림차순으로 정렬하시오

select player_name,
		(case when height like '' then '0' else height end) as height,
		(case when weight like '' then '0' else weight end) as weight
from player
where team_id like (select team_id
						from team
						where region_name like '포항')
order by height desc
;

-- 문제 8
-- 서울팀 선수들 이름과 포지션과
-- 키(cm표시)와 몸무게(kg표시)와  각 선수의 BMI지수를 출력하시오
-- 단, 키와 몸무게가 없으면 "0" 표시하시오
-- BMI는 "NONE" 으로 표시하시오(as bmi)
-- 최종 결과는 이름내림차순으로 정렬하시오

select player_name, position,
		(case when height like '' then '0' else concat(height, 'cm') end) as height,
		(case when weight like '' then '0' else concat(weight, 'kg') end) as weight,
		(case when height like '' then 'None' 
		else round(weight * 10000 / (height*height)) end) as bmi
from player
where team_id like (select team_id
						from team
						where region_name like '서울')
order by player_name desc
;

-- 문제 9
-- 4개의 테이블의 키값을 가지는 가상 테이블을 생성하시오 (join)
-- 카티전 프로덕트 8,195 행

select *
from player as p
	join team as t
;

-- 문제 10
-- 수원팀(K02) 과 대전팀(K10) 선수들 중 포지션이 골키퍼(GK) 인 
-- 선수를 출력하시오
-- 단 , 팀명, 선수명 오름차순 정렬하시오

select player_name
from player
where position like 'GK'
	and (team_id like (select team_id
						from team
						where region_name like '수원')
		or
		team_id like (select team_id
						from team
						where region_name like '대전'))
order by player_name asc
;

-- 문제 11
-- 팀과 연고지를 연결해서 출력하시오
-- [팀 명]             [홈구장]
-- 수원[ ]삼성블루윙즈 수원월드컵경기장  

select concat(region_name, ' ', team_name) as '팀 명',
		stadium_name as '홈구장'
from team as t
	join stadium as s on (t.team_id = s.hometeam_id)
;

-- 문제 12
-- 수원팀(K02) 과 대전팀(K10) 선수들 중
-- 키가 180 이상 183 이하인 선수들
-- 키, 팀명, 사람명 오름차순

select p.height, t.team_name, p.player_name
from team as t
	join player as p using(team_id)
where (t.region_name like '수원'
		or t.region_name like '대전')
	and p.height between 180 and 183
order by player_name asc
;

-- 문제 13
-- 모든 선수들 중 포지션을 배정 받지 못한 선수들의 
-- 팀명과 선수이름 출력 둘다 오름차순

select p.player_name,
	(select t.team_name from team as t where t.team_id = p.team_id) as team_id
from player as p
where p.POSITION like ''
order by player_name asc
;

-- 문제 14
-- 팀과 스타디움, 스케줄을 조인하여
-- 2012년 3월 17일에 열린 각 경기의
-- 팀이름, 스타디움, 어웨이팀 이름 출력
-- 다중테이블 join 을 찾아서 해결하시오.

select sche_date,
	(select t.team_name from team as t where t.team_id = sc.hometeam_id) as home,
	(select t.team_name from team as t where t.team_id = sc.awayteam_id) as away,
	(select stadium_name from stadium as s where s.hometeam_id = sc.hometeam_id) as stadium
from `SCHEDULE` as sc
where sche_date like 20120317
;

-- 문제 15 
-- 2012년 3월 17일 경기에
-- 선수, 포지션,팀명 (연고지포함),
-- 스타디움, 경기날짜를 구하시오
-- 연고지와 팀이름은 간격을 띄우시오(수원[]삼성블루윙즈)

SELECT p.player_name, 
			p.`POSITION`, 
			CONCAT(t.team_name, ' ', t.region_name) AS 팀명,
			c.sche_date
FROM stadium s
	JOIN schedule c using(stadium_id)
	JOIN team t using(stadium_id)
	JOIN player p using(team_id)
WHERE c.sche_date LIKE '20120317'
	AND t.region_name LIKE '포%'
	AND p.`POSITION` LIKE 'GK' 
;

-- 문제 16 
-- 홈팀이 3점이상 차이로 승리한 경기의
-- 경기장 이름, 경기 일정
-- 홈팀 이름과 원정팀 이름을
-- 구하시오

select sche_date,
	(select t.team_name from team as t where t.team_id = sc.hometeam_id) as home,
	(select t.team_name from team as t where t.team_id = sc.awayteam_id) as away,
	(select stadium_name from stadium as s where s.hometeam_id = sc.hometeam_id) as stadium
from `SCHEDULE` as sc
where (home_score - away_score) >= 3
;
-- 문제 18 (추가 문제)
-- 다음 조건을 만족하는 선수명단을 출력하시오
-- 소속팀이 삼성블루윙즈이거나
-- 드래곤즈에 소속된 선수들이어야 하고,
-- 포지션이 미드필더(MF:Midfielder)이어야 한다.
-- 키는 170 센티미터 이상이고 180 이하여야 한다.

-- 문제 19 (그룹바이: 집계함수 - 딱 5개 min, max, count, sum, avg)
-- 평균키가 인천 유나이티스팀('K04')의 평균키  보다 작은 팀의
-- 팀ID, 팀명, 평균키 추출
-- 인천 유나이티스팀의 평균키 -- 176.59  
-- 키와 몸무게가 없는 칸은 0 값으로 처리한 후 평균값에 
-- 포함되지 않도록 하세요.

-- 문제 20
-- 포지션이 MF 인 선수들의 소속팀명 및  선수명, 백넘버 출력

select 
	(select t.team_name from team as t where t.team_id = p.`team_id`) as team,
	p.player_name,
	p.back_no
from player as p
where p.`POSITION` LIKE 'MF'
;

-- 문제 21
-- 가장 키큰 선수 5명 소속팀명 및  선수명, 백넘버 출력, 
-- 단 키  값이 없으면 제외

select
	(select t.team_name from team as t where t.team_id = p.`team_id`) as team,
	p.player_name,
	p.back_no
from player as p
order by height desc
limit 5
;

-- 문제 22
-- 선수 자신이 속한 팀의 평균키보다 작은  선수 정보 출력

-- 문제 23
-- 2012년 5월 한달간 경기가 있는 경기장  조회

select sche_date,
	(select stadium_name from stadium as s where s.stadium_id = sc.stadium_id) as stadium
from `SCHEDULE` as sc
where sc.sche_date like '201205%'
;