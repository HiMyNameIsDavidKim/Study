"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
********************************
"""


class GradeTable(object):
    def __init__(self,name,kr,en,ma):
        self.name = name
        self.kr = kr
        self.en = en
        self.ma = ma
    
    def execute(self):
        self.calc_total()
        self.class_grade()
        self.print_table()

    def class_grade(self):
        avg = round(self.calc_total()/3)
        grade = ""
        if avg >= 90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        elif avg >= 50: grade = "E"
        elif avg < 50: grade = "F"
        return grade

    def calc_total(self):
        kr = self.kr
        en = self.en
        ma = self.ma
        return kr+en+ma

    def print_table(self):
        name = self.name
        kr = self.kr
        en = self.en
        ma = self.ma
        total = self.calc_total()
        avg = round(total/3)
        grade = self.class_grade()
        title = "### 성적표 ###"
        aster = "*"*30
        schema = "이름 국어 영어 수학 총점 평균 학점"
        result = f"{name} {kr} {en} {ma} {total} {avg} {grade}"
        print(f"{title}\n{aster}\n{schema}\n{aster}\n{result}\n{aster}")

    @staticmethod
    def main():
        name = input("Please input your name : ")
        kr = int(input("Please input your Korean score : "))
        en = int(input("Please input your English score : "))
        ma = int(input("Please input your Math score : "))
        gradetable = GradeTable(name,kr,en,ma)
        gradetable.execute()

GradeTable.main()