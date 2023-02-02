def solution(common):
    answer = 0
    if common[0]-common[1] == common[1]-common[2]:
        answer = common[len(common)-1] + common[1] - common[0]
    elif common[0]/common[1] == common[1]/common[2]:
        answer = common[len(common)-1] * common[1] / common[0]
    return answer

print(solution([1,3,5,7]))
print(solution([2,4,8]))


#런타임 에러가 뜬다는 것이 힌트임....