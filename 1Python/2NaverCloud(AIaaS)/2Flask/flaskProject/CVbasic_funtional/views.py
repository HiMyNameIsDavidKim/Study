from matplotlib import pyplot as plt
from PIL import Image
from CVbasic_funtional.services import ImageToNumberArray, image_read, Hough_Line, Haar_Line, GaussianBlur, Canny, \
    Mosaic_img
import cv2
import numpy as np

from util.dataset import Dataset
from util.lambdas import ExecuteLambda

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
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        edges, dst = Hough_Line(img)
        plt.subplot(121), plt.imshow(edges, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):
        print(params[0])
        girl = ExecuteLambda('IMAGE_READ', params[2])
        girl = cv2.cvtColor(girl, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(girl, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(np.array(girl), 50, 40)
        edgess, dst = Hough_Line(girl)
        dst2, (x, y, w, h) = Haar_Line(girl)
        plt.subplot(321), plt.imshow(girl, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(322), plt.imshow(gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(323), plt.imshow(edges, cmap='gray')
        plt.title('Edges'), plt.xticks([]), plt.yticks([])
        plt.subplot(324), plt.imshow(dst, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(325), plt.imshow(dst2, cmap='gray')
        plt.title('Haar'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_6(*params):
        print(params[0])
        girl = ExecuteLambda('IMAGE_READ', params[2])
        girl = cv2.cvtColor(girl, cv2.COLOR_BGR2RGB)
        mos = Mosaic_img(girl, 10)
        plt.subplot(121), plt.imshow(girl, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(mos, cmap='gray')
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()