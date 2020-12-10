es = int(input())
e_mem = set(map(int, input().split()))
fr = int(input())
f_mem = set(map(int, input().split()))

print(len(e_mem.symmetric_difference(f_mem)))
