import random

CROSSES_MOVE = "X"
NOUGHTS_MOVE = "O"
EMPTY_CELL = "."

COLS = 3
ROWS = 3

QUANTITY_CROSSES = 5
QUANTITY_NOUGHTS = 4

USER_STEP = "USER"
COMP_STEP = "COMP"
CURRENT_STEP = ''

USER_SIGN = ""
COMP_SIGN = ""

USER_WINNER = "USER"
COMP_WINNER = "COMP"
WINNER = ''
field = []

game_is_running = True

STEPS_COUNT = 0

for i in range(COLS):
    field.append([])
    for j in range(ROWS):
        field[i].append(EMPTY_CELL)

for i in range(ROWS):
    for j in range(COLS):
        print(field[i][j], end=' ')
    print()

if random.randint(1, 1000) <= 500:
    CURRENT_STEP = USER_STEP
    USER_SIGN = CROSSES_MOVE
    COMP_SIGN = NOUGHTS_MOVE
else:
    CURRENT_STEP = COMP_STEP
    COMP_SIGN = CROSSES_MOVE
    USER_SIGN = NOUGHTS_MOVE

while game_is_running:
    i_input = 0
    j_input = 0
    if CURRENT_STEP == USER_STEP:
        print('Ход человека:')
        continue_random = True
        while continue_random:
            i_input = int(input('Введите номер строки: ')) - 1
            j_input = int(input('Введите номер столбца: ')) - 1
            if field[i_input][j_input] == EMPTY_CELL:
                continue_random = False
            else:
                print('Эта клетка уже занята')
        field[i_input][j_input] = USER_SIGN
        for i in range(ROWS):
            for j in range(COLS):
                print(field[i][j], end=' ')
            print()
        STEPS_COUNT += 1
        CURRENT_STEP = COMP_STEP
    else:
        print('Ход компьютера (нажмите Enter):')
        input()
        continue_random = True
        while continue_random:
            i_input = random.randint(0, ROWS - 1)
            j_input = random.randint(0, ROWS - 1)
            if field[i_input][j_input] == EMPTY_CELL:
                continue_random = False
        field[i_input][j_input] = COMP_SIGN
        for i in range(ROWS):
            for j in range(COLS):
                print(field[i][j], end=' ')
            print()
        STEPS_COUNT += 1
        CURRENT_STEP = USER_STEP
    if STEPS_COUNT >= 5:
        main_diagonal = False
        side_diagonal = False
        verticals = False
        horizontals = False
        if (field[0][0] == field[1][1] == field[2][2]) and field[0][0] != EMPTY_CELL:
            main_diagonal = True
            if field[0][0] == USER_SIGN:
                WINNER = USER_WINNER
            else:
                WINNER = COMP_WINNER
        elif (field[2][0] == field[1][1] == field[0][2]) and field[2][0] != EMPTY_CELL:
            side_diagonal = True
            if field[0][2] == USER_SIGN:
                WINNER = USER_WINNER
            else:
                WINNER = COMP_WINNER
        elif field[0][0] == field[1][0] == field[2][0] and field[0][0] != EMPTY_CELL:
            verticals = True
            if field[0][0] == USER_SIGN:
                WINNER = USER_WINNER
            else:
                WINNER = COMP_WINNER
        elif field[0][1] == field[1][1] == field[2][1] and field[0][1] != EMPTY_CELL:
            verticals = True
            if field[0][1] == USER_SIGN:
                WINNER = USER_WINNER
            else:
                WINNER = COMP_WINNER
        elif field[0][2] == field[1][2] == field[2][2] and field[0][2] != EMPTY_CELL:
            verticals = True
            if field[0][2] == USER_SIGN:
                WINNER = USER_WINNER
            else:
                WINNER = COMP_WINNER
        elif field[0][0] == field[0][1] == field[0][2] and field[0][0] != EMPTY_CELL:
            horizontals = True
            if field[0][0] == USER_SIGN:
                WINNER = USER_WINNER
            else:
                WINNER = COMP_WINNER
        elif field[1][0] == field[1][1] == field[1][2] and field[1][0] != EMPTY_CELL:
            horizontals = True
            if field[1][0] == USER_SIGN:
                WINNER = USER_WINNER
            else:
                WINNER = COMP_WINNER
        elif field[2][0] == field[2][1] == field[2][2] and field[2][0] != EMPTY_CELL:
            horizontals = True
            if field[2][0] == USER_SIGN:
                WINNER = USER_WINNER

            else:
                WINNER = COMP_WINNER
        if main_diagonal or side_diagonal or verticals or horizontals or STEPS_COUNT == 9:
            game_is_running = False
if WINNER == USER_WINNER:
    print('Победил пользователь')
elif WINNER == COMP_WINNER:
    print('Победил компьютер')
else:
    print('Ничья')
