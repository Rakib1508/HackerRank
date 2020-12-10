eng_number = int(input())
eng_students = list(map(int, input().split()))

fr_number = int(input())
fr_students = list(map(int, input().split()))

print(len(set(eng_students).union(set(fr_students))))
