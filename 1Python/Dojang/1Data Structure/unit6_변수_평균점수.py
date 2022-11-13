a = 50
b = a + 50
c = None

print(a)
print(b)
print(c)

a,b,c,d = map(int, input('4개의 수를 입력하세요 : ').split())
print(int((a+b+c+d)/4))