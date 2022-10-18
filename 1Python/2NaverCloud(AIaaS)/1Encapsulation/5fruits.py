"""
### Fruits number tag ###
**************************************
Fruits No.1 : banana
Fruits No.2 : apple
Fruits No.3 : mango
**************************************
"""

class Fruits():
    def __init__(self):
        self.menu = ["banana", "apple", "mango"]
        pass
    
    def print_menu(self):
        title = f"### Fruits number tag ###"
        aster = f"*"*30
        result = f""
        for i in range(0,len(self.menu)):
            result += f"Fruits No.{i+1} : {self.menu[i]}\n"
        print(f"{title}\n{aster}\n{result}{aster}")

    @staticmethod
    def main():
        fruits = Fruits()
        fruits.print_menu()

Fruits.main()