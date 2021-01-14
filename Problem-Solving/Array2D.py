array = list()
for i in range(6):
    array.append(list(map(int, input().split())))

sums = []
for a in range(len(array) - 2):
    for b in range(len(array) - 2):
        items = [array[a][b], array[a][b+1], array[a][b+2], array[a+1][b+1], array[a+2][b], array[a+2][b+1], array[a+2][b+2]]
        sums.append(sum(items))

print(max(sums))
