from titanic.models import TitanicModel
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
            model = TitanicModel()
            print_ = model.new_model("train.csv")
            print(f"Type : {type(print_)}")
            print(f"Columns : {print_.columns}")
            print(f"Head : {print_.head}")
            print(f"Null수 : {print_.isnull().sum()}")
            #plot = Plot("train.csv")
            #plot.draw_sex()
            #Null Memo : Age 177ea, Cabin 687ea, Embarked 2ea
        elif menu == "2":
            print(" ### 모델링 ### ")
        elif menu == "3":
            print(" ### 머신러닝 ### ")
        else:
            print(" ### 해당 메뉴 없음 ### ")