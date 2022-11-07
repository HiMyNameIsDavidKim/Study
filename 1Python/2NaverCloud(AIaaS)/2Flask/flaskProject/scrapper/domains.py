from urllib.request import urlopen

from bs4 import BeautifulSoup


class BugsMusic(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        pass

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        _ = 0
        title = {'class': 'title'}
        artist = {'class': 'artist'}
        titles = soup.find_all(name='p', attrs=title)
        artists = soup.find_all(name='p', attrs=artist)
        [print(f'{i.find("a").text} - {j.find("a").text}') for i, j in zip(titles, artists)]