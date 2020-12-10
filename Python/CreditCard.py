import re

formats = re.compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]'
    r'\d{3}'
    r'(?:-?\d{4}){3}'
    r'$'
)

for _ in range(int(input())):
    credit_card = input().strip()
    print('Valid' if formats.search(credit_card) else 'Invalid')
