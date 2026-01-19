def f3(n):
    result = ''
    while n != 0:
        result = str(n % 3) + result
        n = n // 3
    return result

d = []

for i in range(1, 1000):
    s = f3(i)
    if i % 3 == 0:
        s += s[-2:]
    else:
        s += str(f3(sum(int(i) for i in s)))

    r = int(s, 3)
    if r > 220 and r % 2 == 0:
        d.append(r)
    
print(min(d))
