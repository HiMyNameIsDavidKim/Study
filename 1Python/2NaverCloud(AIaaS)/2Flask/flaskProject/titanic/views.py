from titanic.models import TitanicModel
from util.dataset import Dataset

class TitanicController(object):

    dataset = Dataset()
    model = TitanicModel()

    def __init__(self):
        pass
    def __str__(self):
        return f""

    def preprocess(self) -> object: #전처리
        pass

    def modeling(self) -> object: #모델 생성
        self.preprocess

    def learning(self): #머신러닝
        pass

    def submit(self): #제출
        pass