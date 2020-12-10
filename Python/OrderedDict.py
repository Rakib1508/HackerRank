from collections import OrderedDict

number_of_items = int(input())
item_list = OrderedDict()
for i in range(number_of_items):
    line = input().split()
    v = int(line[-1])
    k = ' '.join(line[:-1])
    if k not in item_list:
        item_list[k] = int(v)
    else:
        item_list[k] += v

for k, v in item_list.items():
    print(k, v)
