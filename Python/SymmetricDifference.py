m = int(input())
list_1 = list(map(int, input().split()))
n = int(input())
list_2 = list(map(int, input().split()))

common = set(list_1).intersection(list_2)
all_items = set(list_1).union(list_2)

diff = [item for item in all_items if item not in common]

for i in sorted(diff):
    print(i)
