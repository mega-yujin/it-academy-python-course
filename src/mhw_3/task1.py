"""FizzBuzz.
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def fizzbuzz() -> str:
    return '\n'.join([
        'FizzBuzz' if not num % 3 and not num % 5 else
        'Fizz' if not num % 3 else
        'Buzz' if not num % 5 else
        str(num) for num in range(1, 101)
    ])


print(fizzbuzz())
