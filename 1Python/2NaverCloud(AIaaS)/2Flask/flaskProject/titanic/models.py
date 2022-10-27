import pandas as pd
from util.dataset import Dataset

"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
# [Null Memo]
# Age 177ea
# Cabin 687ea
# Embarked 2ea
"""


class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass
    def __str__(self):
        b = self.new_model(self.dataset.fname)
        return f"Type : {type(b)}\n" \
               f"Columns : {b.columns}\n" \
               f"Head : {b.head()}\n" \
               f"Null의 개수 : {b.isnull().sum()}"

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        pass

    def create_label(self):
        pass