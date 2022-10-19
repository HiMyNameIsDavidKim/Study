import random
# 중복 없는 랜덤 : random.sample(range(1,11),5)
# 중복 있는 랜덤 : random.choices(range(1,11),k=5)

class RandomList(object):
    def __init__(self):
        pass

    def get_rand(self, start, end, count):
        return random.sample(range(start,end),count)

    def print(self):
        cnt = 0
        for i in self.get_rand(10, 100, 10):
            if i % 2 == 0:
                print(i)
                cnt += 1
            if cnt != 10: pass

    @staticmethod
    def main():
        randlist = RandomList()
        randlist.print()

RandomList.main()