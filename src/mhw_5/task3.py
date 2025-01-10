"""
3.
Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”.
"""


def get_ranges(numbers):
    """Return sorted and collapsed numbers."""
    ranges = []
    start = numbers[0]

    for index, _ in enumerate(numbers[1:], start=1):
        if numbers[index] != numbers[index - 1] + 1:
            if start == numbers[index - 1]:
                ranges.append(str(start))
            else:
                ranges.append(f'{start}-{numbers[index - 1]}')
            start = numbers[index]

    if start == numbers[-1]:
        ranges.append(str(start))
    else:
        ranges.append(f'{start}-{numbers[-1]}')

    return ','.join(ranges)


def main():
    """Return and displays the main result."""
    try:  # noqa: WPS229
        input_numbers = input('Введите числа через пробел: ')
        numbers = list(map(int, input_numbers.split(' ')))
        print(f'Результат: {get_ranges(sorted(set(numbers)))}')
    except ValueError:
        print('Список должен содержать числа!')
        main()


if __name__ == '__main__':
    main()
