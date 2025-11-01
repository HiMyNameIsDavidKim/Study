'''
[설명]
재택근무와 함께 출근 희망 시각을 자유롭게 결정
각자 설정한 출근 희망 시각에 늦지 않고 출근한 직원 = 상품
출근 희망 시각 +10분 까지 어플로 출근 체크 일주일 진행
(토요일, 일요일은 이벤트 영향 x)
시간은 1013, 958 이런식으로 계산됨

상품을 받을 직원은 몇명?

[아이디어]
startday로 timelogs 다시 정렬 후 토일 날리기
직원 한명씩 돌면서 시간보다 작은지 확인

[변수]
직원 수, n
출근 희망 시각 1차원 배열, schedules
직원 일주일 출근 시각 2차원 배열, timelogs
이벤트 시작 요일, startday
'''

'''
[리뷰]
1. 둘째자리 수 비교하기: limit % 100 >= 60
'''

def solution(schedules, timelogs, startday):
    answer = 0
    
    sorted_logs = [timelog[7-startday+1:] + timelog[:7-startday+1] for
                  timelog in timelogs]
    
    for sch, logs in zip(schedules, sorted_logs):
        limit = sch+10
        if limit % 100 >= 60:  # 분이 60 이상이면
            limit = limit + 100 - 60
        
        latest = max(logs[:5])
        if limit >= latest:
            answer += 1
        
    return answer
