'''
[설명]
밑변의 길이와 높이가 n인 삼각형
맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기
첫 행부터 마지막 행까지 모두 순서대로 합친 배열 리턴

[아이디어]
삼각형 배열 만들고
맵이동처럼 구현하기

[시간 복잡도]
[변수]
'''


def solution(n):
    # 1. 실제 삼각형 모양의 배열 생성
    # 예: n=4 -> [[0], [0,0], [0,0,0], [0,0,0,0]]
    triangle = [[0] * (i + 1) for i in range(n)]

    # 2. 현재 위치(x, y)와 채울 숫자(num) 초기화
    # 첫 이동이 (0, 0)이 되도록 x=-1에서 시작
    x, y = -1, 0
    num = 1

    # 3. 방향을 바꿔가며 n번 반복
    for i in range(n):
        # 현재 방향(0: 아래, 1: 오른쪽, 2: 대각선 위)
        direction = i % 3
        # 이번 방향으로 이동할 횟수
        steps = n - i

        # 4. 이동 횟수만큼 숫자를 채움
        for _ in range(steps):
            if direction == 0:  # 아래로 이동
                x += 1
            elif direction == 1:  # 오른쪽으로 이동
                y += 1
            elif direction == 2:  # 대각선 왼쪽 위로 이동
                x -= 1
                y -= 1
            
            triangle[x][y] = num
            num += 1

    # 5. 2차원 배열을 1차원 배열로 펼쳐서 반환
    result = []
    for row in triangle:
        result.extend(row)
    
    return result





