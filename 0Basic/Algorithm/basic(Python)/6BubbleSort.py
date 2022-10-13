import random

class Solution :
    def solution(self) :
        keys = ["1st", "2nd", "3rd", "4th", "5th"]
        dc = {}
        for i in keys : 
            dc[i] = random.randint(1,100)

        print(f" ### Create 5 Random Numbers ### ")
        print(f"*"*30)

        for k,v in dc.items() : 
            print(f"{k} : {v}")

        print(f"*"*30)

if __name__ == "__main__" : #리턴 없이 간소화된 버전
    solution = Solution()
    solution.solution() #리턴 지우고 프린트만 지우면 됨.















