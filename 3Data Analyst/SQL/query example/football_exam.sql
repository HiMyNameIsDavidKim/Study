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
		when position = '' then '신입'
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