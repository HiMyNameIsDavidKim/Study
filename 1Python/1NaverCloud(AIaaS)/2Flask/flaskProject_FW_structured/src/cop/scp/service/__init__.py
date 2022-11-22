from src.cop.scp.service.cop_scp_service import BugsMusic, MelonMusic
from src.cop.scp.service.cop_scp_vo import Scrap

if __name__=="__main__":
    scrap = Scrap()
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
        else:
            print("해당메뉴 없음")