import numpy

numbers = numpy.array(input().split(), float)
print(numpy.polyval(numbers, float(input())))
