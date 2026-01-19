from itertools import product

count_1 = 0
count_2 = 0

for i in product('АВИКЛОРТ', repeat=6):
    count_1 += 1
    count_2 += 1
    s = ''.join(i)
    if s == 'ВИКТОР':
        print(s, count_1)
    elif s == 'КИРИЛЛ':
        print(s, count_2)