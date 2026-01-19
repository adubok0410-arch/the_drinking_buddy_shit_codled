from itertools import product

count = 0

for i in product('ОВАРТ', repeat=5):
    count += 1
    s = ''.join(i)
    print(count, s)
    # s = ''.join(i)
    # if s == 'ТОВАР':
    #     print(count, s)