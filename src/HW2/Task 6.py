num = int(input("Введите число: "))
if num < 0:
    is_palindrome = False
else:
    temp, reversed_num = num, 0
    while temp:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    is_palindrome = num == reversed_num

if is_palindrome:
    print(f"{num} является палиндромом.")
else:
    print(f"{num} не является палиндромом.")
