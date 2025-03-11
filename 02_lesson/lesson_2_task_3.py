import math

def square(side):
    area = side ** 2
    return math.ceil(area)

side = 4
result = square(side)

print(f"Площадь квадрата со стороной {side}: {result}")