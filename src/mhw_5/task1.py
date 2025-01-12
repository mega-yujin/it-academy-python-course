"""
1.
Оформите решение 5 любых задач из прошлых домашних работ в функции и поместите их модуль task1_functions.py.
Напишите функцию runner и определите ее поведение в зависимости от переданных аргументов
a. runner() – все функции из task1_functions вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию с именем func_name.
c. runner(‘func_1’, ‘func_2’...) - вызывает все переданные функции
"""
import task1_functions


def runner(*args):
    """Return given functions."""
    if args:
        for func_name in args:
            func = getattr(task1_functions, func_name, None)
            if callable(func):
                func()
            else:
                print(f'Функция "{func_name}" не найдена.')

    else:
        for name_func in dir(task1_functions):
            func = getattr(task1_functions, name_func, None)
            if callable(func):
                func()


if __name__ == '__main__':
    runner()
    runner('func_1')
    runner('func_1', 'func_3', 'func_5')
    runner('func_6')
