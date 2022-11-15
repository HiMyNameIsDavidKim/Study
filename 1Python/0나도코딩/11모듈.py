#모듈 공부1(기본)
#함수 정의나 클래스 등의 문장을 담는 파일을 모듈이라고 함.
#모듈의 확장자는 ---.py 이다.
#theater_module이라는 모듈을 생성하고 여기서는 모듈을 활용해보자.
#모듈 뒤에 점을 찍고, 정의한 메서드를 불러오면 됨.
#불러오는 3가지 방법이 있음.

# #가장 기본적인 방법
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# #모듈을 원하는 명칭으로 불러오는 방법
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# #from을 사용해서 불러오는 방법
# #이 경우에는 모듈명을 안적어도 된다.
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)




