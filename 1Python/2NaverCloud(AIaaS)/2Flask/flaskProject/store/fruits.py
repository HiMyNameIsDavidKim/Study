import pandas as pd

# {'제품': ['사과', '딸기', '수박'],
# '가격': [1800, 1500, 3000],
# '판매량': [24, 38, 13]}

def new_fruits_df():
    sc = ['제품', '가격', '판매량']
    ls1 = ['사과', '딸기', '수박']
    ls2 = [1800, 1500, 3000]
    ls3 = [24, 38, 13]
    dc = {sc[i]: j for i, j in enumerate([ls1, ls2, ls3])}
    df = pd.DataFrame(dc)
    return f'{df["가격"].mean()}\n{df["판매량"].mean()}'

if __name__ == '__main__':
    print(new_fruits_df())