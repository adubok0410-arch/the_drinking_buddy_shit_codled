COLS = 7
ROWS = 7

square = []
alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.-'

user_word = input('Введите слово: ')
zero_word = False

if len(user_word) == 0:
    zero_word = True

for i in range(COLS):
    square.append([])
    for j in range(ROWS):
        square[i].append(0)

numbers_i = 1
numbers_j = 1
letter = 0

for i in range(ROWS):
    for j in range(COLS):
        if i == j == 0: 
            square[i][j] = ' '
        elif i < 1 and j > 0:
            square[i][j] = numbers_i
            numbers_i += 1
        elif i >= 1 and j == 0:
            square[i][j] = numbers_j
            numbers_j += 1 
        else:
            square[i][j] = alphabet[letter]
            letter += 1

word_index = 0
numbers_word = ''
arr =[]

while word_index < len(user_word):
    for i in range(ROWS):
        if word_index == len(user_word):
            break
        for j in range(COLS):
            if square[i][j] == user_word[word_index]:
                numbers_word = str(i) + str(j)
                word_index += 1
                arr.append(numbers_word)
                if word_index == len(user_word):
                    break

for i in range(ROWS):
    for j in range(COLS):
        print(square[i][j], end=' ')
    print()

if zero_word == True:
    print('Вы не ввели слово, введите слово!!!')
elif zero_word == False:
    print('Введенное слово -', user_word)
    print('Зашифрованно под номерами:', *arr) 