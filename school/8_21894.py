from itertools import permutations

count = 0
for i in permutations('0123456789', 4):
    if i[0] != '0':
        numbers = [int(j) for j in i]
        flag = True
        for j in range(len(i) - 1):
            if numbers[j] % 2 == numbers[j + 1] % 2:
                flag = False
                break
        if flag:
            count += 1
print(count)
