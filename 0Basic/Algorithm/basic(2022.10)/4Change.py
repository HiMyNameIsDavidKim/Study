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

# #Greedy 개념을 반영하지 않은 코드
# class Solution :
#     def solution(self, money) :
#         title = " ### Money Changer ### "
#         aster = "*"*30
#         answer = f"요청금액 : {money:,} 원"
#         answer2 = int(money / 50000) #몫만 구함.
#         answer3 = int(money % 50000 / 10000) #50k으로 나눈 나머지를 10k로 나눠 몫만 구함.
#         answer4 = int(money % 10000 / 5000) #이때 각 윗화폐는 아랫화폐의 배수라서 가능한거임.
#         answer5 = int(money % 5000 / 1000)
#         answer6 = int(money % 1000 / 500)
#         answer7 = int(money % 500 / 100)
#         answer8 = int(money % 100 / 50)
#         answer9 = int(money % 50 / 10)
#         result = (
#             f"{title}\n{aster}\n{answer}"
#             f"50k : {answer2}\n"
#             f"10k : {answer3}\n"
#             f"5k : {answer4}\n"
#             f"1k : {answer5}\n"
#             f"500 : {answer6}\n"
#             f"100 : {answer7}\n"
#             f"50 : {answer8}\n"
#             f"10 : {answer9}\n"
#             f"n{aster}"
#         ) #f-스트링을 괄호로 묶어서 변수로 선언할 수도 있다...ㅇㅁㅇ
#         return result

# if __name__ == "__main__" :
#     solution = Solution()
#     money = int(input("Please input money : "))
#     print(solution.solution(money))


# #Greedy 개념을 반영한 코드
# class Solution :
#     def solution(self, money) :
#         title = " ### Money Changer ### "
#         aster = "*"*30
#         answer = f"요청금액 : {money:,} 원"
#         unit = [money+1, 50000, 10000, 5000, 1000, 500, 100, 50, 10]
#         unit2 = ["5만", "1만", "5천", "1천", "5백", "백", "오십", "십"]
#         result = (
#             f"{title}\n{aster}\n{answer}"
#         )
#         for i in range(0,8) : #0~7까지 진행
#             result = result + f"\n{unit2[i]}원 : {money % unit[i] // unit[i+1]}"
#         return result

# if __name__ == "__main__" :
#     solution = Solution()
#     money = int(input("Please input money : "))
#     print(solution.solution(money))


# #더 간결한 버전
# class Solution :
#     def solution(self, money) :
#         title = " ### Money Changer ### "
#         aster = "*"*30
#         answer = f"요청금액 : {money:,} 원"
#         unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
#         count = 0
#         result = (
#             f"{title}\n{aster}\n{answer}\n"
#         )
#         for i in unit :
#             count = money // i
#             money %= i
#             result += f"{i}원 : {count}\n"
#         result += aster
#         return result

# if __name__ == "__main__" :
#     solution = Solution()
#     money = int(input("Please input money : "))
#     print(solution.solution(money))


#딕셔너리를 활용한 버전
class Solution :
    def solution(self, money) :
        title = " ### Money Changer ### "
        aster = "*"*30
        answer = f"요청금액 : {money:,} 원"
        unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
        dc = {}
        result = (
            f"{title}\n{aster}\n{answer}\n"
        )
        for i in unit :
            cnt = money // i
            dc[i] = cnt
            money %= i

        #딕셔너리의 키와 벨류를 다 뽑고 싶은 경우 사용.
        #딕셔너리를 바로 사용할 수 없음. items 써서 사용해야함.
        #딕셔너리는 아이템만 불러내고, 아이템은 키랑 벨류만 불러냄.
        for k,v in dc.items() :
            if k >= 1000 :
                result += f"{k}원 : {v}매\n"
            elif k < 1000 :
                result += f"{k}원 : {v}개\n"

        result += aster
        return result

if __name__ == "__main__" :
    solution = Solution()
    money = int(input("Please input money : "))
    print(solution.solution(money))












