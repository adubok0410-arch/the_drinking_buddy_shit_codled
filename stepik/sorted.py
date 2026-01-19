a = [int(x) for x in input().split()]
bool = False
temp = 0
while bool == False:
    bool = True
    for i in range(len(a) - 1):
        if a[i + 1] < a[i]:
            temp = a[i + 1]
            a[i + 1] = a[i]
            a[i] = temp
            bool = False
print(*a)