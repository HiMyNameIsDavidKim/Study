from matplotlib import pyplot as plt
from PIL import Image
from canny_funtional.services import ImageToNumberArray, image_read, Hough_Line, Haar_Line, GaussianBlur, Canny, \
    ExecuteLambda
import cv2
import numpy as np

from util.dataset import Dataset

ds = Dataset()
ds.context = './data/'

class MenuController(object):

    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = ExecuteLambda('IMAGE_READ', params[1])
        print(f' Shape is {img.shape}')
        cv2.imshow('Original', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    @staticmethod
    def menu_2(*params):
        print(params[0])
        src = ImageToNumberArray(params[1])
        src = ExecuteLambda('GRAY_SCALE', src)
        plt.imshow(src)
        plt.show()

    @staticmethod
    def menu_3(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        print(f'img type : {type(img)}')
        edges = cv2.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        edges, dst = Hough_Line(img)
        plt.subplot(121), plt.imshow(edges, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):
        print(params[0])
        girl = ExecuteLambda('IMAGE_READ', params[2])
        gray = cv2.cvtColor(girl, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(np.array(girl), 50, 40)
        edgess, dst = Hough_Line(girl)
        dst2 = Haar_Line(girl)
        plt.subplot(321), plt.imshow(girl, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(322), plt.imshow(gray, cmap='gray')
        plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(323), plt.imshow(edges, cmap='gray')
        plt.title('Edges Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(324), plt.imshow(dst, cmap='gray')
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(325), plt.imshow(dst2, cmap='gray')
        plt.title('Haar Image'), plt.xticks([]), plt.yticks([])
        plt.show()
        # # 여기서부터 얼굴 인식
        # haar = cv2.CascadeClassifier(ds.context+params[1])
        # girl = cv2.imread(ds.context+'girl.jpg')
        # face = haar.detectMultiScale(girl, minSize=(150, 150))
        # if len(face) == 0:
        #     print('얼굴인식 실패')
        #     quit()
        # for(x, y, w, h) in face:
        #     print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        #     red = (0, 0, 255)
        #     cv2.rectangle(girl, (x, y), (x+w, y+h), red, thickness=20)
        # girl = cv2.resize(girl, (300, 300))
        # cv2.imwrite(ds.context+'girl-face.png', girl)
        # cv2.imshow('GIRL FACE', girl)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # cv2.waitKey(1)