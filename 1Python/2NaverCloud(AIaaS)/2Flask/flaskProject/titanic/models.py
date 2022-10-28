import numpy as np
import pandas as pd
from util.dataset import Dataset

"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

시각화를 통해 얻은 상관관계 변수(variable = feature = column)
Pclass
Sex
Age
Fare
Embarked

[Null Memo]
Age 177ea
Cabin 687ea
Embarked 2ea
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
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature) -> object: # 자료구조 객체를 '*'으로 표시한다.
        for i in feature:
            this.train = this.train.drop(i, axis=1)
            this.test = this.test.drop(i, axis=1)
        return this

    @staticmethod
    def pclass_ordinal(this) -> object: # 등급 1, 2, 3
        train = this.train
        test = this.test
        return this

    @staticmethod
    def sex_nominal(this) -> object: # female, male
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({"male": 0, "female": 1})
        return this

    @staticmethod
    def age_ordinal(this) -> object: # 10대, 20대, 30대
        for i in [this.train, this.test]:
            i['Age'] = i['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 68, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in [this.train, this.test]:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def fare_ordinal(this) -> object: # 4등분, qcut 사용
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels=[1, 2, 3, 4])
        return this

    @staticmethod
    def embarked_nominal(this) -> object: # 승선점 S, C, Q
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].fillna('S')
            i['Embarked'] = i['Embarked'].map({"S": 1, "C": 2, "Q": 3})
        return this

if __name__ == '__main__': # 테스트용
    pass