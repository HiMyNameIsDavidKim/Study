"""
두자리 정수 랜덤숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 개발하시오.
ex) [12, 23, 48,...,]
사용자 input = 12인 경우
출력값이 12, 48만 되도록 한다.
"""
from random_list import RandomList

class Search_num(object):
    def __init__(self,input_num):
        self.input_num = input_num

    def print(self):
        r1 = RandomList()
        my_list = r1.get_rand(10,100,10)
        print(my_list)
        for i in my_list:
            if i % self.input_num == 0: print(i)
            else: pass

    @staticmethod
    def main():
        input_num = int(input("Please input number : "))
        searchnum = Search_num(input_num)
        searchnum.print()

Search_num.main()