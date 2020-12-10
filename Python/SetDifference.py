eng_students = int(input())
eng_student_rolls = set(map(int, input().split()))
fr_students = int(input())
fr_student_rolls = set(map(int, input().split()))

print(len(eng_student_rolls.difference(fr_student_rolls)))
