class TimeIterator():
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            now = self.start
            self.start += 1
            return now
        else: raise StopIteration

    def __getitem__(self, index):
        start = self.start
        stop = self.stop
        if start+index-1 < stop:
            return start+index-1
        else:
            raise IndexError


if __name__ == '__main__':
    start, stop, index = map(int, input().split())
    [print(i) for i in TimeIterator(start, stop)]
    print('\n', TimeIterator(start,stop)[index], sep='')