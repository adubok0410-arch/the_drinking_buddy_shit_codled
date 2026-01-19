def f2(n):
    result = ''
    while n != 0:
        result = str(n % 2) + result
        n = n // 2
    return result

d =[]
for i in range(1, 1000):
    s = f2(i)
    sum_bin = sum([int(x) for x in s])
    s += str(sum_bin % 2) 
    sum_bin = sum([int(x) for x in s])
    s += str(sum_bin % 2)

    r = int(s, 2)
    if r > 253:
        d.append(i)

print(min(d))