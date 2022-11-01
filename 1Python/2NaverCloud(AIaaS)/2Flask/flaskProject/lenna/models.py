from io import BytesIO
import cv2
import numpy as np
import requests
from PIL import Image
import matplotlib.pyplot as plt

from util.dataset import Dataset


class LennaModel(object):

    dataset = Dataset()

    def __init__(self):
        headers = {'User-Agent': 'My User Agent 1.0'}
        res = requests.get('https://upload.wikimedia.org/wikipedia/ko/2/24/Lenna.png', headers=headers)
        lenna = Image.open(BytesIO(res.content))
        self.lenna = np.array(lenna)
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

    def canny(self, src):
        src = self.gaussian_filter(src)
        src = self.calc_gradiant(src)
        src = self.non_maximum_suppression(src)
        src = self.edge_tracking(src)

    def calc_gradiant(self):
        pass

    def non_maximum_suppression(self):
        pass

    def edge_tracking(self):
        pass


class GaussianBlur(object):
    def __init__(self, src, sigmax, sigmay):
        self.src = src
        self.sigmax = sigmax
        self.sigmay = sigmay
        # 가로 커널과 세로 커널 행렬을 생성
        i = np.arange(-4 * sigmax, 4 * sigmax + 1)
        j = np.arange(-4 * sigmay, 4 * sigmay + 1)
        # 가우시안 계산
        mask = np.exp(-(i ** 2 / (2 * sigmax ** 2))) / (np.sqrt(2 * np.pi) * sigmax)
        maskT = np.exp(-(j ** 2 / (2 * sigmay ** 2))) / (np.sqrt(2 * np.pi) * sigmay)
        mask = mask[:, np.newaxis]
        maskT = maskT[:, np.newaxis].T
        self.dst = self.filter2D(self.filter2D(src, mask), maskT) # 2회 필터링

    def get(self):
        return self.dst

    def filter2D(self, src, kernel, delta=0):
        # 가장자리 픽셀을 (커널의 길이 // 2) 만큼 늘리고 새로운 행렬에 저장
        halfX = kernel.shape[0] // 2
        halfY = kernel.shape[1] // 2
        cornerPixel = np.zeros((src.shape[0] + halfX * 2, src.shape[1] + halfY * 2), dtype=np.uint8)

        # (커널의 길이 // 2) 만큼 가장자리에서 안쪽(여기서는 1만큼 안쪽)에 있는 픽셀들의 값을 입력 이미지의 값으로 바꾸어 가장자리에 0을 추가한 효과를 봄
        cornerPixel[halfX:cornerPixel.shape[0] - halfX, halfY:cornerPixel.shape[1] - halfY] = src

        dst = np.zeros((src.shape[0], src.shape[1]), dtype=np.float64)

        for y in np.arange(src.shape[1]):
            for x in np.arange(src.shape[0]):
                # 필터링 연산
                dst[x, y] = (kernel * cornerPixel[x: x + kernel.shape[0], y: y + kernel.shape[1]]).sum() + delta
        return dst


if __name__ == '__main__':
    lm = LennaModel()
    img = lm.grayscale(lm.lenna)
    lm.imshow(img)