def roundels(number):

    result = 0

    for i in range(len(number)):

        if number[i] == '8':
            result += 2
        elif number[i] in ('0', '6', '9'):
            result += 1

    print(result)

number = input().strip()

roundels(number)