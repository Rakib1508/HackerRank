number_of_commands = int(input())
my_list = []
for count in range(number_of_commands):
    command, *arg = input().split()
    arguments = list(map(int, arg))
    if command == 'insert':
        my_list.insert(arguments[0], arguments[1])
    elif command == 'print':
        print(my_list)
    elif command == 'remove':
        my_list.remove(arguments[0])
    elif command == 'append':
        my_list.append(arguments[0])
    elif command == 'sort':
        my_list = sorted(my_list)
    elif command == 'pop':
        my_list.pop()
    elif command == 'reverse':
        my_list.reverse()
