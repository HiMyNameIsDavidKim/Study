import cv2
from PIL import Image


def ExecuteLambda(*params):
    cmd = params[0]
    target = params[1]
    if cmd == 'IMAGE_READ':
        return (lambda x: cv2.imread('./data/' + x, cv2.IMREAD_COLOR))(target)
    elif cmd == 'GRAY_SCALE':
        return (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(target)
    elif cmd == 'ARRAY_TO_IMAGE':
        return (lambda x: (Image.fromarray(x)))(target)
    elif cmd == '':
        pass