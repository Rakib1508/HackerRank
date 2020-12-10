from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result_list = list(product(a, b))
result_string = ''

for item in result_list:
    result_string += str(item) + ' '

print(result_string)
