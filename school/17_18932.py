with open('17_18932.txt') as file:
    numbers = [int(i) for i in file]
    special_numbers = len([i for i in numbers if abs(i) % 2 == 0])
    d = []
    for i in range(len(numbers) - 1):
        x, y = numbers[i], numbers[i + 1]
        t = (x > 0) + (y > 0)
        if t >= 1 and (x + y) < special_numbers:
            d.append(x ** 2 + y ** 2)
    print(len(d), max(d))