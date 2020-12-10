import re

for _ in range(int(input())):
    number = input().strip()
    if re.match(r'[789]\d{9}$', number):
        print('YES')
    else:
        print('NO')
