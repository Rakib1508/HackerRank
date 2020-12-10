result = []
for _ in range(int(input())):
    f_count = int(input())
    first = set(map(int, input().split()))
    s_count = int(input())
    second = set(map(int, input().split()))
    result.append(first.issubset(second))
    
[print(item) for item in result]
