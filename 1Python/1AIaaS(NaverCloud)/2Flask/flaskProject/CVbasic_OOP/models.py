from io import BytesIO
import cv2
import numpy as np
import requests
from PIL import Image
import matplotlib.pyplot as plt

from util.dataset import Dataset

def CannyModel(img):
    headers = {'User-Agent': 'My User Agent 1.0'}
    res = requests.get(img, headers=headers)
    return np.array(Image.open(BytesIO(res.content)))


class LennaModel(object):

    dataset = Dataset()

    def __init__(self):
        self.ADAPTIVE_THRESH_MEAN_C = 0
        self.ADAPTIVE_THRESH_GAUSSIAN_C = 1
        self.THRESH_BINARY = 2
        self.THRESH_BINARY_INV = 3
        headers = {'User-Agent': 'My User Agent 1.0'}
        res = requests.get('https://upload.wikimedia.org/wikipedia/ko/2/24/Lenna.png', headers=headers)

    def get(self):
        return np.array((self.lenna))

    def new_model(self, fname) -> object:
        this = self.dataset
        this.fname = fname
        return cv2.imread('./data/' + this.fname, cv2.IMREAD_COLOR)

    def new_messi_model(self, url) -> object:
        headers = {'User-Agent': 'My User Agent 1.0'}
        res2 = requests.get(url, headers=headers)
        return np.array(Image.open(BytesIO(res2.content)))

    def messi(self, url) -> object:
        return cv2.Canny(self.new_messi_model(url), 100, 200)

    def messi_show(self, url):
        plt.subplot(121), plt.imshow(self.new_messi_model(url), cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(self.messi(url), cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    def grayscale(self, url):
        plt.imshow(self.new_messi_model(url), cmap='gray')
        plt.show()

    def canny(self, src):
        src = self.gaussian_filter(src)
        src = self.calc_gradiant(src)
        src = self.non_maximum_suppression(src)
        src = self.edge_tracking(src)

    def calc_gradiant(self):
        pass

    def non_maximum_suppression(self):
        pass

    def edge_tracking(self, src, adaptiveMethod, thresholdType, blocksize, C):
        mask = np.zeros((blocksize, blocksize))
        if adaptiveMethod == self.ADAPTIVE_THRESH_MEAN_C:
            pass
        elif adaptiveMethod == self.ADAPTIVE_THRESH_GAUSSIAN_C:
            sigma = (blocksize - 1) / 8
            i = np.arange(-(blocksize // 2), (blocksize // 2) + 1)
            j = np.arange(-(blocksize // 2), (blocksize // 2) + 1)
            i, j = np.meshgrid(i, j)
            mask = np.exp(-((i ** 2 / (2 * sigma ** 2)) + (j ** 2 / (2 * sigma ** 2)))) / (2 * np.pi * sigma * sigma)
        else:
            return -1
        # ???????????? ????????? (????????? ?????? // 2) ?????? ????????? ????????? ????????? ??????
        halfX = blocksize // 2
        halfY = blocksize // 2
        cornerPixel = np.zeros((src.shape[0] + halfX * 2, src.shape[1] + halfY * 2), dtype=np.uint8)

        # (????????? ?????? // 2) ?????? ?????????????????? ??????(???????????? 1?????? ??????)??? ?????? ???????????? ?????? ?????? ???????????? ????????? ????????? ??????????????? 0??? ????????? ????????? ???
        cornerPixel[halfX:cornerPixel.shape[0] - halfX, halfY:cornerPixel.shape[1] - halfY] = src

        dst = np.zeros((src.shape[0], src.shape[1]), dtype=np.float64)

        for y in np.arange(src.shape[1]):
            for x in np.arange(src.shape[0]):
                # ????????? ??????
                threshold = 0
                if adaptiveMethod == self.ADAPTIVE_THRESH_MEAN_C:
                    threshold = cornerPixel[x: x + mask.shape[0], y: y + mask.shape[1]].mean() - C

                elif adaptiveMethod == self.ADAPTIVE_THRESH_GAUSSIAN_C:
                    threshold = (mask * cornerPixel[x: x + mask.shape[0], y: y + mask.shape[1]]).sum() / mask.sum() - C

                if thresholdType == self.THRESH_BINARY:
                    if cornerPixel[x, y] > threshold:
                        dst[x, y] = 255
                    else:
                        dst[x, y] = 0
                elif thresholdType == self.THRESH_BINARY_INV:
                    if cornerPixel[x, y] > threshold:
                        dst[x, y] = 0
                    else:
                        dst[x, y] = 255
        return dst


class GaussianBlur(object):
    def __init__(self, src, sigmax, sigmay):
        self.src = src
        self.sigmax = sigmax
        self.sigmay = sigmay

    def get(self):
        src = self.src
        sigmax = self.sigmax
        sigmay = self.sigmay
        # ?????? ????????? ?????? ?????? ????????? ??????
        i = np.arange(-4 * sigmax, 4 * sigmax + 1)
        j = np.arange(-4 * sigmay, 4 * sigmay + 1)
        # ???????????? ??????
        mask = np.exp(-(i ** 2 / (2 * sigmax ** 2))) / (np.sqrt(2 * np.pi) * sigmax)
        maskT = np.exp(-(j ** 2 / (2 * sigmay ** 2))) / (np.sqrt(2 * np.pi) * sigmay)
        mask = mask[:, np.newaxis]
        maskT = maskT[:, np.newaxis].T
        return filter2D(filter2D(src, mask), maskT) # 2??? ?????????

class Canny(object):
    def __init__(self, src, lowThreshold, highThreshold):
        self.src = src
        self.lowThreshold = lowThreshold
        self.highThreshold = highThreshold

    def get(self):
        src = self.src
        lowThreshold = self.lowThreshold
        highThreshold = self.highThreshold

        Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # x??? ?????? ????????? ??????
        Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # y??? ?????? ????????? ??????
        Ix = filter2D(src, Kx)
        Iy = filter2D(src, Ky)
        G = np.hypot(Ix, Iy)  # ??????????????? ?????? ?????????
        img = G / G.max() * 255  # ????????? ????????????????????? ??????
        D = np.arctan2(Iy, Ix)  # ??????????????? ???????????? ?????????????????? ??????

        M, N = img.shape
        Z = np.zeros((M, N), dtype=np.int32)  # ????????? ??????????????? ????????? ??????
        angle = D * 180. / np.pi  # ???????????? degree??? ??????(???????????? ??????)
        angle[angle < 0] += 180  # ????????? ??? 180??? ??????

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                try:
                    q = 255
                    r = 255

                    # angle 0
                    if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                        q = img[i, j + 1]
                        r = img[i, j - 1]
                    # angle 45
                    elif (22.5 <= angle[i, j] < 67.5):
                        q = img[i + 1, j - 1]
                        r = img[i - 1, j + 1]
                    # angle 90
                    elif (67.5 <= angle[i, j] < 112.5):
                        q = img[i + 1, j]
                        r = img[i - 1, j]
                    # angle 135
                    elif (112.5 <= angle[i, j] < 157.5):
                        q = img[i - 1, j - 1]
                        r = img[i + 1, j + 1]

                    if (img[i, j] >= q) and (img[i, j] >= r):  # ?????? ??????(q, r)?????? ?????? static ????????? ?????? ????????? ??????
                        Z[i, j] = img[i, j]
                    else:  # ????????? ?????? ?????? 0??? ??????
                        Z[i, j] = 0

                except IndexError as e:  # ????????? ?????? ?????? ??? pass
                    pass

        M, N = img.shape
        res = np.zeros((M, N), dtype=np.int32)

        weak = np.int32(25)  # ?????? ??????
        strong = np.int32(255)  # ?????? ??????

        # ?????? ????????? ??????

        # ?????? ??????????????? ??? ????????? ???????????? ??????
        strong_i, strong_j = np.where(img >= highThreshold)
        # ?????? ??????????????? ?????? ????????? ???????????? ??????
        zeros_i, zeros_j = np.where(img < lowThreshold)

        # ?????? ???????????? ?????? ????????? ????????? ?????? ????????? ???????????? ??????
        weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

        # ?????? ?????? ????????? ?????? ????????? ????????? ??????
        res[strong_i, strong_j] = strong
        res[weak_i, weak_j] = weak

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if (img[i, j] == weak):
                    try:
                        if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong)
                                or (img[i, j - 1] == strong) or (img[i, j + 1] == strong)
                                or (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (
                                        img[i - 1, j + 1] == strong)):  # ?????? ????????? ?????? ???????????? ???
                            img[i, j] = strong  # ???????????? ?????? ?????? ?????? ?????? ????????? ???
                        else:  # ???????????? ?????? ?????? ???
                            img[i, j] = 0  # ????????? ?????? 0?????? ??????
                    except IndexError as e:
                        pass
        return img

def filter2D(src, kernel, delta=0):
    # ???????????? ????????? (????????? ?????? // 2) ?????? ????????? ????????? ????????? ??????
    halfX = kernel.shape[0] // 2
    halfY = kernel.shape[1] // 2
    cornerPixel = np.zeros((src.shape[0] + halfX * 2, src.shape[1] + halfY * 2), dtype=np.uint8)

    # (????????? ?????? // 2) ?????? ?????????????????? ??????(???????????? 1?????? ??????)??? ?????? ???????????? ?????? ?????? ???????????? ????????? ????????? ??????????????? 0??? ????????? ????????? ???
    cornerPixel[halfX:cornerPixel.shape[0] - halfX, halfY:cornerPixel.shape[1] - halfY] = src

    dst = np.zeros((src.shape[0], src.shape[1]), dtype=np.float64)

    for y in np.arange(src.shape[1]):
        for x in np.arange(src.shape[0]):
            # ????????? ??????
            dst[x, y] = (kernel * cornerPixel[x: x + kernel.shape[0], y: y + kernel.shape[1]]).sum() + delta
    return dst

def imshow(img):
    img = Image.fromarray(img)
    plt.imshow(img)
    plt.show()

def gray_scale(img):
    dst = img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.229  # GRAYSCALE ?????? ??????
    return dst

if __name__ == '__main__':
    '''
    lm = LennaModel()
    static = grayscale(lm.get())
    static = GaussianBlur(static, 1, 1).get()
    static = Canny(static, 50, 150).get()
    imshow(static)
    '''
    # LennaModel().messi_show(LennaModel().messi())
    # https://docs.opencv.org/4.x/roi.jpg