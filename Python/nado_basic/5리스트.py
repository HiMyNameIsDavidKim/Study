#리스트 공부1(리스트, 대괄호)
#리스트는 순서를 가지는 객체의 집합이다.
#리스트는 자료형이 달라도 같이 넣을 수 있음.
subway = [10, 20, 30]
print(subway)
subway = ["You", "Choi", "Park"] #문자열 리스트
print(subway)
print(subway.index("Choi")) #위치 찾기, 이것도 0,1,2번째 임을 주의
subway.append("Ha") #맨 뒤에 넣기
print(subway)
subway.insert(1, "Jung") #중간에 넣기
print(subway)
print(subway.pop()) #맨 뒤 빼기
print(subway)
subway.append("You")
print(subway)
print(subway.count("You")) #같은 문자열이 몇개인지 확인하기
num_list = [5,2,4,3,1]
num_list.sort() #순서대로 정렬 기능
print(num_list)
num_list.reverse() #순서 뒤집기도 가능
print(num_list)
mix_list = ["Choi", 20, True]
mix_list.extend(num_list) #리스트 확장
print(mix_list)

#리스트 공부2(사전, 중괄호와 콜론)
#사전은 키와 벨류 형태로 저장됨.
#키를 입력하면 벨류가 나오고, 키는 중복이 안됨.
cabinet = {3:"You", 100:"Kim"}
#벨류를 부르는 방법
print(cabinet[3])
print(cabinet.get(3))
#print(cabinet[5]) #없는 값을 부르면 멈춤.
print(cabinet.get(5)) #없으면 없다고 출력됨.
print(cabinet.get(5, "사용 가능")) #없을때 원하는 출력도 가능함.
print(3 in cabinet) #있는지 없는지 불린형태로 나옴.
cabinet[20] = "Choi" #추가 가능.
print(cabinet)
cabinet[3] = "Sparta" #기존 값 변경 가능.
print(cabinet)
del cabinet[3] #삭제 가능.
print(cabinet)
print(cabinet.keys()) #키만 출력
print(cabinet.values()) #벨류만 출력
print(cabinet.items()) #전체 다 출력
cabinet.clear() #전체 삭제
print(cabinet)

#리스트 공부3(세트, 중괄호)
#중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)
java = {"You", "Kim", "Yang"} #기본적인 세트 선언법
python = set(["You", "Park"]) #세트 선언법2
print(java & python) #and문 사용해서 교집합 출력.
print(java.intersection(python)) #교집합 함수형태
print(java | python) #or문 사용해서 합집합 출력.
print(java.union(python)) #합집합 함수형태
print(java - python) #차집합
print(java.difference(python)) #차집합 함수형태
python.add("Kim") #항목 추가
print(python)
java.remove("Kim") #항목 제거
print(java)

#리스트 공부4(튜플, 소괄호)
#튜플은 변경이 불가능하나 속도가 빠름.
menu = ("Don", "Chi")
print(menu[0])

#리스트 공부5(자료구조의 변경)
menu = {"coffee", "milk", "juice"} #세트임
print(menu, type(menu))
menu = list(menu) #리스트로 변경
print(menu, type(menu))
menu = tuple(menu) #튜플로 변경
print(menu, type(menu))
menu = set(menu) #세트로 변경
print(menu, type(menu))

#Quiz 풀이
from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#lst = range(1,21) 이라고 치면 됨.
#단, type이 range라서 lst = list(lst) 해주면 됨.
winners = sample(lst,4)
chicken = winners[0]
winners.remove(chicken)
coffee = winners
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken))
print("커피 당첨자 : {0}".format(coffee))
print(" -- 축하합니다 --")




