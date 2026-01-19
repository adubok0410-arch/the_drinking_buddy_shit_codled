from itertools import product

count = 0
for i in product('АГИНРТ', repeat=6):
    count += 1
    s = ''.join(i)
    if s[0] != 'А' and s[0] != 'Г' and s[0] != 'И' and s.count('А') == 1 and count % 2 != 0:
        print(s, count)
        break