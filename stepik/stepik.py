# 1. Загружаем числа из файла
with open('17.txt') as f:
    a = [int(x) for x in f]

# 2. Находим максимальный элемент, оканчивающийся на 37
max_37 = -1
for x in a:
    if x % 100 == 37:
        max_37 = max(max_37, x)

# Функция для проверки "двух одинаковых цифр в конце"
def has_same_last_digits(n):
    # n % 10 - последняя цифра, n // 10 % 10 - предпоследняя
    # Условие корректно работает для чисел >= 10
    return n >= 10 and (n % 10 == n // 10 % 10)

count = 0
total_sum = 0

# 3. Перебираем четверки идущих подряд элементов
for i in range(len(a) - 3):
    four = [a[i], a[i+1], a[i+2], a[i+3]]
    
    # Считаем, сколько элементов в четверке больше max_37
    greater_count = sum(1 for x in four if x > max_37)
    
    # Считаем, сколько элементов оканчиваются на 2 одинаковые цифры
    same_digits_elements = [x for x in four if has_same_last_digits(x)]
    
    # 4. Проверяем условия задачи
    if greater_count == 2 and len(same_digits_elements) == 1:
        count += 1
        # Добавляем в сумму тот самый единственный элемент
        total_sum += same_digits_elements[0]

# Вывод ответа: количество и сумма
print(count, total_sum)