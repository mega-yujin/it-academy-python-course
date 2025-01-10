def dict_comprehension_20() -> dict:
    """
    Create a dict with keys from 1 to 20, values are keys cubed.

    Returns:
         dict: Dictionary with keys from 1 to 20, values are keys cubed.
    """
    return {num: num ** 3 for num in range(1, 21)}


def all_the_same(elements: list[any]) -> bool:
    """
    Check if all elements in a sequence are equal.

    Args:
        elements (list[any]): Sequence to check.

    Returns:
        bool: True if uniform.
    """
    if len(set(elements)) <= 1:
        return True
    return False


def ugly_number() -> int:
    """
    Find the Nth ugly number.

    Returns:
        int: The Nth ugly number.
    """
    num = int(input('Enter a number: '))
    ugly_numbers = [0 for _ in range(num)]
    ugly_numbers[0] = 1

    i2 = 0
    i3 = 0
    i5 = 0
    multiple_of_2 = 2
    multiple_of_3 = 3
    multiple_of_5 = 5

    for index in range(1, num):
        # Choose the minimum of the multiples
        next_ugly_number = min(multiple_of_2, multiple_of_3, multiple_of_5)
        ugly_numbers[index] = next_ugly_number

        if next_ugly_number == multiple_of_2:
            i2 += 1
            multiple_of_2 = ugly_numbers[i2] * 2
        if next_ugly_number == multiple_of_3:
            i3 += 1
            multiple_of_3 = ugly_numbers[i3] * 3
        if next_ugly_number == multiple_of_5:
            i5 += 1
            multiple_of_5 = ugly_numbers[i5] * 5
    print(ugly_numbers[-1])
    return ugly_numbers[-1]


def find_fibonacci(number: int) -> int:
    """
    Calculate the nth Fibonacci number.

    Args:
        number (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if number == 1:
        return 0
    if number == 2:
        return 1

    f1, f2 = 0, 1
    for _ in range(number - 2):
        f1, f2 = f2, f1 + f2

    return f2


def fizzbuzz():
    """
    Print numbers from 1 to 100. If a number is divisible by 3, print 'Fizz'.
    If divisible by 5, print 'Buzz'. If divisible by both 3 and 5, print 'FizzBuzz'.
    """
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append('FizzBuzz')
        elif num % 3 == 0:
            result.append('Fizz')
        elif num % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(num))
    print('\n'.join(result))
