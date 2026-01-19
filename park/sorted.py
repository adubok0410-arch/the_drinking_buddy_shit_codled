mass = [int(x) for x in input().split()]
max_num = max(mass)
sortet = [0] * (max_num + 1)
d = []
for i in mass:
    sortet[i] += 1
for j in range(max_num + 1):
    d.append((str(j) + ' ') * sortet[j])
print(*d)