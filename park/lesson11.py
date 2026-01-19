def input_numbr(message):
    number = int(input(message))
    return number

def sum_numbers(a, b):
    return a + b

a = input_numbr("введите первое число: ")
b = input_numbr("введите второе число: ")

result = sum_numbers(a, b)

print(f"сумма = {result}")