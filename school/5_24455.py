from itertools import product

count = 0

for i in product('АВИКЛОРТ', repeat=6):
    count += 1
    s = ''.join(i)
    if s == 'КИРИЛЛ':
        print(s, count) #42991 + 109733
        
print(42991 + 109733)