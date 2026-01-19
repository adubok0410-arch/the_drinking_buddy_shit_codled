with open('17_24892.txt') as file:
    
    numbers = [int(i) for i in file]
    special_number = max([i for i in numbers if len(str(i)) == 4 and i < 0 and abs(i) % 9 == 0])   
    d = []
    
    for i in range(len(numbers) - 1):
        x, y = numbers[i], numbers[i + 1]
        t = (x < 0) + (y < 0)
        
        if t == 1 and (x + y) > special_number:
            d.append(x ** 2 + y ** 2)
            
    print(len(d), min(d))    