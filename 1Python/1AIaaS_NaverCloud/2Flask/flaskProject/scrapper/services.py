import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrapper import Scrap

def MusicChart(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    title = {'class': arg.class_names[0]}
    artist = {'class': arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    titles = [i.find('a').text for i in titles]
    artists = [i.find('a').text for i in artists]
    # 디버깅
    [print(f'{i+1}위.{j} - {k}')
     for i, j, k in zip(range(len(titles)), titles, artists)]
    # dict 로 변환
    diction = {}
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    # csv 파일로 저장
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()