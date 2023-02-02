class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.result = None

    def is_time_valid(self): #문자열이 시간인지 검사
        h = self.hour
        m = self.minute
        s = self.second
        if (h < 25) and (m < 60) and (s < 61):
            self.result = True
        else:
            self.result = False
        return self.result


if __name__ == '__main__':
    time_string = input('Please input time. : ')
    h, m, s = map(int, time_string.split(':'))
    time = Time(h, m, s)
    if time.is_time_valid():
        print(time.hour, time.minute, time.second)
    else:
        print('This is not time type.')