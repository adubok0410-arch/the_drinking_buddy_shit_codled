from itertools import product

count = 0

for i in product('АВНРЬЯ', repeat=5):
    flag = True
    count += 1
    for j in range(len(i) - 1):
        if i[j] == i[j + 1] == 'Я':
             flag = False
             break
    if i[0] != 'Я' and i.count('Ь') <= 1 and flag:
        print(count)
