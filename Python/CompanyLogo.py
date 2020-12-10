from collections import OrderedDict

company_name = input()
inventory = OrderedDict()
for item in sorted(company_name):
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1

result = {}
for k, v in sorted(inventory.items(), key = lambda item:item[1], reverse = True):
    result[k] = v
