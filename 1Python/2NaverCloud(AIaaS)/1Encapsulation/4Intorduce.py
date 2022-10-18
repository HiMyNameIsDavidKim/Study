from datetime import *

class Introduce(object):
    def __init__(self,name,p_num,addr):
        self.name = name
        self.p_num = p_num
        self.addr = addr
        self.age = 0
        self.gender = ""
    
    def execute(self):
        self.read_gender()
        self.read_age()
        self.print_intro()

    def read_gender(self):
        p_num = self.p_num
        if (int(p_num[7]) == 1) or (int(p_num[7]) == 3): self.gender = "Male"
        elif (int(p_num[7]) == 2) or (int(p_num[7]) == 4): self.gender = "Female"
        return self.gender

    def read_age(self):
        p_num = self.p_num
        if int(p_num[0:2]) < datetime.today().year-1999:
            age = datetime.today().year-1999-int(p_num[0:2])
        elif int(p_num[0:2]) >= datetime.today().year-1999:
            age = 100-int(p_num[0:2])+datetime.today().year-1999
        return age

    def print_intro(self):
        title = f"### Introduce App ###"
        aster = f"*"*30
        name = self.name
        age = self.read_age()
        gender = self.read_gender()
        addr = self.addr
        print(f"{title}\n{aster}\nname : {name}\nage : {age}\ngender : {gender}\naddress : {addr}\n{aster}")

    @staticmethod
    def main():
        name = input("Please input your name : ")
        p_num = input("Please input your personal number : ")
        addr = input("Please input your address : ")
        introduce = Introduce(name, p_num, addr)
        introduce.execute()

Introduce.main()