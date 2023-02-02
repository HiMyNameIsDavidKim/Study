kor, eng, mat, sci = map(int, input().split())
avg = (kor + eng + mat + sci)/4
if 80 <= avg < 100: print('Pass')
elif 0 <= avg < 80 : print('Fail')
else :
    print('please input score by number.')