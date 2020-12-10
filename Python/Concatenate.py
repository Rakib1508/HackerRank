import numpy

n, m, p = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(n + m)]
print(numpy.array(numbers))
