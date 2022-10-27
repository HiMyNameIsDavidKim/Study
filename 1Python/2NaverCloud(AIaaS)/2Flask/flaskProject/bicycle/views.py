from bicycle.models import BicycleModel
from util.dataset import Dataset

class BicycleController(object):

    dataset = Dataset()
    model = BicycleModel()

    def __init__(self):
        pass
    def __str__(self):
        return f""

    def preprocess(self) -> object:
        pass

    def modeling(self) -> object:
        self.preprocess()

    def learning(self):
        pass

    def submit(self):
        pass