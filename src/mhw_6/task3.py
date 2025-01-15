"""Testing.
Оформите указанную задачу из прошлых домашних в виде
функции и покройте тестами. Учтите, что в функцию могут
быть переданы некорректные значения, здесь может пригодиться
‘assertRaises’. Не нужно переделывать функцию для того
чтобы она ловила все возможные ситуации сама.
"""

import unittest
from task3_function import languages


class TestLanguagesFunc(unittest.TestCase):

    def test_empty_data(self):
        data = []
        with self.assertRaises(TypeError):
            languages(data)

    def test_wrong_type_data(self):
        data = [123, 234]
        with self.assertRaises(TypeError):
            languages(data)

    def test_2common_2different_languages(self):
        data = [{'rus', 'eng', 'esp'}, {'rus', 'eng', 'ukr'}]
        wanted = """Все школьники знают хотя 2 язык(-а/ов)
Хотя бы один из школьников знает 1 из 4 язык(-а/ов)
eng
esp
rus
ukr\n"""
        self.assertEqual(
            languages(data),
            wanted
        )

    def test_0common_3different_languages(self):
        data = [{'hin', 'tur'}, {'por'}]
        wanted = """Все школьники знают хотя 0 язык(-а/ов)
Хотя бы один из школьников знает 1 из 3 язык(-а/ов)
hin
por
tur\n"""
        self.assertEqual(
            languages(data),
            wanted
        )

    def test_3common_3different_languages(self):
        data = [{'ger', 'bel', 'chi'}, {'ger', 'bel', 'chi'}]
        wanted = """Все школьники знают хотя 3 язык(-а/ов)
Хотя бы один из школьников знает 1 из 3 язык(-а/ов)
bel
chi
ger\n"""
        self.assertEqual(
            languages(data),
            wanted
        )
