def func_1():
    return {key: key**3 for key in range(1, 21)}


def func_2():
    list1 = [1, 2, 3, 4, 3, 5, 6, 7, 8]
    list2 = [4, 6, 5, 7, 8, 9, 10, 11, 9, 12]
    return (len(set(list1) & set(list2)))


def func_3 ():
    list1 = [1, 2, 3, 4, 3, 5, 6, 7, 8]
    list2 = [4, 6, 5, 7, 8, 9, 10, 11, 9, 12]
    return (len(set(list1) ^ set(list2)))


def func_4():
    import re
    some_text = input('Введите текст:')
    new_text = re.split('[,;!?: ]', some_text)
    filtered_text = list(filter(None, new_text))
    return (len(set(filtered_text)))


def func_5():
    numbers = [0, 1, 0, 45, 0, 2, -3, 0, 4, 0, -6]
    for ind in numbers:
        if ind == 0:
            numbers.append(ind)
            numbers.remove(ind)
    return numbers
