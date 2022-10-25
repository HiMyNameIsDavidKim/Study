from dataclasses import dataclass

@dataclass
class Dataset(object):

    context: str #파일이 저장된 경로
    fname: str #파일이름
    train: object #train.csv 가 데이터프레임으로 전환된 객체
    test: object #test.csv 가 데이터프레임으로 전환된 객체
    id: str #승객ID, 문제
    label: str #승객ID에 따른 사망여부, 답안지

    #데이터를 읽고(getter = property) / 쓰기(setter) 기능을 추가한다.