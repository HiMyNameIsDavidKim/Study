from datetime import *

class Person(object):
    def __init__(self, name, pnum, addr):
        self.name = name
        self.pnum = pnum
        self.addr = addr
        self.age = self.get_age()
        self.gender = self.get_gender()

    def __str__(self):
        return f"{self.name}, {self.pnum}, {self.addr}, {self.age}, {self.gender}"

    def get_age(self):
        pnum = self.pnum
        if int(pnum[0:2]) < datetime.today().year-1999:
            age = datetime.today().year-1999-int(pnum[0:2])
        elif int(pnum[0:2]) >= datetime.today().year-1999:
            age = 100-int(pnum[0:2])+datetime.today().year-1999
        return age

    def get_gender(self):
        pnum = self.pnum
        if (int(pnum[7]) == 1) or (int(pnum[7]) == 3): gender = "Male"
        elif (int(pnum[7]) == 2) or (int(pnum[7]) == 4): gender = "Female"
        return gender

    @staticmethod
    def new_intro():
        name = input("Please type your name : ")
        pnum = input("Please type your Personal Number : ")
        addr = input("Please type your address : ")
        return Person(name, pnum, addr)