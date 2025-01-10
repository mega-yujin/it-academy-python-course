"""
Оформите решение 5 любых задач из прошлых домашних работ в функции и поместите их модуль task1_functions.py.
Напишите функцию runner и определите ее поведение в зависимости от переданных аргументов
runner() – все функции из task1_functions вызываются по очереди
runner(‘func_name’) – вызывается только функцию с именем func_name.
Runner(‘func_1’, ‘func_2’...) - вызывает все переданные функции
Подсказки:
функция callable(obj) возвращает True если передаваемый объект можно вызвать(например если это функция)
функция dir(obj) возвращает список всех атрибутов передаваемого объекта
функция getattr(obj, name) возвращает атрибут с именем name объекта obj. Если он отсутствует - значение по-умолчанию.
модуль - это тоже объект!!!
"""
import task1_functions


def get_all_functions():
    """Возвращает все доступные функции из модуля task1_functions."""
    return {
        name: getattr(task1_functions, name)
        for name in dir(task1_functions)
        if callable(getattr(task1_functions, name))
    }


def execute_function(func_name, *args):
    """Исполняет функцию по имени с передачей аргументов."""
    all_functions = get_all_functions()

    if func_name in all_functions:
        func = all_functions[func_name]
        return func(*args)
    print(f'Функция {func_name} не найдена.')
    return None


def execute_all_functions():
    """Вызывает все функции из модуля task1_functions."""
    all_functions = get_all_functions()
    for func in all_functions.values():
        print(func())


def execute_selected_functions(*args):
    """Вызывает выбранные функции из модуля task1_functions с аргументами."""
    all_functions = get_all_functions()

    for item in args:
        if isinstance(item, str) and item in all_functions:
            print(execute_function(item))
        elif isinstance(item, tuple) and len(item) > 1:
            func_name = item[0]
            func_args = item[1:]
            print(execute_function(func_name, *func_args))


def runner(*args):
    """Запускает функции с их аргументами."""
    if args:
        execute_selected_functions(*args)
    else:
        execute_all_functions()


if __name__ == '__main__':
    runner('cubes_of_numbers')
    runner(('unique_one', [1, 2, 3, 4, 3, 5, 6, 7, 8], [4, 6, 5, 7, 8, 9, 10, 11, 9, 12]))
    runner(('count_words', input('Введите текст: ')))
    runner(('count_number_of_pairs', list(map(int, input('Введите числа через пробел: ').split()))))
    runner(('longest_word', input('Введите предложение ')))
