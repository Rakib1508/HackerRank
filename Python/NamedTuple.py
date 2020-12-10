from collections import namedtuple
row, col = int(input()), namedtuple('student', input().split())
rows = [col(*input().split()) for i in range(row)]
print('%.2f' % (sum([int(student.MARKS) for student in rows]) / row))
