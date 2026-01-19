n = int(input())
money = [int(i) for i in input().split()]
needed_amount_of_money = 0
for i in money:
    difference = max(money) - i
    needed_amount_of_money += difference
print(needed_amount_of_money) 
