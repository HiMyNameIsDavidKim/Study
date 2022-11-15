from dataclasses import dataclass
import urllib
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

'''
class BugsMusic(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        pass

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        title = {'class': 'title'}
        artist = {'class': 'artist'}
        titles = soup.find_all(name='p', attrs=title)
        artists = soup.find_all(name='p', attrs=artist)
        [print(f'{i}위.{j.find("a").text} - {k.find("a").text}') for i, j, k in zip(range(1, len(titles)+1), titles, artists)]
'''

@dataclass
class Scrap(object):
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
        path = './save/result.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header={'User-Agent': "Mozilla/5.0"})