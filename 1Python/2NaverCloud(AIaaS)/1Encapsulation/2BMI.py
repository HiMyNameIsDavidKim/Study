class Bmi(object):
    def __init__(self, name, m, kg): #입력
        self.name = name
        self.m = m
        self.kg = kg
        self.index = ""

    def execute(self): #로직의 순서
        self.index = self.getIndex()
        self.getIndex()
        self.printIndex()

    def getBmi(self): #비즈니스 로직1
        kg = self.kg
        m = self.m
        return (kg) / (m ** 2)

    def getIndex(self): #비즈니스 로직2
        index = ""
        bmi = self.getBmi()
        if bmi >= 35: index = "고도 비만"
        elif bmi >= 30: index = "중도 비만"
        elif bmi >= 25: index = "경도 비만"
        elif bmi >= 23: index = "과체중"
        elif bmi >= 18.5: index = "정상"
        elif bmi < 18.5: index = "저체중"
        self.index = index

    def printIndex(self): #출력
        name = self.name
        m = self.m
        kg = self.kg
        index = self.index
        title = "### Body Mass Index ###"
        aster = "*"*30
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        result = f"{name} {m*100} {kg} {index}"
        print(f"{title}\n{aster}\n{schema}\n{aster}\n{result}\n{aster}")

    @staticmethod
    def main():
        name = input("Please input your name : ")
        m = float(input("Please input your height(m) : "))
        kg = int(input("Please input your weight(kg) : "))
        bmi = Bmi(name, m, kg)
        bmi.execute()

Bmi.main()