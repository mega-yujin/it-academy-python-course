"""
    Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz.
    Вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.
"""

for numbers in range(1, 101):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print('FizzBuzz')
    elif numbers % 3 == 0:
        print('Fizz')
    elif numbers % 5 == 0:
        print('Buzz')
    else:
        print(numbers)
