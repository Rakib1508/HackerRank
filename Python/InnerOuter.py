import numpy

a, b = (numpy.array(input().split(), int) for _ in range(2))
print(numpy.inner(a, b))
print(numpy.outer(a, b))
