arr = [1, 4, 7, 10, 13, 16]
result = []
for num in arr:
    if num % 2 == 0:
        result.append(num)
print(result)


numbers = [15, 3, 27, 8, 12]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Максимальный элемент: {max_val}")


arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n // 2):
    temp = arr[i]
    arr[i] = arr[n - 1 - i]
    arr[n - 1 - i] = temp

print(arr)

n = int(input("Введите число для отсчета: "))
while n > 0:
    print(n)
    n -= 1
print("Старт!")

num = int(input("Введите число: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

n = int(input("Введите число: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} — простое число.")
else:
    print(f"{n} — составное число.")

