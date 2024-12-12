"""Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...
shows the first 11 ugly numbers. By convention, 1 is included.
The numbers 7, 11, 13 are not ugly because they are prime.
The number 14 is not ugly because in its prime factor the 7 will come.
Write a program to find and print the N’th ugly number.
"""


def ugly_number(num: int) -> int:
    """
    Find the Nth ugly number.

    Args:
        num (int): The position of the wanted ugly number.

    Returns:
        int: The Nth ugly number.
    """
    ugly_numbers = [0] * num
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

    return ugly_numbers[-1]


if __name__ == '__main__':
    print(ugly_number(int(input('Enter a number: '))))
