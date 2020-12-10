from itertools import groupby

string = input()
series = []
for key, value in groupby(string):
    series.append(list(value))

for item in series:
    print('(' + str(len(item)) + ', ' + str(item[0]) + ')', end=' ')
