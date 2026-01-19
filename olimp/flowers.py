flowers = ['G', 'C', 'V']
k = int(input())
for i in range(k):
    flowers[2], flowers[1] = flowers[1], flowers[2]
    flowers[0], flowers[1] = flowers[1], flowers[0]
print(*flowers, sep='')