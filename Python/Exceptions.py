n = int(input())

for i in range(n):
    try:
        first_number, second_number = map(int, input().split(' '))
        print(first_number // second_number)
    except Exception as err:
        print('Error Code:', err)
