def f3(numbers):

    result = ''

    while numbers != 0:
        result = str(numbers % 3) + result
        numbers //= 3
    return result

d = []

for i in range(1, 1000):

    s = f3(i)

    if i % 5 == 0:
        s += s[-2:]
    else:
        ost_dividers = i % 5 * 7
        f_ost_dividers = f3(ost_dividers)
        s += f_ost_dividers

    r = int(s, 3)
    if r <= 273:
        d.append(i)

print(max(d))