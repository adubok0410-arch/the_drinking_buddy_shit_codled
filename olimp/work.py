n, t = map(int, input().split())
mass = []
for i in range((10 ** n) - 1, 10 ** (n - 1), -1):
    if i % t == 0:
        mass.append(i)
print(max(mass))