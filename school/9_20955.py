with open('9_20955.txt') as file:
    count = 0
    for s in file:
        numbers = [int(i) for i in s.split()]
        numbers_2 = [i for i in numbers if numbers.count(i) == 2] #[2, 2, 4, 4]
        numbers_1 = [i for i in numbers if numbers.count(i) == 1]
        if len(set(numbers_2)) == 2 and len(numbers_1) == 4 and sum(set(numbers_2)) >= sum(numbers_1):
            count += 1
    print(count)