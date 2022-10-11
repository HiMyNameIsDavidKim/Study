#상단에 문제 써놓고 시작하는 습관 필요함.
"""
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
bmi 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))

bmi 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만

이름 키 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
***************************
"""

class Solution :
    def solution(self, name, m, kg) :
        title = "[Body Mass Index]"
        aster = "*"*30
        bmi = (kg) / (m * m)
        index = "" #자연어를 출력할 때는 항상 빈걸로 선언 먼저 해줘야함.
        if bmi >= 35 : index = "고도 비만" #if문에서 짧으면 붙여서 써도 무관함.
        elif bmi >= 30 : index = "중도 비만"
        elif bmi >= 25 : index = "경도 비만"
        elif bmi >= 23 : index = "과체중"
        elif bmi >= 18.5 : index = "정상"
        elif bmi < 18.5 : index = "저체중"
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        values = f"{name} {round(m*100)} {kg} {index}" #f스트링 쓰는 연습 해야함. 속도도 제일 빠르고 직관적임.
        return f"{aster}\n{title}\n{aster}\n{schema}\n{aster}\n{values}\n{aster}"

if __name__ == "__main__" :
    solution = Solution()
    name = input("Please input your name : ")
    m = float(input("Please input your height(m) : "))
    kg = int(input("Please input your weight(kg) : "))
    print(solution.solution(name, m, kg))






















