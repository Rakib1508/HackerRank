case, numbers = int(input()), list(map(int, input().split()))
print(all(num > 0 for num in numbers) and any(str(num) == str(num)[::-1] for num in numbers))
