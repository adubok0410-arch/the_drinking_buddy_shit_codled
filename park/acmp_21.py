number = int(input("Введите четырехзначное число: "))
spezial_number = 0

number_1 = str(number)
spezial_number = number_1[::-1]

if number_1 == spezial_number:
    print("YES")
else:
    print("NO")
