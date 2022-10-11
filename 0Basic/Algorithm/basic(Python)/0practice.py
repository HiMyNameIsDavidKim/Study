"""
 * 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램
    * [요구사항] 금융업을 하는 고객사로부터 프로그램 개발요청이 들어왔습니다.
    * 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램입니다.
    * 예를들어, 126,520 원을 입력하면 화면에 이렇게 보이게 하면 됩니다.
    * 표시하고 10원미만은 절삭
      ******************************************************
         요청금액 : 126520 원
         50000원 : 2매
         10000원 : 2매
         5000원 : 1매
         1000원 : 1매
         500원 : 1개
         100원 : 0개
         50원 : 0개
         10원 : 2개
      ********************************************************
"""

class Solution:
    def solution(self, money):
        aster = "*"*30
        unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
        dc = {}
        print(f" ### Money Change ### ")
        print(f"{aster}")
        print(f"Request money : {money}")
        for i in unit:
            dc[i] = money // i
            money %= i
        for k,v in dc.items():
            print(f"{k}원 : {v}매")
        print(f"{aster}")

if __name__ == "__main__":
    solution = Solution()
    money = int(input("Please input money : "))
    solution.solution(money)











