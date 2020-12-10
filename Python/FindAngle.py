from math import degrees, atan2

perpendicular = float(input())
base = float(input())

angle = int(round(degrees(atan2(perpendicular, base)), 0))
print(str(angle) + '°')
