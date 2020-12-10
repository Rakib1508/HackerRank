import cmath

r = complex(input())

radius = cmath.polar(r)[0]
angle = cmath.polar(r)[1]

print(radius)
print(angle)
