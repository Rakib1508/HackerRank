result = []
grades = []
for i in range(int(input())):
    name = str(input())
    num = float(input())
    result.append([name, num])
    grades.append(num)
tool = sorted(list(set(grades)))
final = []
for c in range(len(result)):
    if result[c][1] == tool[1]:
        final.append(result[c][0])
for name in sorted(final):
    print(name)
