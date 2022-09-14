#자료형 공부1(숫자)
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#자료형 공부2(문자)
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#자료형 공부3(Boolean)
print(5>10)
print(5<10)
print(True)
print(not True)
print(not (5 > 10))

#자료형 공부4(변수)
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = (age >= 3)

print("우리집" +animal+ "의 이름은" +name+ "에요")
hobby = "공놀이"
print(name+ "는" +str(age)+ "살이며, " +hobby+ "을 아주 좋아해요") #숫자는 스트링으로 변환
print(name+ "는 어른일까요? " +str(is_adult))

print("우리집" ,animal, "의 이름은" ,name, "에요") #콤마를 써도 되긴한데 띄어쓰기 강제사용됨
print(name, "는" ,age, "살이며, " ,hobby, "을 아주 좋아해요")
print(name, "는 어른일까요? " ,is_adult)

#자료형 공부5(주석)
#1줄짜리 주석은 #으로 처리
'''
이것도 주석이다 이마리야~~~ (여러줄 쓰고 싶을때 사용)
'''
#드래그 후에 Command + / 로 한번에 주석처리 가능

#Quiz풀이
station = "사당"
print(station+ "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+ "행 열차가 들어오고 있습니다.")
station = "인청공항"
print(station+ "행 열차가 들어오고 있습니다.")