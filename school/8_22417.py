from itertools import product

count = 0
usl = 0
for i in product('АБЕИЛРТФЦ', repeat=5):
    count += 1
    s = ''.join(i)
    if count % 2 != 0 and s[0] not in 'АЕИ' and s.count('Ц') == s.count('Ф'):
        usl += 1
print(usl)