n = int(input())
arr = map(int, input().split(' '))
my_set = set(arr)
item = list(sorted(my_set))
print(item[-2])
