import pandas as pd

class Mpg(object):

    @staticmethod
    def menu_0(*args):
        print(args[0])

    @staticmethod
    def menu_1(*args) -> object:
        print(args[0])
        mpg = args[1]
        return print(mpg.head())

    @staticmethod
    def menu_2(*args) -> object:
        print(args[0])
        mpg = args[1]
        return print(mpg.tail())

    @staticmethod
    def menu_3(*args) -> object:
        print(args[0])
        mpg = args[1]
        return print(mpg.shape)

    @staticmethod
    def menu_4(*args) -> object:
        print(args[0])
        mpg = args[1]
        return print(mpg.info())

    @staticmethod
    def menu_5(*args) -> object:
        print(args[0])
        mpg = args[1]
        return print(mpg.describe())