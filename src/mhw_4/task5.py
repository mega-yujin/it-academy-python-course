"""
5.
Каждый из N школьников некоторой школы знает M языков. Определите:
1) какие языки знают все школьники и языки
2) какие языки знает хотя бы один из школьников.
Входные данные:
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
"""


def get_students_languages(count_students):
    """Return the languages that schoolchildren know."""
    students_languages = []
    for num1 in range(count_students):
        count_languages = int(input(f'Введите количество языков, которые знает школьник {num1 + 1}: '))
        languages = set()
        for num2 in range(count_languages):
            language = input(f'Введите {num2 + 1}-й язык для {num1 + 1}-ого школьника: ')
            languages.add(language.strip())
        students_languages.append(languages)
    return students_languages


count_students = int(input('Введите количество школьников: '))
students_languages = get_students_languages(count_students)
common_languages = set.intersection(*students_languages)
all_languages = set.union(*students_languages)

if common_languages:
    print(f'Языки, которые знают все школьники: {", ".join(common_languages)}')
else:
    print('Нет языков, которые знают все школьники.')
print(f'Языки, которые знает хотя бы один школьник: {", ".join(all_languages)}')
