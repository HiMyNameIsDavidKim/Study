#반복문 공부1(if문)
weather = input("What is weather today?")
if weather == "rain" or weather == "snow" :
    print("Keep umbrella")
elif weather == "dust" :
    print("Keep mask")
else :
    print("Just go")

#반복문 공부2(if문 심화)
temp = int(input("How about today's temperature?"))
if 30 <= temp :
    print("Too hot, don't go out")
elif 10 <= temp and temp < 30 :
    print("Good Day")
elif 0 <= temp < 10 :
    print("Take a cloth")
else : 
    print("It is too cold, don't go out")

#반복문 공부3(for문)
for Waiting_No in range(5) : #range(5)는 range(1,6)으로 대체 가능
    print("Waiting No : {0}".format(Waiting_No))
starbucks = ["IronMan", "Thor", "Groot"]
for customer in starbucks : 
    print("{0}, You can take coffee".format(customer))

#반복문 공부3(While문 단순반복)
customer = "Thor"
index = 5
while index >= 1 :
    print("{0}, You can take coffee. {1} times left.".format(customer, index-1))
    index -= 1
    if index == 0 :
        print("I will threw coffee.")

#반복문 공부4(While문 조건반복)
customer = "Thor"
person = "Unknown"
while person != customer :
    print("{0}, You can take coffee.".format(customer))
    person = input("What is your name?")
    if person != "Thor" :
        print("This coffee is for Thor.")
    elif person == "Thor" :
        print("Have a nice day. sir.")

#반복문 공부5(continue&break)
absent = [2,5]
no_book = [7]
for student in range(1,11) :
    if student in absent :
        continue #조건에 걸리면 아래 코드 skip하고 다음 반복 실행함
    if student in no_book :
        print("this is for today. {0}, come to office.".format(no_book))
        break #조건에 걸리면 당장 반복문 끝냄
    print("{0}, read book.".format(student))

#반복문 공부6(한줄for문)
students = list(range(1,6))
print(students)
students = [i+100 for i in students]
#students에서 i를 하나씩 불러오며 i+100으로 '대체'하라.
print(students)
students_names = ["IronMan", "Thor", "Groot"]
print(students_names)
students_names = [len(i) for i in students_names]
#i를 하나씩 불러오며 길이로 '대체'하라.
print(students_names)
students_big = ["IronMan", "Thor", "Groot"]
print(students_big)
students_big = [i.upper() for i in students_big]
#i를 하나씩 불러오며 대문자로 '대체'하라.
print(students_big)

#Quiz 풀이
from random import *
i = 0

for customer in range(1,51) :
    min = randrange(5,51) #5~51 사이에서 1개 무작위 도출
    if 5 <= min <= 15 :
        choose = "O"
        i += 1
    else :
        choose = " "
    print("[{2}] {0}번째 손님 (소요시간 : {1}분)".format(customer,min,choose))
print("총 탑승 승객 : {0}명".format(i))








