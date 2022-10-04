class Solution :
    def solution(self, Kor, Math, Eng) :
        title = "Grade Table"
        answer = Kor + Math + Eng
        return f"{title}\nTotal : {answer}"

if __name__ == "__main__" :
    solution = Solution()
    Kor = int(input("input Kor Grade : "))
    Math = int(input("input Math Grade : "))
    Eng = int(input("input Eng Grade : "))
    print(solution.solution(Kor, Math, Eng))

















