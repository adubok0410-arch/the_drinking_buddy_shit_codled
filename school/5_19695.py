def f2(n):
    result = ''
    while n != 0:
        result = str(n % 2) + result
        n //= 2
    return result

d = []
for i in range(1, 1000):
    s = f2(i)
    if i % 3 == 0:
        s += s[-2:]
    else:
        s = '1' + s + '1'
    
    r = int(s, 2)
    if r > 700:
        d.append(r)

print(min(d))