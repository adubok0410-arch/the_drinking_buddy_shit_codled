x = int(input())
y = int(input())
n = int(input())

effective_jump = x + y
pairs_of_jumps = n // effective_jump
total_jumps = 2 * pairs_of_jumps
left = n % effective_jump

if left == 0:
    print(total_jumps)
elif left <= y:
    print(total_jumps + 1)
else:
    print(total_jumps + 2)