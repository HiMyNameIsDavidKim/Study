'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))
BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.
### 비만도 계산 ###
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
이순신 170 79 정상
유관순 170 79 정상
***************************
'''


class Bmi(object):

    def __init__(self, name, cm, kg) -> None:
        self.name = name
        self.cm = cm
        self.kg = kg
        self.biman = ""

    def __str__(self):
        return f'{self.name} {self.cm} {self.kg} {self.biman}'

    @staticmethod
    def new_bmi():
        name = input("이름: ")
        cm = float(input("키: "))
        kg = float(input("몸무게: "))
        return Bmi(name, cm, kg)

    def get_bmi(self):
        kg = self.kg
        m = self.cm / 100
        return kg / m ** 2

    def get_biman(self):
        biman = ""
        bmi = self.get_bmi()
        if bmi >= 35:
            biman = "고도비만"
        elif bmi >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif bmi >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        self.biman = biman

    @staticmethod
    def result(ls):
        print("### 비만도 계산 ###")
        print("*" * 40)
        print("이름 키(cm) 몸무게(kg) 비만도")
        [print(i) for i in ls]
        print("*" * 40)




