import numpy

n, m = map(int, input().split())
array = []

for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

matrix = numpy.array(array)
print(numpy.mean(matrix, axis=1))
print(numpy.var(matrix, axis=0))
print(numpy.around(numpy.std(matrix), 11))
