"""
 * 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램
    * [요구사항] 금융업을 하는 고객사로부터 프로그램 개발요청이 들어왔습니다.
    * 금액을 입력받은 후 우리나라 화폐종류별로 해당 갯수를 표기하는 프로그램입니다.
    * 예를들어, 125,520 원을 입력하면 화면에 이렇게 보이게 하면 됩니다.
    * 표시하고 10원미만은 절삭
      ******************************************************
         요청금액 : 126520 원
         5만원 : 2매
         1만원 : 2매
         5천원 : 1매
         1천원 : 1매
         5백원 : 1개
         백원 : 0개
         오십원 : 0개
         십원 : 2개
      ********************************************************
"""

class Solution :
    def solution(self, money) :
        title = " ### Money Changer ### "
        aster = "*"*30
        answer = f"요청금액 : {money:,} 원"
        return f"{title}\n{aster}\n{answer}\n{aster}"

if __name__ == "__main__" :
    solution = Solution()
    money = int(input("Please input money : "))
    print(solution.solution(money))









