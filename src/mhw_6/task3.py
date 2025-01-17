"""
3.
Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами.
Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама.
"""
import unittest

from task3_function import count_pairs


class TestCountPairs(unittest.TestCase):
    """Тесты для функции count_pairs."""

    def test_empty_list(self):
        """Проверяет, что функция возвращает 0 для пустого списка."""
        self.assertEqual(count_pairs([]), 0)

    def test_no_pairs(self):
        """Проверяет, что функция возвращает 0, если в списке нет пар."""
        self.assertEqual(count_pairs([1, 2, 3, 4]), 0)

    def test_one_pair(self):
        """Проверяет, что функция правильно считает одну пару."""
        self.assertEqual(count_pairs([1, 1]), 1)

    def test_multiple_pairs(self):
        """Проверяет, что функция правильно считает несколько пар."""
        self.assertEqual(count_pairs([1, 1, 2, 2, 3]), 2)

    def test_more_than_two_pairs(self):
        """Проверяет, что функция правильно считает количество пар, когда есть более двух одинаковых элементов."""
        self.assertEqual(count_pairs([1, 1, 1, 2, 2, 3]), 4)


if __name__ == '__main__':
    unittest.main()
