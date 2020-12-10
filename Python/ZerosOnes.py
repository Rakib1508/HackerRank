import numpy

constraint = tuple(map(int, input().split()))
print(numpy.zeros(constraint, dtype=int))
print(numpy.ones(constraint, dtype=int))
