import cv2 as cv
from PIL import Image

from src.cmm.const.path import CTX

def MosaicLambda(*params):
    cmd = params[0]
    target = params[1] # girl.jpg
    if cmd == 'IMAGE_READ_FOR_CV':
        return (lambda x: cv.imread(CTX+x))(target)
    elif cmd == 'IMAGE_READ_FOR_PLT':
        return cv.cvtColor((lambda x: cv.imread(CTX+x))(target), cv.COLOR_BGR2RGB)
    elif cmd == 'GRAY_SCALE': # GRAYSCALE 변환 공식
        return (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(target)
    elif cmd == 'IMAGE_FROM_ARRAY':
        return (lambda x: Image.fromarray(x))(target)