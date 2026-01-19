home_or_school = input()
x = int(input())
if home_or_school == 'Home':
    print('Yes')
else:
    if x % 2 == 0:
        print('No')
    else:
        print('Yes')