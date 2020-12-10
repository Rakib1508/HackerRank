n, m = map(int, input().split())

num_list = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness = 0

for i in range(n):
    if num_list[i] in set_a:
        happiness += 1
    elif num_list[i] in set_b:
        happiness -= 1

print(happiness)
