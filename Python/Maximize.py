from itertools import product

def calculate(num_list):
    return sum(x**2 for x in num_list) % m


k, m = map(int, input().split())
arrays = (list(map(int, input().split()[1:])) for _ in range(k))

combination = product(*arrays)
print(max(map(calculate, combination)))
