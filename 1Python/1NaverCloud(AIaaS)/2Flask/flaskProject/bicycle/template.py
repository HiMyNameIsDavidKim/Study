from bicycle.models import BicycleModel
from util.dataset import Dataset


class Template(object):

    dataset = Dataset()
    model = BicycleModel()

    def __init__(self, fname):
        self.entry = self.model.new_model(fname)

    def __str__(self):
        return f""