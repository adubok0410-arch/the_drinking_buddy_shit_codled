# def rectangle(cols, rows, symbol):

#     if cols < 0 and rows < 0:
#         print('Нельзя сделать прямоугольник из отрицательного числа!!')
#     else:
#         for i in range(cols):
#             for j in range(rows):
#                 print(symbol, end='')
#             print()

# rectangle(5, 6, '*')

# def drawing(numbers, symbol):

#     if numbers < 0:
#         print(f'Число {numbers} должно быть не отрицательным!!!')  
#     else:
#         for i in range(numbers):
#             print(symbol)

# drawing(50, '*')

# def drawing(numbers, symbol):

#     if numbers < 0:
#         print(f'Число {numbers} должно быть не отрицательным!!!')  
#     else:
#         print(numbers * symbol)

# drawing(50, '*')

# import math

# def factorial_number(numbers):

#     if numbers < 0:
#         return None

#     return math.factorial(numbers)

# numerator = 2 * factorial_number(5) + 3 * factorial_number(8)
# denominator = factorial_number(6) + factorial_number(4)

# print(numerator / denominator)

# def prime_number(number):
    
    
#     if number <= 1:
#         return None
    
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return None

#     return 1

# number = int(input('Введите число: '))
# result = prime_number(number)

# if result is None:
#     print(f'Число {number} не простое')
# else:
#     print(f'Число {number} простое')