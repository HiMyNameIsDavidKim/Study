import os
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from dataclasses import dataclass
import pandas as pd
from src.cmm.const.path import static

@dataclass
class ScrapVO:
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
        path = f'{static}/save/cop/scp/melon_ranking.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)

def BugsMusic(arg):
    soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), 'lxml')
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    diction = {} # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv() # csv파일로 저장


def MelonMusic(arg):
    soup = BeautifulSoup(urlopen(urllib.request.Request(arg.domain + arg.query_string, headers={'User-Agent' : "Mozilla/5.0"})), "lxml")
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    titles = [i.find('a').text for i in titles]
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    artists = [i.find('a').text for i in artists]
    [print(f"{i}위 {j} : {k}") # 디버깅
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    diction = {} # dict 로 변환
    for i, j in enumerate(titles):
        diction[j] = artists[i]
    arg.diction = diction
    arg.dict_to_dataframe()
    arg.dataframe_to_csv() # csv파일로 저장


if __name__=="__main__":
    scrap = ScrapVO()
    while True:
        menu = input("0번:종료,1번:벅스")
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("벅스")
            scrap.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            scrap.query_string = "20221101"
            scrap.parser = "lxml"
            scrap.class_names=["title", "artist"]
            scrap.tag_name = "p"
            BugsMusic(scrap)
        elif menu == "2":
            print("멜론")
            scrap.domain = "https://www.melon.com/chart/index.htm?dayTime="
            scrap.query_string = "2022110909"
            scrap.parser = "lxml"
            scrap.class_names = ["rank01", "rank02"]
            scrap.tag_name = "div"
            MelonMusic(scrap)

        elif menu == "3":
            df = pd.read_csv(f"{static}/save/cop/scp/bugs_ranking.csv")
            print(df)
        else:
            print("해당메뉴 없음")
