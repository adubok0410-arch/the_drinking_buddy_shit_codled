n = int(input())
for i in range(n):
    buss = input()
    letters = 'ABCEHKMOPTXYАВСЕНКМОРТХУ'
    if len(buss) == 6 and buss[0] in letters and buss[1].isdigit() and buss[2].isdigit() and buss[3].isdigit() and buss[-2] in letters and buss[-1] in letters:
        print('Yes')
    else:
        print('No')
