n = int(input())
a = []
for i in range(n):
    t = []
    for j in range(n):
        t.append(0)
    a.append(t)

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
    