from itertools import combinations

num = int(input())
letters = list(map(str, input().split()))
tools = int(input())
things = list(combinations(letters, tools))

result = [item for item in things if 'a' in item]
print(len(result) / len(things))
