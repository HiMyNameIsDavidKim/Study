from titanic.models import TitanicModel
from util.dataset import Dataset

class TitanicController(object):

    dataset = Dataset()
    model = TitanicModel()

    def __init__(self):
        pass

    def __str__(self):
        return f""

    def preprocess(self, train, test) -> object: # 전처리
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        this = model.sex_nominal(this)
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_nominal(this)
        this = model.title_norminal(this)
        this = model.drop_features(this,
                                   'PassengerId', 'Name', 'Sex', 'Age',
                                   'SibSp', 'Parch', 'Ticket',
                                   'Fare', 'Cabin')
        return this

    def modeling(self, train, test) -> object: # 모델 생성
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        return this

    def learning(self, train, test): # 머신러닝
        pass

    def submit(self, train, test): # 제출
        pass

if __name__ == '__main__':
    this = TitanicController()
    this = this.modeling('Train.csv', 'Test.csv')
    print(this.train.columns)
    print(f"[null 갯수]\n{this.train.isnull().sum()}")
    print(this.train.head(5))