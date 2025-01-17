"""
Оформите указанную задачу из прошлых домашних в виде функции и покройте тестами.
Учтите, что в функцию могут быть переданы некорректные значения, здесь может пригодиться ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные ситуации сама.
"""
import unittest

from nastya_tsykunova.src.MHW_5.task4 import process_top_movies


class TestProcessMovies(unittest.TestCase):
    """Класс для тестирования функции process_top_movies."""

    def test_empty_data(self):
        """Проверяет, что пустой файл вызывает исключения."""
        empty_file = []
        ratings = {}
        years = {}
        result = process_top_movies(empty_file, ratings, years)
        self.assertEqual(result, [])

    def test_incorrect_data_format(self):
        """Проверяет, что некорректные строки не вызывают исключений и игнорируются."""
        incorrect_file = ['Incorrect line']
        ratings = {}
        years = {}
        result = process_top_movies(incorrect_file, ratings, years)
        self.assertEqual(result, [])

    def test_find_necessary(self):
        """Проверяет, что корректные данные обрабатываются."""
        file = ['Incorrect line', '      0000000125  1888533   9.2  The Shawshank Redemption (1994)']
        ratings = {}
        years = {}
        result = process_top_movies(file, ratings, years)
        self.assertEqual(result, ['The Shawshank Redemption'])

    def test_limit_to_250_movies(self):
        """Проверяет, что функция обрабатывает не более 250 фильмов."""
        file = [
            '      0000000125  1888533   9.2  The Shawshank Redemption (1994)',
        ] + [
            f'      0000000125  1888533   8.0  Film {number} (2000)'
            for number in range(1, 251)
        ]
        ratings = {}
        years = {}
        result = process_top_movies(file, ratings, years)
        self.assertEqual(len(result), 250)

    def test_file_not_string(self):
        """Проверка, что будет ошибка, если в функцию передать не строковый тип данных."""
        with self.assertRaises(TypeError):
            process_top_movies(123, {}, {})
