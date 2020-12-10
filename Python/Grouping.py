import re

string = input().strip()
item = re.search(r'([a-zA-Z0-9])\1+', string)
print(item.group(1) if item else -1)
