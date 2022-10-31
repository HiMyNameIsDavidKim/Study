from io import BytesIO
import cv2
import numpy as np
import requests
from PIL import Image
import matplotlib.pyplot as plt

from util.dataset import Dataset


class LenaModel(object):

    dataset = Dataset()

    def __init__(self):
        headers = {'User-Agent': 'My User Agent 1.0'}
        res = requests.get('https://upload.wikimedia.org/wikipedia/ko/2/24/Lenna.png', headers=headers)
        lena = Image.open(BytesIO(res.content))
        self.lena = np.array(lena)
        self.createOption()

    def __str__(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return cv2.imread(this.context + this.fname, cv2.IMREAD_COLOR)

    def createOption(self):
        self.ADAPTIVE_THRESH_MEAN_C = 0
        self.ADAPTIVE_THRESH_GAUSSIAN_C = 1
        self.THRESH_BINARY = 2
        self.THRESH_BINARY_INV = 3

    def imshow(self, img):
        img = Image.fromarray(img)
        plt.imshow(img)
        plt.show()

    def grayscale(self, img):
        dst = img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.229
        return dst

if __name__ == '__main__':
    lm = LenaModel()
    img = lm.grayscale(lm.lena)
    lm.imshow(img)