import cv2

from lenna.models import LennaModel
from util.dataset import Dataset


class LennaController(object):

    dataset = Dataset()
    model = LennaModel()

    def __init__(self):
        pass
    def __str__(self):
        pass

    def preprocess(self, img) -> object:
        model = self.model
        this = self.dataset
        this = model.new_model(img)
        return this

    def modeling(self, img) -> object:
        this = self.preprocess(img)
        return this