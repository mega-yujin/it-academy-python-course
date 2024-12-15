"""FizzBuzz.
Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
"""


def fizzbuzz():
    """
    Print number from 1 to 100, if number divisible by 3 print
    'Fizz', if by 5 print 'Buzz', if by 3 and 5 print 'FizzBuzz'.
    """
    print('\n'.join([
        'FizzBuzz' if not num % 3 and not num % 5 else
        'Fizz' if not num % 3 else
        'Buzz' if not num % 5 else
        str(num) for num in range(1, 101)
    ]))


if __name__ == '__main__':
    fizzbuzz()
