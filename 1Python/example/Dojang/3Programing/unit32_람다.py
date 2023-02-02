if __name__ == '__main__':
    files = input().split()
    print(list(map(lambda x: x[:x.index('.')].zfill(3) + x[x.index('.'):], files)))



'''
점 앞에까지 끊고
숫자 3개로 만들고
다시 조합
'''