with open('9_1.txt') as file:
    count = 0
    for s in file:
        numbers = [int(i) for i in s.split()]
        pov_numbers = [i for i in numbers if numbers.count(i) == 3]
        ne_numbers = [i for i in numbers if numbers.count(i) == 1]
        if len(pov_numbers) // 3 == 2 and sum(numbers) // 6 < ne_numbers[0]:
            count += 1
    print(count)