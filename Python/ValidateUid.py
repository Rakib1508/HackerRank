def ID_checker(string):
    count_upper = 0
    count_digit = 0
    for i in range(len(string)):
        if string[i].isupper():
            count_upper += 1
        if string[i].isdigit():
            count_digit += 1
    
    if len(string) == 10 and len(string) == len(set(string)) and string.isalnum() and count_upper > 1 and count_digit > 2:
        print('Valid')
    else:
        print('Invalid')


for _ in range(int(input())):
    ID = input().strip()
    ID_checker(ID)
