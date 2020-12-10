from itertools import combinations_with_replacement as com

string, r = input().split()
result = list(com(sorted(string), int(r)))
for item in result:
    print(''.join(item))
