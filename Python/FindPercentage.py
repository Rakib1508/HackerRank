n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
my_list = student_marks[query_name]
summation = 0
for num in my_list:
    summation += num
avg = float(summation) / len(my_list)
print('%.2f' % avg)
