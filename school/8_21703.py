from itertools import product

count = 0
for i in product('АБДЕОП', repeat=6):
    count += 1
    s = ''.join(i)
    if count % 2 == 0 and s[0] == 'О' and len(set(s)) == 6:
        print(count)