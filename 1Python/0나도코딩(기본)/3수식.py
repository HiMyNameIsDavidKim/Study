#수식 공부1(간단 수식)
print(2 + 3 * 4)
print((2+ 3) * 4)

#수식 공부2(변수 활용)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2 #(number = number + 2) 랑 같은 문장임
print(number)
number *= 2 #(number = number * 2) 랑 같은 문장임
print(number)
number /= 2 #(number = number / 2) 랑 같은 문장임
print(number)
number -= 2 #(number = number - 2) 랑 같은 문장임
print(number)
number %= 2 #(number = (number / 2)의 나머지) 랑 같은 문장임
print(number)

#수식 공부3(숫자 처리 함수)
print(abs(-5)) #absolute, 절대값
print(pow(4, 2)) #power, 제곱
print(max(5, 12)) #최대값
print(min(5, 12)) #최소값
print(round(4.99)) #반올림

#수식 공부4(math 라이브러리 활용)
from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

#수식 공부4(random 라이브러리 활용)
from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값을 생성함
print(random() * 10) #0 ~ 10 미만의 임의의 값을 생성함
print(int(random() * 10)) #0 ~ 10 미만의 임의의 값(정수)
print(int(random() * 10) + 1) #1 ~ 10 이하의 임의의 값(정수)
print(int(random() * 45) + 1) #1 ~ 45 이하의 임의의 값(정수)
print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성
print(randint(1,45)) #1 ~ 45 이하의 임의의 값 생성

#Quiz 풀이
from random import *
on1 = randint(4,28)
on2 = randint(4,28)
on3 = randint(4,28)
off1 = randint(4,28)
print("온라인 스터디 날짜는 "+str(on1)+ "일과 " +str(on2)+ "일과 " +str(on3)+"일 이며,")
print("오프 스터디 날짜는 "+str(off1)+"일 입니다.")