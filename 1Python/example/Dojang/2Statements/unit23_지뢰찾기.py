def solution(x, y):
    matrix = []
    for i in range(x):
        matrix.append([])
        n_row = input()
        n_row = list(n_row)
        for j in range(y):
            if n_row[j] == '*': matrix[i].append(n_row[j])
            elif n_row[j] == '.': matrix[i].append(0)

    for i in range(x):
        for j in range(y):
            if matrix[i][j] == '*':
                for k in range(-1,2):
                    for w in range(-1,2):
                        try :
                            if matrix[i+k][j+w] == '*': pass
                            elif matrix[i+k][j+w] != '*' and i+k>=0 and j+w>=0: matrix[i+k][j+w] += 1
                            else: pass
                        except IndexError: continue
            else: continue

    print('\n[answer]')
    for i in range(x):
        for j in range(y):
            print(matrix[i][j], end='')
        print()


if __name__ == '__main__':
    x, y = map(int, input().split())
    solution(x,y)