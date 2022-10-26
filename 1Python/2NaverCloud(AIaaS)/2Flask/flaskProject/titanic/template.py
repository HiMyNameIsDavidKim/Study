from titanic.models import TitanicModel
from util.dataset import Dataset
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

class Plot(object):

    dataset = Dataset()
    model = TitanicModel()

    def __init__(self, fname):
        self.entry = self.model.new_model(fname)

    def __str__(self):
        return f""

    def draw_survived(self):
        this = self.entry
        f, ax = plt.subplots(1, 2, figsize=(18, 8)) #한 화면에 2개 그래프 그린다.
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 vs 1.생존자')
        sns.countplot(x='Survived', data=this, ax=ax[1])
        plt.show()