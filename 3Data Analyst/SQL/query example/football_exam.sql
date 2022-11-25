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

-- 문제 6
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