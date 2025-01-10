"""
Оформите решение 5 любых задач из прошлых домашних работ в функции и поместите их модуль task1_functions.py.
Напишите функцию runner и определите ее поведение в зависимости от переданных аргументов
runner() – все функции из task1_functions вызываются по очереди
runner(‘func_name’) – вызывается только функцию с именем func_name.
Runner(‘func_1’, ‘func_2’...) - вызывает все переданные функции
"""


def cubes_of_numbers() -> dict:
    """
    Создает и возвращает словарь с помощью генератора словарей.
    Ключи: числа от 1 до 20, значения: кубы этих чисел.
    """
    return {number: number**3 for number in range(1, 21)}


def unique_one(list1: list[int], list2: list[int]) -> int:
    """
    Из двух заданных списков чисел, функция считает.
    Сколько различных чисел содержится одновременно как в первом списке, так и во втором.
    """
    return len(set(list1) & set(list2))


def count_words(text: str) -> int:
    """Функция считает, сколько различных слов содержится во введенном тексте."""
    return len(set(text.split()))


def count_number_of_pairs(list_of_numbers: list[int]) -> int:
    """Функция считает, сколько в данном списке чисел пар элементов, равных друг другу."""
    return sum(
        (list_of_numbers.count(number) * (list_of_numbers.count(number) - 1)) // 2
        for number in set(list_of_numbers)
    )


def longest_word(my_string: str) -> str:
    """Находит самое длинное слово во введенном предложении."""
    marks = '.,!?-‘“”'
    words = ''.join(word for word in my_string if word not in marks).split()
    return f'Самое длинное слово - {max(words, key=len)}'
