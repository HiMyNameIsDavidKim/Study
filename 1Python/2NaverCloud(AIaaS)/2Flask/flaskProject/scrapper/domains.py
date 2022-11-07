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
class MusicRanking(object):
    html: str
    parser: str
    domain: str
    query_string: str
    headers: dict
    tag_name: str
    fname: str
    class_name: list
    artists: list
    titles: list
    dic: dict
    df: None

    @property
    def html(self) -> str: return self._html
    @html.setter
    def html(self, html): self._html = html

    @property
    def parser(self) -> str: return self._parser
    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def domain(self) -> str: return self._domain
    @domain.setter
    def domain(self, domain): self._domain = domain

    @property
    def query_string(self) -> str: return self._query_string
    @query_string.setter
    def query_string(self, query_string): self._query_string = query_string

    @property
    def headers(self) -> str: return self._headers
    @headers.setter
    def headers(self, headers): self._headers = headers

    @property
    def tag_name(self) -> str: return self._tag_name
    @tag_name.setter
    def tag_name(self, tag_name): self._tag_name = tag_name

    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def class_name(self) -> str: return self._class_name
    @class_name.setter
    def class_name(self, class_name): self._class_name = class_name

    @property
    def artists(self) -> str: return self._artists
    @artists.setter
    def artists(self, artists): self._artists = artists

    @property
    def titles(self) -> str: return self._titles
    @titles.setter
    def titles(self, titles): self._titles = titles

    @property
    def dic(self) -> str: return self._dic
    @dic.setter
    def dic(self, dic): self._dic = dic

    @property
    def df(self) -> str: return self._df
    @df.setter
    def df(self, df): self._df = df

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient='index')

    def dataframe_to_csv(self):
        path = CTX+self.fname+'.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')