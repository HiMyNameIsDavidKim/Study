start, stop = map(int, input().split())

for i in range(start, stop+1):
    print(('Fizz' * (i%5==0) + 'Buzz' * (i%7==0)) or i)