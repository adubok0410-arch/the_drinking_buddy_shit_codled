with open('17_1.txt') as file:
    numbers = [int(x) for x in file]
    spezial_numbers = max([i for i in numbers if 10000 <= abs(i) <= 99999 and abs(i) % 100 == 43])
    d = []
    for i in range(len(numbers) - 2):
        x, y, z = numbers[i], numbers[i + 1], numbers[i + 2]
        t = (10000 <= abs(x) <= 99999 and abs(x) % 100 == 43) + (10000 <= abs(y) <= 99999 and abs(y) % 100 == 43) + (10000 <= abs(z) <= 99999 and abs(z) % 100 == 43)
        if t >= 1 and (x ** 2 + y ** 2 + z ** 2) <= spezial_numbers ** 2:
            d.append(x ** 2 + y ** 2 + z ** 2)
    print(len(d), min(d))