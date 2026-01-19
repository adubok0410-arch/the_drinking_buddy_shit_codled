ROWS = 5
COLS = 5

snake = []
snake_1 = []

number_1 = 12
number_2 = 16
number_3 = 23
number = 1

for i in range(ROWS):
    snake.append([])
    for j in range(COLS):
        snake[i].append(0)
        
for i in range(ROWS):
    snake_1.append([])
    for j in range(COLS):
        snake_1[i].append(0)

for i in range(ROWS):
    for j in range(COLS):
        if i < 1 and j <= 3:
            snake[i][j] = number
            number += 1
        elif i <= 3 and j > 3:
            snake[i][j] = number
            number += 1
        elif i > 3 and j >= 1:
            snake[i][j] = number_1
            number += 1
            number_1 -= 1

for i in range(ROWS):
    snake.append([])
    for j in range(COLS):
        snake[i].append(0)
        if i > 1 and j < 1:
            snake[i][j] = number_2
            number += 1
            number_2 -= 1
        
for i in range(ROWS):
    snake.append([])
    for j in range(COLS):        
        if i == 1 and j < 4:
            snake[i][j] = number
            number += 1

for i in range(ROWS):
    snake.append([])
    for j in range(COLS):
        if (1 < i < 3) and j == 3:
            snake[i][j] = number
            number += 1
        elif i == 3 and (1 <= j < 4):
            snake[i][j] = number_3
            number += 1
            number_3 -= 1

for i in range(ROWS):
    snake.append([])
    for j in range(COLS):    
        if i == 2 and (1 <= j < 3):
            snake[i][j] = number
            number += 1

for i in range(ROWS):
    for j in range(COLS):
        print('  {}'.format(snake[i][j]), end='  ')
    print()