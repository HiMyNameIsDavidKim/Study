from matplotlib import pyplot as plt
from PIL import Image
from canny_funtional.services import ImageToNumberArray, GaussianBlur, Canny, image_read
import cv2
import numpy as np

class MenuController(object):
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = image_read(params[1])
        print(f' Shape is {img.shape}')
        cv2.imshow('Gray', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        arr = ImageToNumberArray(params[1])
        img = (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(arr)
        # img = Canny(GaussianBlur(img, 1, 1), 50, 150)
        plt.imshow((lambda x: (Image.fromarray(x)))(img))
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
