#클래스 공부1(기본)
#스타크래프트 예시
from pickle import FALSE

name = "Marin"
hp = 40
damage = 5

print("{0} Unit is created.".format(name))
print("hp : {0}, damage : {1}\n".format(hp,damage))

tank_name = "Tank"
tank_hp = 150
tank_damage = 35

print("{0} Unit is created.".format(tank_name))
print("hp : {0}, damage : {1}\n".format(tank_hp,tank_damage))

def attack(name, location, damage) : 
    print("{0} attack enermy to {1} directon. [damage {2}]".format(name, location, damage))

attack(name, "1 o'clock", damage)
attack(tank_name, "1 o'clock", tank_damage) #유닛이 수십 수백개 라면 계속 이렇게 쓸텐가?
#클래스는 붕어빵틀처럼 형식이 있고, 재료를 넣으면 계속 찍어내줌.
class Unit : #유닛이라는 클래스를 만들었음.
    def __init__(self, name, hp, speed) : #기본적으로 이닛이라는 함수(=메서드)를 정의해야함. 이걸로 필요한 값들을 정의함.
        self.hp = hp
        self.name = name #위에서 전달받은 값을 self.name에 저장하는 과정.
        self.speed = speed
        print("{0} unit is created.".format(self.name))

    def move(self, location) : 
        print("[normal unit move]")
        print("{0} : is move to {1} direction. [speed {2}]".format(self.name, location, self.speed))

marine1 = Unit("Marin", 40, 1)
marine2 = Unit("Marin", 40, 1)
tank1 = Unit("Tank", 150, 1)


#클래스 공부2(__init__)
#그렇다면 init의 역할은 무엇인가?
#init은 생성자라고 하는 것.
#객체를 만들 때는 이닛함수에서 셀프를 제외한 것을 다 정의해야 만들 수 있음.
#클래스(class) : 객체를 만들어 내기 위한 설계도 or 틀. 연관 변수와 메서드의 집합체.
#객체(Object) : SW 세계에 구현할 대상. 클래스에 의해 선언된 모양대로 생성된 실체.
#인스턴스(Instance) : 설계도를 바탕으로 SW 세계에 구현된 실체. 객체를 실체화 하면 그것을 인스턴스라고 부름.
#객체는 '클래스의 인스턴스' 이다.


#클래스 공부3(멤버변수)
#클래스 내에서 정의된 변수.
#위 예시에서 name hp damage 3개가 멤버변수임.
#정의한 객체의 이름에 점을 붙여서 멤버변수에 접근할 수 있음.
wraith1 = Unit("Wraith", 80, 1)
print("Unit name = {0}.".format(wraith1.name))

wraith2 = Unit("Graped Wraith", 80, 1)
wraith2.clocking = True

#외부에서도 객체에 필요한 멤버변수를 추가로 만들어서 쓸 수 있음. (=확장할 수 있다.)
#특이하게도 외부에서 확장한 경우에는 특정 객체는 있고 특정 객체는 없는 것도 가능함.
if wraith2.clocking == True :
    print("{0} is in clocking state now.".format(wraith2.name))


#클래스 공부4(메서드)
#공격 유닛을 만들어보자.
class AttackUnit : 
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} unit is created.".format(self.name))
        print("hp : {0}, damage : {1}\n".format(self.hp,self.damage))    
    
    def attack(self, location) :
        print("{0} : attack enermy to {1} directon. [damage {2}]".format(self.name, location, self.damage))

    def damaged(self, damage) : 
        print("{0} : have damaged. [damaged {1}]".format(self.name, damage))
        self.hp -= damage
        print("{0} : now hp is {1}.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : is destroyed.".format(self.name))

firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("5 o'clock")
firebat1.damaged(25)
firebat1.damaged(25)


#클래스 공부5(상속)
#Unit클래스랑 AttackUnit클래스를 보면 name이랑 hp가 동일함.
#이런 경우에 상속을 사용할 수 있음. 말그대로 물려받는 것을 의미함.
#이런경우에 Unit같은 애들을 부모클래스, AttackUnit같은 애들을 자식클래스라고 부름.
class Unit :
    def __init__(self, name, speed, hp) :
        self.hp = hp
        self.name = name
        self.speed = speed
        print("{0} unit is created.".format(self.name))

    def move(self, location) : 
        print("[normal unit move]")
        print("{0} : is move to {1} direction. [speed {2}]".format(self.name, location, self.speed))

    def damaged(self, damage) : 
        print("{0} : have damaged. [damaged {1}]".format(self.name, damage))
        self.hp -= damage
        print("{0} : now hp is {1}.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : is destroyed.".format(self.name))

class AttackUnit(Unit) : #괄호에 상속해줄 클래스 넣기. 
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, speed, hp) #정의하는 과정에서 상속 받겠다는 것을 표현함.
        self.damage = damage
        print("{0} unit is created.".format(self.name))
        print("hp : {0}, damage : {1}\n".format(self.hp,self.damage))    
    
    def attack(self, location) :
        print("{0} : attack enermy to {1} directon. [damage {2}]".format(self.name, location, self.damage))

    def damaged(self, damage) : 
        print("{0} : have damaged. [damaged {1}]".format(self.name, damage))
        self.hp -= damage
        print("{0} : now hp is {1}.".format(self.name, self.hp))
        if self.hp <= 0 :
            print("{0} : is destroyed.".format(self.name))

firebat1 = AttackUnit("Firebat", 50, 1, 16)
firebat1.attack("5 o'clock")
firebat1.damaged(25)
firebat1.damaged(25)


#클래스 공부6(다중 상속)
class Flyable :
    def __init__(self, flying_speed) : 
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : fly to {1} direction. [speed {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable) : #콤마로 넣으면 됨.
    def __init__(self, name, hp, damage, flying_speed) : 
        AttackUnit.__init__(self, name, hp, 0, damage) #부모클래스 쩜 이닛에서 가져와서 이닛해준다.
        Flyable.__init__(self, flying_speed)

    def move(self, location) :
        print("[Flyable Unit move]")
        self.fly(self.name, location)

valkyrie1 = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie1.fly(valkyrie1.name, "3 o'clock")


#클래스 공부7(메소드 오버라이딩)
vulture1 = AttackUnit("Vulture", 80, 10, 20)
battlecruiser1 = FlyableAttackUnit("Battlecruiser", 500, 25, 3)

vulture1.move("11 o'clock")
battlecruiser1.fly(battlecruiser1.name, "9 o'clock")
#지상 유닛은 무브, 공중 유닛은 플라이, 오버라이딩하면 하나로 통합시킬 수 있음.
#142~144번째 줄 새로 작성함. 함수 안에서 무브로 재정의 해주는 것.
#서로 관련없는 클래스 이지만, 유사한 함수를 이름을 같게 해줄 수 있는 거임.
battlecruiser1.move("9 o'clock")


#클래스 공부8(pass)
#아무것도 안하고 일단 넘어간다는 의미의 코드
class BuildingUnit(Unit) : 
    def __init__(self, name, hp, location) : 
        pass

supply_depot1 = BuildingUnit("Supply_depot", 500, "7 o'clock")

def game_start() : 
    print("[Alarm] New game is started now.")

def game_over() : 
    pass

game_start()
game_over() #진짜 레알 아무것도 없는데 코드 에러는 없음.


#클래스 공부9(super)
#부모클래스에서 상속받을때 사용함. 클래스 이름 몰라도 걍 가져옴.
#문제는 다중상속에서가 문제인데, 처음 상속받은 클래스 한테만 받음.
#예를 들어 FlyableUnit(Unit, Flyable)이면 Unit 한테만 받음.
class BuildingUnit(Unit) : 
    def __init__(self, name, hp, location) : 
            Unit.__init__(self, name, hp, 0)
            self.location = location

class BuildingUnit(Unit) : 
    def __init__(self, name, hp, location) : 
            super().__init__(name, hp, 0) #꼭 괄호쓰고 점 찍어야함. 셀프 안써도 됨.
            self.location = location


#클래스 공부10(예제1 스타크래프트 전반전)
class Marine(AttackUnit) : 
    def __init__(self) : 
        AttackUnit.__init__(self, "Marine", 40, 1, 5)
    
    def stimpack(self) : 
        if self.hp > 10 : 
            self.hp -= 10
            print("{0} : use stimpack. (HP decrease 10.".format(self.name))
        else :
            print("{0} : HP is not enough. Can not use stimpack".format(self.name))

class Tank(AttackUnit) :
    seize_developed = False 
    def __init__(self) : 
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_sieze_mode(self) : 
        if Tank.seize_developed == False :
            return
        if self.seize_mode == False :
            print("{0} : change to seize mode ON.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else :
            print("{0} : change to seize mode OFF.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

class Wraith(FlyableAttackUnit) :
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False
    
    def clocking(self) :
        if self.clocked == True :
            print("{0} : change to clocking mode OFF.".format(self.name))
            self.clocked = False
        else : 
            print("{0} : change to clocking mode ON.".format(self.name))
            self.clocked = True
            

#클래스 공부11(예제2 스타크래프트 후반전)
from random import *

def game_start(): 
    print("[Inform] New game is started.")

def game_over():
    print("Player : gg")
    print("[Player] get out the game.")

#실제 게임 시뮬레이션
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

#유닛들을 일괄 관리하기 위해 리스트에 추가하기.
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#유닛들을 특정 방향으로 이동시키기.
for unit in attack_units :
    unit.move("1 o'clock")

#탱크 시즈모드를 개발하기.
Tank.seize_developed = True
print("[Inform] Tank seize mode develop is completed.")

#공격 준비.
for unit in attack_units :
    if isinstance(unit, Marine) : #특정 클래스의 인스턴스인지 확인함.
        unit.stimpack()
    elif isinstance(unit, Tank) :
        unit.set_sieze_mode()
    elif isinstance(unit, Wraith) :
        unit.clocking()

#공격 명령하기.
for unit in attack_units : 
    unit.attack("1 o'clock")

#피해 입은 상황 표현하기.
for unit in attack_units : 
    unit.damaged(randint(5, 21))

#게임 종료
game_over()


#Quiz 풀이
class House :
    def __init__(self, location, house_type, deal_type, price, completion_year) : 
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self) : 
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

houses = []
h1 = House("GangNam", "Appartment", "Sell", "1B", 2010)
h2 = House("Mapo", "Officetell", "Borrow", "0.5B", 2007)
h3 = House("Songpa", "Billa", "Monthly", "500/50", 2000)
houses.append(h1)
houses.append(h2)
houses.append(h3)

print("There are {0} item now.".format(len(houses)))
for house in houses :
    house.show_detail()

















