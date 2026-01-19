car = input("Введите скорость автомобилей: ")
m = [int (x) for x in car.split()]
max_speed = max(m)
max_speed_1 = [max_speed]
for i in range(len(max_speed_1)):
    if i > 1:
        print(i[0], i[-1])
    else:
        print(max_speed)
        