def solution(A, B):
    answer = 0
    for i in range(0,len(A)):
        if A == B: break
        cut_end = A[len(A)-1]
        A= cut_end+A[0:len(A)-1]
        answer += 1
        if answer == len(A): answer = -1
    return answer

print(solution("hello","ohell"))
print(solution("apple","elppa"))