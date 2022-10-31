import cv2

from lena.models import LenaModel
from util.dataset import Dataset


class LenaController(object):

    dataset = Dataset()
    model = LenaModel()

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