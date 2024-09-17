class Common(object):
    def __init__(self):
        pass

    @staticmethod
    def menu(ls):
        for i, j in enumerate(ls): # ["종료", "등록", "출력", "삭제"]
            print(f"{i}. {j}")
        return input("메뉴 선택: ")

    @staticmethod
    def spec(param):
        (lambda x: print(f"--- 1.Shape ---\n{x.shape}\n"
                         f"--- 2.Features ---\n{x.columns}\n"
                         f"--- 3.Info ---\n{x.info}\n"
                         f"--- 4.Case Top1 ---\n{x.head(1)}\n"
                         f"--- 5.Case Bottom1 ---\n{x.tail(3)}\n"
                         f"--- 6.Describe ---\n{x.describe()}\n"
                         f"--- 7.Describe All ---\n{x.describe(include='all')}"))(param)