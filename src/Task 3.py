month = int(input("Введите номер месяца от 1 до 12:"))
if month < 1:
    result = "Значение слишком маленькое"
elif month > 12:
   result = "Значение слишком большое"
elif month in [12, 1, 2]:
   result = "зима"
elif month in [3, 4, 5]:
   result = "весна"
elif month in [6, 7, 8]:
   result = "лето"
elif month in [9, 10, 11]:
   result = "осень"
print("result")