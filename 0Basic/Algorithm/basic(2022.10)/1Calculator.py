#전문가 코드의 기본 형태.
#헬로월드를 찍더라도 이 형태로 코딩하는 연습이 필요함.
class Solution :
    def solution(self) :
        answer = "Hello world!"
        return answer

if __name__ == "__main__" :
    solution = Solution()
    print(solution.solution())


#헷갈리면 안됨 Solution은 클래스 / solution()은 메서드(=함수) / solution은 인스턴스
#마지막줄은 인스턴스의 메서드를 호출하겠다는 거임.
class Solution :
    def solution(self, a, b, c) :
        if b == "+" :
            answer = a + c
        elif b == "-" :
            answer = a - c
        elif b == "*" :
            answer = a * c
        elif b == "/" :
            answer = a / c
        elif b == "%" :
            answer = a % c
        else :
            answer = "Wrong input."
        return answer

if __name__ == "__main__" :
    solution = Solution()
    a = int(input("First number : "))
    b = input("+, -, *, /, % : ")
    c = int(input("Second number : "))
    print(solution.solution(a, b, c))



























