import numpy

n, m = map(int, input().split())
array = []

for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

matrix = numpy.array(array)
print(max(numpy.min(matrix, axis=1)))
