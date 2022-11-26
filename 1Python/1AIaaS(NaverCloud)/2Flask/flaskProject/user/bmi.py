class Bmi(object):
    def __init__(self, name, m, kg):
        self.name = name
        self.m = m
        self.kg = kg
        self.index = self.get_index()

    def __str__(self):
        return f"{self.name}, {self.m}, {self.kg}, {self.index}"

    def get_index(self):
        m = self.m
        kg = self.kg
        bmi = kg / (m ** 2)
        if bmi >= 35: index = "고도 비만"
        elif bmi >= 30: index = "중도 비만"
        elif bmi >= 25: index = "경도 비만"
        elif bmi >= 23: index = "과체중"
        elif bmi >= 18.5: index = "정상"
        elif bmi < 18.5: index = "저체중"
        return index

    @staticmethod
    def new_bmi():
        name = input("이름 : ")
        m = float(input("키 : "))
        kg = int(input("몸무게 : "))
        return Bmi(name, m, kg)