width, length = map(int, input().split())
design = '.|.'
title = 'WELCOME'

for i in range(1, width, 2):
    line_design = i * design
    print(line_design.center(length, '-'))

print(title.center(length, '-'))

for j in range(width-2, -1, -2):
    line_design = j * design
    print(line_design.center(length, '-'))
