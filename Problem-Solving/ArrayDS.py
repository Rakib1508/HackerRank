i = int(input())
num_list = list(map(int, input().split()))
[print(a, end=' ') for a in num_list[::-1]]
