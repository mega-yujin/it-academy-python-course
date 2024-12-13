import math

a = float(input("Длина стороны a: "))
b = float(input("Длина стороны b: "))
c = float(input("Длина стороны c: "))

if a + b > c and a + c > b and b + c > a:
    height = (2 / a) * math.sqrt(s * (s - a) * (s - b) * (s - c))
    area = 0.5 * b * height
    print(f"Площадь равна {area:.2f}")
else:
    print("Треугольник с такими сторонами не существует")
