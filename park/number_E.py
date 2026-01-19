n = int(input())
e = '2.7182818284590452353602875'
a = list(e[:n + 3])
if n == 0:
    print(3)
elif n == 25:
    print(*e, sep='')
elif int(a[-1]) >= 5:
    a[-2] = str(int(a[-2]) + 1)
    print(*a[:-1], sep='')
else:
    print(*a[:-1], sep='')
