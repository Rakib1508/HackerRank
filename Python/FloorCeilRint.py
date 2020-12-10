import numpy

numpy.set_printoptions(sign=' ')

numbers = numpy.array(input().split(), float)
print(numpy.floor(numbers))
print(numpy.ceil(numbers))
print(numpy.rint(numbers))
