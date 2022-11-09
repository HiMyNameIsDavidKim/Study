def solution(n, score):
    score = score.split()
    score_list = []
    sum_new_score = 0
    for i in range(0,n):
        score_list.append(int(score[i]))
    for i in score_list:
        sum_new_score += i/max(score_list)*100
    print(sum_new_score/n)

if __name__ == "__main__":
    n = int(input())
    score = input()
    solution(n, score)