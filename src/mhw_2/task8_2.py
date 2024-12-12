"""Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...
shows the first 11 ugly numbers. By convention, 1 is included.
The numbers 7, 11, 13 are not ugly because they are prime.
The number 14 is not ugly because in its prime factor the 7 will come.
Write a program to find and print the N’th ugly number."""


def ugly_number(n: int) -> int:
    number = [0] * n
    number[0] = 1

    i2 = i3 = i5 = 0
    multiple_of2 = 2
    multiple_of3 = 3
    multiple_of5 = 5

    for index in range(1, n):
        # Chooses the minimal multiple
        number[index] = min(
            multiple_of2,
            multiple_of3,
            multiple_of5,
        )
        # Calculates the next multiple of the current minimal
        if number[index] == multiple_of2:
            # Serves to avoid multiplying wrong number e.g. 7
            i2 += 1
            multiple_of2 = number[i2] * 2
        if number[index] == multiple_of3:
            i3 += 1
            multiple_of3 = number[i3] * 3
        if number[index] == multiple_of5:
            i5 += 1
            multiple_of5 = number[i5] * 5
    return number[-1]


if __name__ == "__main__":
    print(ugly_number(int(input('Enter a number: '))))
