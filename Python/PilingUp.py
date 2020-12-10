result = []
for _ in range(int(input())):
    string = 'Yes'
    number_of_cubes = int(input())
    sides = list(map(int, input().split()))
    
    m = sides.index(min(sides))
    right = sides[m+1:]
    left = sides[:m]
    
    if not (left == sorted(left, reverse = True) and right == sorted(right)):
        string = 'No'
    
    result.append(string)
    
[print(item) for item in result]
