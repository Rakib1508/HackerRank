count, initial = int(input()), set(map(int, input().split()))
for _ in range(int(input())):
    command = input().split()
    next_set = set(map(int, input().split()))
    command = command[0]
    if command == 'update':
        initial.update(next_set)
    elif command == 'intersection_update':
        initial.intersection_update(next_set)
    elif command == 'symmetric_difference_update':
        initial.symmetric_difference_update(next_set)
    elif command == 'difference_update':
        initial.difference_update(next_set)
        
print(sum(initial))
