x = int(input())
y = input()

print(x-3000) if y == 'Cash3000' else print(x-5000) if y == 'Cash5000' else print('input Error')