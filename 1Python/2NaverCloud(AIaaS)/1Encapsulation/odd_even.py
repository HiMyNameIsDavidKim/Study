from random_list import RandomList

class Odd_even(object):
    def __init__(self,input_num):
        self.input_num = input_num

    def print(self):
        r1 = RandomList()
        print(r1.get_rand(10,100,10))
        for i in r1.get_rand(10,100,10):
            if i % 2 == 0: print(f"even : {i}")
            else: print(f"odd : {i}")

        print([f"even : {i}" if i % 2 == 0 else f"odd : {i}" for i in r1.get_rand(10,100,10)])

    @staticmethod
    def main():
        input_num = int(input("Please input number : "))
        oe = Odd_even(input_num)
        oe.print()

Odd_even.main()