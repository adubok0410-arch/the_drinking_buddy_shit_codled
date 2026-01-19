number = int(input("Введите четырехзначное число: "))
number_1 = number
spezial_number = 0

while number != 0:
    spezial_number = spezial_number * 10 + number % 10
    number = number // 10

if number_1 == spezial_number:
    print("YES")
else:
    print("NO")