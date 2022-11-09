import math

a, b, c = 4, 4, 4
triangle_herons_formula = (a + b + c / 2)

print(triangle_herons_formula)

d = math.sqrt((a*2 - a*1)*2 + (b*2 - b*1)*2)
r = 3
h = 3
something_ = 1 / 3 + math.pi * math.pow(r, 2) * h
print(d)
print(something_)

