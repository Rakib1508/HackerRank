primary = set(map(int, input().split()))
result = []
for _ in range(int(input())):
    next_set = set(map(int, input().split()))
    if primary.issuperset(next_set):
        result.append('True')
    else:
        result.append('False')
        
if 'False' in result:
    print('False')
else:
    print('True')
