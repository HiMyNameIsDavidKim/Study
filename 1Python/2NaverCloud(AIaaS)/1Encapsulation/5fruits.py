"""
### Fruits number tag ###
**************************************
Fruits No.1 : banana
Fruits No.2 : apple
Fruits No.3 : mango
**************************************
구매할 과일 : 바
바나나
"""

class Fruits():
    def __init__(self):
        self.menu = ["banana", "apple", "mango"]
    
    def print_menu(self):
        title = f"### Fruits number tag ###"
        aster = f"*"*30
        result = f""
        menu = self.menuㅇ
        for i in range(0,len(menu)):
            result += f"Fruits No.{i+1} : {menu[i]}\n"
        print(f"{title}\n{aster}\n{result}{aster}")
        buy = input("Choose fruit that you want to buy : ")
        for i in menu:
            if i[0] == buy: print(i)
            else: pass

    @staticmethod
    def main():
        fruits = Fruits()
        fruits.print_menu()

Fruits.main()