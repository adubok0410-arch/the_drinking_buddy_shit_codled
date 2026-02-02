from itertools import product

count = 0

for i in product('АБИНОРТУ', repeat=5):

    count += 1
    s = ''.join(i)

    if count % 2 != 0 and s[0] not in 'АИОУ' and len(set(s)) == len(s):
        print(count)
        