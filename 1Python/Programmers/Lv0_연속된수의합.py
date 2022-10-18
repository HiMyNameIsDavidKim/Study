def solution(num, total):
    answer = []
    if num % 2 == 0:
        mid = int(total/num)
        first = int(mid-int(num/2)+1)
        for i in range(first,first+num):
            answer.append(i)
    else:
        mid = int(total/num)
        first = int(mid-int(num/2))
        for i in range(first,first+num):
            answer.append(i)
    return answer

print(solution(3,12))
print(solution(5,15))
print(solution(4,14))
print(solution(5,5))
print(solution(3,0))
print(solution(5,3))

