with open('9.txt') as file:
    count = 0
    for s in file:
        numbers = [int(i) for i in s.split()]
        numbers3 = [i for i in numbers if numbers.count(i) == 3]
        numbers1 = [i for i in numbers if numbers.count(i) == 1]
        if len(numbers3) // 3 == 1 and len(numbers1) == 4 and max(numbers) in numbers1:
            count += 1
    print(count)