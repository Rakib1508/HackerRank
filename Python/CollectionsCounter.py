from collections import Counter

number_of_shoes = int(input())
shoes_inventory = Counter(map(int, input().split()))
queued_customer = int(input())
income = 0

for num in range(queued_customer):
    size, price = map(int, input().split())
    if shoes_inventory[size]:
        income += price
        shoes_inventory[size] -= 1

print(income)
