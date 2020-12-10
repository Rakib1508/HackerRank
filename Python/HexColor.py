import re

for _ in range(int(input())):
    line = input().strip()
    colors = re.findall(r'[\s:](#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})', line)
    if colors:
        print(*colors, sep='\n')
