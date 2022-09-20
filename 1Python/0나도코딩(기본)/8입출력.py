#입출력 공부1(표준)
print("Python", "Java") #띄어서 나옴
print("Python" + "Java") #붙어서 나옴
print("Python", "Java", sep = ",") #세퍼레이트로 어떻게 구분할지 정할 수 있음.
print("Python", "Java", sep = " vs ")
print("Python", "Java", sep = ",", end = "?") #끝맺음을 엔터 말고 다른 걸로 정할 수 있음.
print("Which one is fun to you?")

import sys
print("Python", "Java", file = sys.stdout) #표준출력
print("Python", "Java", file = sys.stderr) #표준에러

#정렬하는 방법
scores = {"Math":0, "English":50, "Cording":100}
for subject, score in scores.items() : 
    print(subject.ljust(8), str(score).rjust(4), sep = ":") #왼쪽정렬 오른쪽정렬 하는법, 글자수 지정해줘야함

#대기 순번표
for num in range(1,21) : 
    print("waiting No : " + str(num).zfill(3)) #3자리수로 고정하는 방법

# answer = input("input any keys : ")
# print("your input is " + answer + ".")
# print(type(answer)) #인풋은 뭐를 적든 항상 스트링으로 설정된다?!


#입출력 공부2(다양한 출력 포맷)
#빈자리는 빈공간으로 두고,오른쪽 정렬, 총 10자리 공간 확보
print("{0: >10}".format(500)) #0에 대해서, 스페이스바는 앞에 빈공간 둬라, >는 오른쪽 정렬, 10은 총 10자리 확보
#양수는 +표시, 음수는 -표시
print("{0: >+10}".format(500)) #+ 입력해주면 됨.
print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))
print("{0:_<+10}".format(500))
#3자리 마다 콤마 찍어주기
print("{0:,}".format(10000000000))
print("{0:+,}".format(10000000000))
#3자리 마다 콤마 찍기, 부호 붙이기, 자리수 확보, 빈자리는 웃음
print("{0:^<+30,}".format(10000000000))
#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리까지만 출력
print("{0:.2f}".format(5/3)) #반올림이 기본 세팅임


#입출력 공부3(파일 입출력)
#2번째 값은 용도임. w는 쓰기, a는 이어쓰기, r은 읽어오기
# #파일 실제로 하나 만들기
# #변수에다가 파일을 여는 기능을 걸꺼임.
# score_file = open("score.text", "w", encoding="utf8") #한글 쓰려면 encoding="utf8" 써야함.
# print("Math : 0", file = score_file)
# print("English :50", file = score_file)
# score_file.close() #꼭 닫아줘야함.
#파일 수정하기
# score_file = open("score.text", "a", encoding="utf8")
# score_file.write("Science : 80")
# score_file.write("\ncoding : 100")
# score_file.close()
#모든 내용 다 읽기
score_file = open("score.text", "r", encoding="utf8")
print(score_file.read())
score_file.close()
#한줄씩 읽기
score_file = open("score.text", "r", encoding="utf8")
print(score_file.readline(), end="") #기본이 줄바꿈이라 지워줄 수 있음.
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
#몇줄인지 모를때 읽어오기
score_file = open("score.text", "r", encoding="utf8")
while True : 
    line = score_file.readline()
    if not line :
        break
    print(line, end="") #기본이 줄바꿈이라 지워줄 수 있음.
score_file.close()
#리스트 형태로 저장하고 출력
score_file = open("score.text", "r", encoding="utf8")
lines = score_file.readlines() #list 형태로 저장.
for line in lines : 
    print(line, end="")
score_file.close()


#입출력 공부3(피클)
#wb는 w뒤에 b(바이너리)를 적어준 것. 피클은 항상 바이너리 정의를 해줘야함.
import pickle
#피클이라는 입출력 모듈이 있는데 이걸 써볼거야.
profile_file = open("profile.pickle", "wb")
profile = {"name" : "Park", "age" : 30, "hobby" : ["football", "golf", "coding"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close()











