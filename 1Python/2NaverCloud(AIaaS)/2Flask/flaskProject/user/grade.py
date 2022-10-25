class Grade(object):
    def __init__(self, name, kr, en, ma):
        self.name = name
        self.kr = kr
        self.en = en
        self.ma = ma
        self.grade = self.calc_grade()

    def __str__(self):
        return f"{self.name}, {self.kr}, {self.en}, {self.ma}, {self.grade}"

    def calc_grade(self):
        avg = round((self.kr + self.en + self.ma)/3)
        grade = ""
        if avg >= 90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        elif avg >= 50: grade = "E"
        elif avg < 50: grade = "F"
        return grade

    @staticmethod
    def new_grade():
        name = input("Please input your name : ")
        kr = int(input("Please input your Korean score : "))
        en = int(input("Please input your English score : "))
        ma = int(input("Please input your Math score : "))
        return Grade(name, kr, en, ma)