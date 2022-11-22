from dataclasses import dataclass
import pandas as pd
from bs4 import BeautifulSoup

@dataclass
class Scrap:
    html = ''
    parser = ''
    domain = ''
    query_string = ''
    headers = {}
    tag_name = ''
    fname = ''
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = 'save/melon_ranking.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)



