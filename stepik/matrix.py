COLS = 10
ROWS = 10

matrix = []

for i in range(COLS):
    matrix.append([])
    for j in range(ROWS):
        matrix[i].append(0)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()