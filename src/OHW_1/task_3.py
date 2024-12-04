month = int(input("Введите число: "))
if month < 1:
    print("значение слишком маленькое")
elif month > 12:
    print("значение слишком большое")
elif 3 <= month <= 5:
    print("весна")
elif 6 <= month <= 8:
    print("лето")
elif 9 <= month <= 11:
    print("осень")
else:
    print("зима")
