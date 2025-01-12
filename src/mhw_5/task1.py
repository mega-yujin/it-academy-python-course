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
    if args:
        for func_name in args:
            func = getattr(task1_functions, func_name, None)
            if func:
                func()
    else:
        module_attributes = dir(task1_functions)
        print(module_attributes)
        for attribute_name in module_attributes:
            print(attribute_name)
            attribute = getattr(task1_functions, attribute_name)
            print(attribute)
            if callable(attribute):
                attribute()


runner()
