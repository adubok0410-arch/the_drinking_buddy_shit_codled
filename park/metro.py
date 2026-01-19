n, i, j = map(int, input().split())
move_a = 0
move_b = 0

if i < j:
    move_a = (j - i - 1)
elif i > j:
    move_a = (n - i) + (j - 1)
if i < j:
    move_b = i - j + n - 1
elif i > j:
    move_b = i - j - 1
result = min(move_a, move_b)
print(result)

    