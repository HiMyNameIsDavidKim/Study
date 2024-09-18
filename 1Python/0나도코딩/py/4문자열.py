#문자열 공부1(기본)
sentence = '나는 소년입니다.'
print(sentence) #작따
sentence2 = "파이썬은 쉬워요."
print(sentence2) #큰따
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3) #띄어쓰기 가능

#문자열 공부2(슬라이싱)
jumin = "951113-1234567"
print("sex : " + jumin[7]) #한글자만 뽑아낼때 사용 #0부터 시작함 주의
print("year : " + jumin[0:2]) #0부터 2직전 까지 가져옴 주의 (=0이상 2미만)
print("month : " + jumin[2:4]) 
print("day : " + jumin[4:6])
print("YYMMDD : " + jumin[0:6])
print("YYMMDD : " + jumin[:6]) #윗줄이랑 동일, 생략하면 처음부터
print("code : " + jumin[7:14])
print("code : " + jumin[7:]) #윗줄이랑 동일, 생략하면 끝까지
print("code(from back) : " + jumin[-7:]) #뒤에서 7번째~끝까지

#문자열 공부3(문자열 처리 함수1)
python = "Python is Amazing"
print(python.lower()) #전체 소문자
print(python.upper()) #전체 대문자
print(python[0].isupper()) #대문자인지 확인, 불린 답변
print(len(python)) #길이 반환
print(python.replace("Python", "Java")) #찾아서 바꾸기
print(python.replace("Python", "")) #제거에도 활용 가능함

#문자열 공부4(문자열 처리 함수2)
print(python.count("n")) #특정 문자가 몇개?
index = python.index("n") #특정 문자가 몇번째에?
print(index) #index 함수는 선언해야 프린트 가능
index = python.index("n", index + 1) #2번째로 나온게 몇번째에?
print(index)
print(python.find("Java")) #index함수랑 유사하나, 없는 것도 확인 가능
#print(python.index("Java")) #인덱스는 오류남, 멈춰버림.

#문자열 공부5(문자열 포맷1)
print("a" + "b") #기본1
print("a", "b") #기본2
print("나는 %d살 입니다." % 20) #d는 정수를 의미함
print("나는 %s를 좋아해요." % "파이썬") #s는 string(문자열)을 의미함
print("Apple은 %c로 시작해요." % "A") #c는 1글자만 가져옴
#%s가 범용적이라, 이걸 주로 사용하면 다른건 안써도 됨.
print("I like %s color and %s color." % ("blue", "red")) #여러개 가능

#문자열 공부6(문자열 포맷2)
print("I'm {} years old.".format(20))
print("I like {} color and {} color.".format("blue", "red")) #여러개 가능
print("I like {0} color and {1} color.".format("blue", "red")) #순서 지정 가능
print("I like {1} color and {0} color.".format("blue", "red"))
print("I'm {age} years old and I like {color} color.".format (age = 20, color = "red")) #변수 선언도 가능
age = 20
color = "red"
print(f"I'm {age} years old and I like {color} color.") #f로 시작하면 변수 가져올 수도 있음, 직관적이라 베스트인듯

#문자열 공부7(탈출 문자)
# \n : line change
print("백문이 불여일견\n백견이 불여일타")
# \" : 문자열 안에서 큰따옴표를 쓰고 싶을때 사용
print("저는 \"나도코딩\" 입니다.")
# \\ : 문자열 안에서 \를 쓰고 싶을때 사용
print("C:\\Users\\Desktop")
# \r : 커서를 맨 앞으로 이동, 문자가 있으면 인서트 해서 작성함
print("Red Apple\rPine")
# \b : 백스페이스
print("Redd\b Apple")
# \t : Tab
print("Red\t Apple")

#Quiz 풀이
site1 = "http://naver.com"
site2 = site1.replace("http://","") #규칙1, 리플레이스로 제거하는 스킬
site3 = site2[:site2.index(".")] #규칙2, 인덱스로 특정문자를 찾아내서 거기 직전까지 쓰겠다는 거임
password = site3[:3] + str(len(site3)) + str(site3.count("e"))
print(f"{site1}, This site password is {password}" + "!")



