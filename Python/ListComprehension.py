from itertools import permutations

x = int(input())
y = int(input())
z = int(input())
n = int(input())

all_coordinates = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            all_coordinates.append([i, j, k])

final = [item for item in all_coordinates if item[0]+item[1]+item[2] != n]
print(final)
