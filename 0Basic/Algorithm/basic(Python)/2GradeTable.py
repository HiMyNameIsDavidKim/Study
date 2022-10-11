class Solution :
    def solution(self, Kor, Math, Eng) :
        title = "[Grade Table]"
        total = Kor + Math + Eng
        avg = round(total/3)
        grade = ""
        if avg >= 90 :
            grade = "A"
        elif avg >= 80 :
            grade = "B"
        elif avg >= 70 :
            grade = "C" 
        elif avg >= 60 :
            grade = "D" 
        elif avg >= 50 :
            grade = "E" 
        elif avg < 50 :
            grade = "F"
        return f"{title}\nTotal : {total}\nAverage : {avg}\nGrade : {grade}"

if __name__ == "__main__" :
    solution = Solution()
    Kor = int(input("input Kor Grade : "))
    Math = int(input("input Math Grade : "))
    Eng = int(input("input Eng Grade : "))
    print(solution.solution(Kor, Math, Eng))

















