from itertools import permutations

string, base = input().split()
initial_list = list(permutations(string, int(base)))
result_list = []

for item in initial_list:
    result_list.append(''.join(item))

for s in sorted(result_list):
    print(s)
