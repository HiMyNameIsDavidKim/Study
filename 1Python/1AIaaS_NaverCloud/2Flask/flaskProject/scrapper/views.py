from scrapper.services import MusicChart


class ScrapperController(object):

    @staticmethod
    def menu_0(*args):
        print(args[0])

    @staticmethod
    def menu_1(*args):
        print(args[0])
        MusicChart(args[1])

    @staticmethod
    def menu_2(*args):
        print(args[0])
        MusicChart(args[1])