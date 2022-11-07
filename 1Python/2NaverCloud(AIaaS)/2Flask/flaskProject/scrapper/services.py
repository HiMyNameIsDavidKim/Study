from urllib.request import urlopen
from bs4 import BeautifulSoup
from scrapper import MusicRanking


def BugsMusic(arg):
    arg = MusicRanking()
    soup = BeautifulSoup(urlopen(arg.domain), 'lxml')
    title = {'class': arg.class_name[0]}
    artist = {'class': arg.class_name[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)
    # 디버깅
    [print(f'{i}위.{j.find("a").text} - {k.find("a").text}')
     for i, j, k in zip(range(1, len(titles)+1), titles, artists)]
    # dict 로 변환
    for i in range(0, len(titles)):
        arg.dic[arg.titles[i]] = arg.artists[i]
    # csv 파일로 저장
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()