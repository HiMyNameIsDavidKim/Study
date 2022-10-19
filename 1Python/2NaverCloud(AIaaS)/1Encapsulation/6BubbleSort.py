import random
# 중복 없는 랜덤 : random.sample(range(1,11),5)
# 중복 있는 랜덤 : random.choices(range(1,11),k=5)

class Bubble(object):
    def __init__(self):
        pass
    def process(self):
        self.print_()
        pass
    def ext_rand(self):
        return random.sample(range(1,11),1)[0]
    def print_(self):
        print(self.ext_rand())
        pass

    @staticmethod
    def main():
        bubble = Bubble()
        bubble.process()

Bubble.main()