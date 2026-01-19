def f3(n):
    result = ''
    while n != 0:
        result = str(n % 3) + result
        n //= 3
    return result

d = []

for i in range(1, 1000):
    s = f3(i)
    if i % 3 == 0:
        s += s[-2:]
    else:
        digit_sum = 0
        for char in s:
            digit_sum += int(char)
        
            tr_sum = f3(digit_sum)
            s += tr_sum
    
    r = int(s, 3)
    if r > 208 and r % 2 != 0:
        d.append(r)
    
print(min(d))