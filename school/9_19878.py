with open('9_19878.txt') as file:
    count = 0
    for s in file:
        numbers = [int(i) for i in s.split()]
        numbers_3 = [i for i in numbers if numbers.count(i) == 3]
        numbers_1 = [i for i in numbers if numbers.count(i) == 1]
        if len(set(numbers_3)) == 1 and len(numbers_1) == 4 and sum(numbers_1) / len(numbers_1) <= numbers_3[0]:
            count += 1
print(count)