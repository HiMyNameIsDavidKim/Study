#공통기능을 하는 공통 모듈

class Common(object):
    def __init__(self):
        pass

    @staticmethod
    def get_data(ls):
        [print(i) for i in ls]

    @staticmethod
    def delete_data(ls, name):
        del ls[[i for i, j in enumerate(ls)
                if j.name == name][0]]

    @staticmethod
    def menu(ls):
        [print(f"{i}.{j}") for i,j in enumerate(ls)]
        return input("메뉴선택 : ")

    @staticmethod
    def spec(read_csv):
        (lambda x: print(f' --- 2.Spec ---\n'
                            f'--- 1)Shape ---\n{x.shape}\n'
                            f'--- 2)Features ---\n{x.columns}\n'
                            f'--- 3)Info ---\n{x.info()}\n'
                            f'--- 4)Case Top1 ---\n{x.head(1)}\n'
                            f'--- 5)Case Bottom1 ---\n{x.tail(3)}\n'
                            f'--- 6)Describe ---\n{x.describe()}\n'
                            f'--- 7)Describe All ---\n{x.describe(include="all")}'))(read_csv)