import numpy

n, m = map(int, input().split())
array = []
for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)
print(numpy.prod(numpy.sum(array, axis=0)))
