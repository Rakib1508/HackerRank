students, subject = map(int, input().split())
scores = list()
for _ in range(subject):
    sub_scores = list(map(float, input().split()))
    scores.append(sub_scores)

[print(sum(item)/len(item)) for item in zip(*scores)]
