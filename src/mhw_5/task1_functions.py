def func_1():
    """Return the total amount."""
    rubl = int(input('Введите рубли: '))
    cent = int(input('Введите копейки: '))
    product = int(input('Введите количество товара: '))

    total_price = (rubl * 100 + cent) * product
    print(f'Общая цена: {total_price // 100} рублей, {total_price % 100} копеек')


def func_2():
    """Return the longest word in the entered sentence."""
    chars = ['!', '?', ',', '.', ':', ';', '-', '"']
    my_string = input('Введите предложение: ')

    for symbol in chars:
        my_string = my_string.replace(symbol, ' ')

    words = (my_string.split(' '))

    longest_word = ''
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word

    print(f'Самое длинное слово: {longest_word}')


def func_3():
    """Return a string with duplicate characters and spaces removed."""
    text = input('Введите строку: ')
    result = ''

    for symbol in text:
        if symbol not in result and symbol != ' ':
            result += symbol
    print(result)


def func_4():
    """Return the number of lowercase and uppercase letters in the input string."""
    text = input('Введите строку: ')
    lower = 0
    upper = 0

    for symbol in text:
        if 'a' <= symbol <= 'z':
            lower += 1
        elif 'A' <= symbol <= 'Z':
            upper += 1

    print(f'Маленькие буквы: {lower}')
    print(f'Большие буквы: {upper}')


def func_5():
    """Return the nth Fibonacci number."""
    number_fibonacci = int(input('Введите n: '))

    if number_fibonacci == 1:
        print(0)
    elif number_fibonacci == 2:
        print(1)
    else:
        first_number, second_number = 0, 1
        for _ in range(number_fibonacci - 1):
            first_number, second_number = second_number, first_number + second_number

        print(first_number)
