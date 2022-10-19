import random
# 중복 없는 랜덤 : random.sample(range(1,11),5)
# 중복 있는 랜덤 : random.choices(range(1,11),k=5)

class Bubble(object):
    def __init__(self):
        pass

    def ext_rand(self):
        return random.sample(range(1,101),10)

    def print(self):
        for i in self.ext_rand():
            if i % 2 == 0 : print(i)
            elif i % 2 != 0 : 

    @staticmethod
    def main():
        bubble = Bubble()
        bubble.print()

Bubble.main()