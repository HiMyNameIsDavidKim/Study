import math

class Point2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


if __name__ == '__main__':
    length = 0.0
    p = [Point2D(), Point2D(), Point2D(), Point2D()]
    p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

    for i in range(len(p)-1):
        if i == len(p)-1: sub_length = math.sqrt((p[0].x-p[i].x)**2+(p[0].x-p[i].x)**2)
        else : sub_length = math.sqrt((p[i+1].x-p[i].x)**2+(p[i+1].x-p[i].x)**2)
        length += sub_length

    print(length)