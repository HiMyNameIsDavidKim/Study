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
        gender_mapping = {"male":0, "female":1}
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object: # 10대, 20대, 30대
        train = this.train
        test = this.test
        return this

    @staticmethod
    def fare_ordinal(this) -> object: # 비쌈, 중간, 쌈
        train = this.train
        test = this.test
        return this

    @staticmethod
    def embarked_nominal(this) -> object: # 승선점 S, C, A
        train = this.train
        test = this.test
        return this

if __name__ == '__main__': # 테스트용
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = TitanicModel.sex_nominal(this)
    print(this.train['Gender'])