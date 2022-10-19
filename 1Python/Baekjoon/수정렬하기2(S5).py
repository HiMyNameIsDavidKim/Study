def solution(n):
    my_list = []
    for i in range(0,n):
        str = int(input())
        my_list.append(str)
    my_list = sorted(my_list)
    for p in my_list:
        print(p)

if __name__ == "__main__":
    n = int(input())
    solution(n)