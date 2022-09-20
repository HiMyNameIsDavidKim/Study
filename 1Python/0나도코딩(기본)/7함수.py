#함수 공부1(개념)
#일종의 박스라고 생각하면 됨.
#5라는 값을 박스에 넣으면, 20을 더한 값을 줌.
def open_account() :
    print("new account is opened")

open_account()


#함수 공부2(전달값과 반환값)
def deposit(balance, money) :
    print("Deposit is completed. now balance is {0}".format(balance + money))
    return balance + money

account1 = 0
account1 = deposit(account1, 1000)

def withdraw(balance, money) :
    if balance >- money :
        print("Withdraw is completed. now balance is {0}".format(balance - money))
        return balance - money
    else :
        print("Withdraw is failed. now balance is {0}.".format(balance))    
        return balance

account2 = 0
account2 = deposit(account2, 1000)
account2 = withdraw(account2, 500)

def withdraw_night(balance, money) : 
    commission = 100
    print("Commission is {0}, now balance is {1}".format(commission, balance - money - commission))
    return commission, balance - money - commission

account3 = 2000
account3 = withdraw_night(account3, 1000)


#함수 공부3(기본값)
#동일한 입력값이 계속 있을 때 사용
def profile(name, age, main_lang) :
    print("이름 : {0} \t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

def profile(name, age = 17, main_lang = "파이썬") : #기본값 입력법
    print("이름 : {0} \t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석") #이름만 입력해줘도 됨. 기본 저장된 값은 그대로 있음.
profile("김태호")


#함수 공부4(키워드값)
#순서대로 입력하기 싫을 때 사용
def profile(name, age, main_lang) :
    print(name, age, main_lang)

profile("You", 20, "Python")
profile(name = "Kim", main_lang = "Java", age = 25) #굳이 순서대로 안해도 됨


#함수 공부5(가변 인자)
#여러 개의 인자를 원하는 갯수만큼 입력하고 싶을 때 사용
def profile(name, age, lang1, lang2, lang3, lang4, lang5) : 
    print("name : {0}\tage : {1} \t".format(name, age), end = " ") #, end = " " 하면 줄바꿈 없이 계속 쓸 수 있음.
    print(lang1, lang2, lang3, lang4, lang5)

profile("You", 20, "Python", "Java", "C", "C++", "C#")
profile("Kim", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language) : 
    print("name : {0}\tage : {1} \t".format(name, age), end = " ") #, end = " " 하면 줄바꿈 없이 계속 쓸 수 있음.
    for lang in language :
        print(lang, end=" ")
    print()

profile("You", 20, "Python", "Java", "C", "C++", "C#", "JS")
profile("Kim", 25, "Kotlin", "Swift")


#함수 공부6(지역변수, 전역변수)
#지역변수 = 함수 내에서만 쓸 수 있는 변수
#전역변수 = 어떤 상황에서든 부를 수 있는 변수
gun = 10 #얘는 전역변수

def checkpoint(soldiers) :
    #gun = 20 #얘는 지역변수 선언 방법
    global gun #전역변수를 불러서 쓰겠다. 
    gun = gun - soldiers
    print("[in function] left gun : {0}".format(gun))

print("Total gun : {0}".format(gun)) #초기 전역변수
checkpoint(2) #함수 사용시 함수 내에서 전역변수
print("left gun : {0}".format(gun)) #함수 쓰고 나서 저장까지 됐음

#근데 위 방법은 권장하지는 않음. 리턴을 쓰는게 더 보편적임.
def checkpoint_ret(gun, soldiers) : 
    gun = gun - soldiers
    print("[in function] left gun : {0}".format(gun))
    return gun

print("Total gun : {0}".format(gun)) #초기 전역변수
gun = checkpoint_ret(gun, 2) #함수 사용시 함수 내에서 전역변수
print("left gun : {0}".format(gun)) #함수 쓰고 나서 저장까지 됐음


#퀴즈 풀이
def std_weight(height, gender) : 
    if gender == "M" :
        weight = round(height/100 * height/100 * 22, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, weight))
    elif gender == "W" :
        weight = round(height/100 * height/100 * 21, 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, weight))

std_weight(175,"M")
std_weight(165,"W")






