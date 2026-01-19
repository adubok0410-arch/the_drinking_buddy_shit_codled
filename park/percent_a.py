with open('stix.txt') as file:
    
    data = file.read()
    count_a = 0
    all = 0

    for i in file:
        
        if i == 'а':
            count_a += 1

    result = all / len(data) * 100

    print(f'{result}%') 