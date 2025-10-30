'''
[설명]
게시판 불량 이용자 신고 처리 결과 메일 발송
한번에 한명 유저 신고 가능 (무제한)
여러번 신고 가능하지만 1번으로 처리
k번 이상 신고 유저는 정지 -> 신고한 유저에게 알림 메일

아이디어:
DP테이블 신고당한 사람 저장, 중복 안되게 set 사용
메일 보내야 하는 목록은 또 따로 처리해야함

변수:
이용자의 ID 문자 배열, id_list
신고 로그, report
정지 기준, k
'''

'''
[리뷰]
1. 리스트에서 인덱스 호출: list.index(value)
'''


def solution(id_list, report, k):
    log_report = [set()] * len(id_list)
    mailed_user = [0] * len(id_list)
    
    for r in report:
        reporter, bad_guy = r.split()
        idx = id_list.index(bad_guy)
        if len(log_report[idx]) == 0:
            log_report[idx] = set([reporter])
        else:
            log_report[idx].add(reporter)
    
    for log in log_report:
        for l in list(log):
            if len(log) >= k:
                idx = id_list.index(l)
                mailed_user[idx] += 1
    
    return mailed_user


