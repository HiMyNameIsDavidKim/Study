def solution(n, score):
    score.split()
    sum = 0
    for i in range(0,n):
        sum += score[i]
    print(sum)

if __name__ == "__main__":
    n = int(input())
    score = input()
    solution(n, score)