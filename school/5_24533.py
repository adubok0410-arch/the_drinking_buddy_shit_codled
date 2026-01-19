from itertools import product

count = 0
for i in product('АЕКНОТ', repeat=7):
    count += 1
    s = ''.join(i)
    if count % 2 != 0:
        print(s, count)