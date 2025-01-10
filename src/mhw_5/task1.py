"""Runner.
Напишите функцию runner и определите ее поведение в
зависимости от переданных аргументов
runner() – все функции из task1_functions вызываются по очереди
runner(‘func_name’) – вызывается только функцию с именем func_name.
runner(‘func_1’, ‘func_2’...) - вызывает все переданные функции
"""

import task1_functions


def runner(*args):
    """
    Run wanted functions from task1_functions.py.
    If none mentioned - run all.

    Args:
        args: Functions names.
    """
    for func_name in args:
        if hasattr(task1_functions, func_name):
            getattr(task1_functions, func_name)()
        else:
            print(f"Function {func_name} does not exist.")
    else:
        task1_functions.dict_comprehension_20()
        task1_functions.all_the_same(input().split())
        task1_functions.ugly_number()
        task1_functions.find_fibonacci(int(input()))
        task1_functions.fizzbuzz()


runner('fizzbuzz', 'ugly_number')
