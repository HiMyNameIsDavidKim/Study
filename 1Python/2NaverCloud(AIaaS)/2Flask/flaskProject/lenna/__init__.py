import cv2

'''
이미지 읽기의 flag는 3가지가 있습니다.
cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.
cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 실제 이미지 처리시 중간단계로 많이 사용합니다.
cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입
3개의 flag대신에 1, 0, -1을 사용해도 됩니다.

Shape is (512, 512, 3)
y축:512(앞)
x축:512(뒤)
3(=RGB)
cv2.waitKey(0) : keyboard입력을 대기하는 함수.
                 0이면 key입력까지 무한대기이며,
                 특정 시간동안 대기하려면 ms값 입력.
cv2.destroyAllWindows() : 화면 종료
'''

from lenna.template import LennaTemplate
from lenna.views import LennaController
from util.common import Common

if __name__ == "__main__":
    api = LennaController()
    while True:
        menu = Common.menu(["종료", "원본 보기", "그레이스케일", "엣지검출", "배포"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 원본 보기 ### ")
            img = api.modeling('lenna.png')
            print(f'Shape is {img.shape}')
            cv2.imshow('This', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif menu == "2":
            img = input("URL을 입력하세요 : ")
            print(" ### 그레이스케일 ### ")
            api.grayscale(img)
        elif menu == "3":
            img = input("URL을 입력하세요 : ")
            print(" ### 엣지검출 ### ")
            api.edgedetect(img)
        elif menu == "4":
            print(" ### 배포 ### ")
        else:
            print(" ### 해당 메뉴 없음 ### ")