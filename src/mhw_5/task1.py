"""Runner.
Оформите решение 5 любых задач из прошлых домашних работ в функции и поместите их модуль 
task1_functions.py.
Напишите функцию runner и определите ее поведение в зависимости от переданных аргументов
runner() – все функции из task1_functions вызываются по очереди
runner(‘func_name’) – вызывается только функцию с именем func_name.
runner(‘func_1’, ‘func_2’...) - вызывает все переданные функции
Задачу поместите в файл task1.py в папке src/mhw_5.
"""

import task1_functions

def runner(*args):
    if args:
        for func_name in args:
            func = getattr(task1_functions, func_name)
            if callable(func):
                func()
    else:
        task1_functions.func_1()
        task1_functions.func_2()
        task1_functions.func_3()
        task1_functions.func_4()
        task1_functions.func_5()

runner()
runner('func_1')
runner('func_1', 'func_3', 'func_5')
