from bicycle.models import BicycleModel
from bicycle.views import BicycleController
from util.common import Common

api = BicycleController
while True:
    menu = Common.menu(["종료", "시각화", "모델링", "머신러닝", "배포"])
    if menu == "0":
        print(" ### 종료 ### ")
        break
    elif menu == "1":
        print(" ### 시각화 ### ")
        model = BicycleModel()
        print_ = model.new_model("train.csv")
        print(f"Type : {type(print_)}")
        print(f"Columns : {print_.columns}")
        print(f"[Head]\n{print_.head}")
        print(f"[Null수]\n{print_.isnull().sum()}")
    elif menu == "2":
        print(" ### 모델링 ### ")
    elif menu == "3":
        print(" ### 머신러닝 ### ")
    else:
        print(" ### 해당 메뉴 없음 ### ")