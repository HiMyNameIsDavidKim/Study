class Bmi(object):
    def __init__(self, name, m, kg):
        self.name = name
        self.m = m
        self.kg = kg

    def printIndex(self):
        title = "### Body Mass Index ###"
        aster = "*"*30
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        bmi = (self.kg) / (self.m * self.m)
        if bmi >= 35 : self.index = "고도 비만"
        elif bmi >= 30 : self.index = "중도 비만"
        elif bmi >= 25 : self.index = "경도 비만"
        elif bmi >= 23 : self.index = "과체중"
        elif bmi >= 18.5 : self.index = "정상"
        elif bmi < 18.5 : self.index = "저체중"
        result = f"{self.name} {self.m*100} {self.kg} {self.index}"
        print(f"{title}\n{aster}\n{schema}\n{aster}\n{result}\n{aster}")

if __name__ == "__main__":
    name = input("Please input your name : ")
    m = float(input("Please input your height(m) : "))
    kg = int(input("Please input your weight(kg) : "))
    bmi = Bmi(name, m, kg)
    bmi.printIndex()