"""
Языки.
Каждый из N школьников некоторой школы знает M языков. Определите:
1) какие языки знают все школьники и языки
2) какие языки знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
Пример:
Введите количество школьников: 3
Введите количество языков для 1-го школьника: 1
Введите 1-й язык для 1-го школьника: Russian
Введите количество языков для 2-го школьника:2
Введите 1-й язык для 2-го школьника: Russian
Введите 2-й язык для 2-го школьника: Belarusian
Введите количество языков для 3-го школьника: 1
Введите 1-й язык для 3-го школьника: Chinese
Все школьники знают 0 язык(-а/ов):
Хотя бы один из школьников знает 1 из 3 язык (-а/ов):
Belarusian
Chinese
Russian
"""
all_languages = []
number_of_students = int(input('Введите количество школьников: '))
for each_student in range(1, number_of_students + 1):
    number_of_languages = int(input(f'Введите количество языков для {each_student}-го школьника: '))
    each_student_languages = set()
    for each_language in range(1, number_of_languages + 1):
        which_languages = input(f'Введите {each_language}-й язык для {each_student}-го школьника: ')
        each_student_languages.add(which_languages)
    all_languages.append(each_student_languages)
print(all_languages)
common_languages = all_languages[0]
for com_languages in all_languages[1:]:
    common_languages &= com_languages
print(f'Все школьники знают {len(common_languages)} язык(-а/ов): ')
for com_lang in common_languages:
    print(com_lang)
any_languages = all_languages[0]
for an_languages in all_languages[1:]:
    any_languages |= an_languages
print(f'Хотя бы один из школьников знает 1 из {len(any_languages)} язык (-а/ов): ')
for any_lang in any_languages:
    print(any_lang)
