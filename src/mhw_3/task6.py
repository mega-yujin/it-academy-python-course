"""Упорядоченный список.
Дан список целых чисел. Требуется переместить все
ненулевые элементы в левую часть списка, не меняя их порядок,
а все нули - в правую часть. Порядок ненулевых элементов
изменять нельзя, дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""


def sorted_list(seq: list):
    """
    Sort list, transfer all zeroes to right end.

    Args:
        seq (list): List to sort.
    """
    sorted_seq = list(map(int, seq[:]))
    ind = 0
    length = len(sorted_seq)
    while ind < length:
        if sorted_seq[ind] == 0:
            # Pop a zero and add a new one in front
            sorted_seq.pop(ind)
            sorted_seq.append(0)
            length -= 1
        else:
            ind += 1
    print(sorted_seq)


def sorted_list2(seq2: list):
    """
    Sort list, transfer all zeroes to right end.

    Args:
        seq2 (list): List to sort.
    """
    sorted_seq2 = list(map(int, seq2[:]))
    non_zero_ind = 0
    for ind, elem in enumerate(sorted_seq2):
        if elem != 0:
            # Change place between a found non-zero and first known zero
            temp = sorted_seq2[non_zero_ind]
            sorted_seq2[non_zero_ind] = sorted_seq2[ind]
            sorted_seq2[ind] = temp
            non_zero_ind += 1

    print(sorted_seq2)


sorted_list(input('Введите последовательность: ').split())
sorted_list2(list(map(int, input('Введите последовательность: ').split())))
