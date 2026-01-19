def f2(n):
    result = ''
    while n != 0:
        result = str(n % 2) + result
        n // 2
    return result

d = []

for i in range(1, 1000):
    s = f2(i)
    if i % 5 == 0:
        s += '11'
    else:
        zel = i // 5
        zel_def = f2(zel)
        s += zel_def
    
    r = int(s, 2)
    if r > 896 and r % 2 == 0:
        d.append(r)
        
print(min(d))