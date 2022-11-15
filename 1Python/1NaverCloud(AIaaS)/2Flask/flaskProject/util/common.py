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