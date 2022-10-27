from titanic.template import Plot
from titanic.views import TitanicController
from util.common import Common

if __name__ == "__main__":
    api = TitanicController()
    while True:
        menu = Common.menu(["종료", "시각화", "모델링", "머신러닝", "배포"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 시각화 ### ")
            plot = Plot("train.csv")
            plot.draw_survived()
            plot.draw_pclass()
            plot.draw_sex()
            plot.draw_embarked()
        elif menu == "2":
            print(" ### 모델링 ### ")
            df = api.modeling('train.csv', 'test.csv')
        elif menu == "3":
            print(" ### 머신러닝 ### ")
            df = api.learning('train.csv', 'test.csv')
        elif menu == "4":
            print(" ### 배포 ### ")
            df = api.submit('train.csv', 'test.csv')
        else:
            print(" ### 해당 메뉴 없음 ### ")