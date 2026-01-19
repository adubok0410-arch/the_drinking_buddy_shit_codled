def f7(n):
    result = ''
    while n != 0:
        result = str(n % 7) + result
        n //= 7
    return result

d = []
for i in range(1, 1000):
    s = f7(i)
    if i % 2 == 0:
        s = '52' + s + '1'
    else:
        s = s[-1] + s[1:-1] + s[0] + '15'
    s = s.lstrip('0')
    if len(s) == 4:
        d.append(i)
    
print(max(d))
    
