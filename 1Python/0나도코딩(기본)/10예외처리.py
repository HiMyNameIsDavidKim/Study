#예외처리 공부1(기본)
#에러 발생 시 처리해주는 것
#ex. 문자에 숫자를 입력, 형식에 맞지 않게 작성
try : #예외처리하려면 이 안에 넣어줘야함.
    print("Calculator for only divide.")
    nums = []
    nums.append(int(input("Please input first number. : ")))
    nums.append(int(input("Please input second number. : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError : #여기서 지정해준 오류에서만 아래 코드가 진행됨.
    print("Error! strange value inputed.")
except ZeroDivisionError as err : #이렇게 하면 에러에서 발생하는 문장을 그대로 출력할 수 있음.
    print(err) 
except Exception as err : #그 외 나머지 에러는 다 이렇게 처리할 수도 있음.
    print("Unknown Error came out.")
    print(err)


#예외처리 공부2(한 자리 숫자만 나누는 계산기)
try :
    print("Calculator for only 1 length number.")
    num1 = int(input("Please input first number. : "))
    num2 = int(input("Please input second number. : "))
    if num1 >= 10 or num2 >= 10 :
        raise ValueError #해당 에러로 지정하겠다.
    print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError :
    print("Error! strange number inputed. please input only 1 length number.")


#예외처리 공부3(사용자 정의 예외처리)











