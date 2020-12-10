eng_students = int(input())
eng_student_rolls = set(input().split())
fr_students = int(input())
fr_student_rolls = set(input().split())

print(len(eng_student_rolls.intersection(fr_student_rolls)))
