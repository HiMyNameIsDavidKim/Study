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
        # 가장자리 픽셀을 (커널의 길이 // 2) 만큼 늘리고 새로운 행렬에 저장
        halfX = blocksize // 2
        halfY = blocksize // 2
        cornerPixel = np.zeros((src.shape[0] + halfX * 2, src.shape[1] + halfY * 2), dtype=np.uint8)

        # (커널의 길이 // 2) 만큼 가장자리에서 안쪽(여기서는 1만큼 안쪽)에 있는 픽셀들의 값을 입력 이미지의 값으로 바꾸어 가장자리에 0을 추가한 효과를 봄
        cornerPixel[halfX:cornerPixel.shape[0] - halfX, halfY:cornerPixel.shape[1] - halfY] = src

        dst = np.zeros((src.shape[0], src.shape[1]), dtype=np.float64)

        for y in np.arange(src.shape[1]):
            for x in np.arange(src.shape[0]):
                # 필터링 연산
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
        # 가로 커널과 세로 커널 행렬을 생성
        i = np.arange(-4 * sigmax, 4 * sigmax + 1)
        j = np.arange(-4 * sigmay, 4 * sigmay + 1)
        # 가우시안 계산
        mask = np.exp(-(i ** 2 / (2 * sigmax ** 2))) / (np.sqrt(2 * np.pi) * sigmax)
        maskT = np.exp(-(j ** 2 / (2 * sigmay ** 2))) / (np.sqrt(2 * np.pi) * sigmay)
        mask = mask[:, np.newaxis]
        maskT = maskT[:, np.newaxis].T
        return filter2D(filter2D(src, mask), maskT) # 2회 필터링

class Canny(object):
    def __init__(self, src, lowThreshold, highThreshold):
        self.src = src
        self.lowThreshold = lowThreshold
        self.highThreshold = highThreshold

    def get(self):
        src = self.src
        lowThreshold = self.lowThreshold
        highThreshold = self.highThreshold

        Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # x축 소벨 행렬로 미분
        Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # y축 소벨 행렬로 미분
        Ix = filter2D(src, Kx)
        Iy = filter2D(src, Ky)
        G = np.hypot(Ix, Iy)  # 피타고라스 빗변 구하기
        img = G / G.max() * 255  # 엣지를 그레이스케일로 표현
        D = np.arctan2(Iy, Ix)  # 아크탄젠트 이용해서 그래디언트를 구함

        M, N = img.shape
        Z = np.zeros((M, N), dtype=np.int32)  # 이미지 크기만큼의 행렬을 생성
        angle = D * 180. / np.pi  # 라디안을 degree로 변환(정확하지 않음)
        angle[angle < 0] += 180  # 음수일 때 180을 더함

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

                    if (img[i, j] >= q) and (img[i, j] >= r):  # 주변 픽셀(q, r)보다 크면 static 행렬의 값을 그대로 사용
                        Z[i, j] = img[i, j]
                    else:  # 그렇지 않을 경우 0을 사용
                        Z[i, j] = 0

                except IndexError as e:  # 인덱싱 예외 발생 시 pass
                    pass

        M, N = img.shape
        res = np.zeros((M, N), dtype=np.int32)

        weak = np.int32(25)  # 약한 에지
        strong = np.int32(255)  # 강한 에지

        # 이중 임곗값 비교

        # 최대 임곗값보다 큰 원소의 인덱스를 저장
        strong_i, strong_j = np.where(img >= highThreshold)
        # 최소 임곗값보다 작은 원소의 인덱스를 저장
        zeros_i, zeros_j = np.where(img < lowThreshold)

        # 최소 임곗값과 최대 임곗값 사이에 있는 원소의 인덱스를 저장
        weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

        # 각각 강한 에지와 약한 에지의 값으로 저장
        res[strong_i, strong_j] = strong
        res[weak_i, weak_j] = weak

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if (img[i, j] == weak):
                    try:
                        if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong)
                                or (img[i, j - 1] == strong) or (img[i, j + 1] == strong)
                                or (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (
                                        img[i - 1, j + 1] == strong)):  # 강한 에지와 연결 되어있을 때
                            img[i, j] = strong  # 연결되어 있는 에지 또한 강한 에지가 됨
                        else:  # 연결되어 있지 않을 때
                            img[i, j] = 0  # 에지가 없는 0으로 설정
                    except IndexError as e:
                        pass
        return img

def filter2D(src, kernel, delta=0):
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

def imshow(img):
    img = Image.fromarray(img)
    plt.imshow(img)
    plt.show()

def gray_scale(img):
    dst = img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.229  # GRAYSCALE 변환 공식
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