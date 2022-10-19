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
    def __init__(self,req):
        self.req = req
        pass

    def print(self):
        r1 = RandomList()
        my_list = r1.get_rand(10,100,10)
        for i in my_list:
            if i % int(self.req) == 0: print(i)
            else: pass
        pass

    @staticmethod
    def main():
        req = input("Please input number : ")
        searchnum = Search_num(req)
        searchnum.print()

Search_num.main()