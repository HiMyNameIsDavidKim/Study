from random_list import RandomList

class OddEven(object):
    def __init__(self) -> None:
        pass

    def print(self):
        r1 = RandomList()
        print(r1.get_rand(2,10,1))

    @staticmethod
    def main():
        oe = OddEven()
        oe.print()

OddEven.main()