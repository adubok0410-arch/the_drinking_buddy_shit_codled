k1, l1, m1 = list(map(int, input().split()))
k2, l2, m2 = list(map(int, input().split()))

bolts_remaining = k1 * (100 - l1) // 100
nuts_remaining = k2 * (100 - l2) // 100

pairs = min(bolts_remaining, nuts_remaining)

damage = (k1 - pairs) * m1 + (k2 - pairs) * m2

print(damage)