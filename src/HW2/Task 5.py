n = int(input("Введите число n: "))

if n <= 0:
    print("Пожалуйста, введите положительное целое число.")
else:
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    print(f"{n} число Фибоначчи: {b if n > 1 else n-1}")
