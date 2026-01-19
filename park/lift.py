etax = input('Введите кнопки: ')
a = list(etax)
b = 0
k = 0
for i in range(len(a)):
    if a[i] == '1':
        b += 1
    elif a[i] == '2':
        k += 1
print((abs(b - k) + 1))
    