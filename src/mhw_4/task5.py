"""Языки.
Каждый из N школьников некоторой школы знает M языков. Определите:
1) какие языки знают все школьники
2) какие языки знает хотя бы один из школьников.
Входные данные
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
"""

stud = int(input('Введите количество школьников: '))
lang_all = None
lang_any = set()
for _ in range(stud):
    mi = int(input('Введите количество языков для школьника: '))
    cur_lang = set(input('Введите язык: ') for _ in range(mi))
    lang_any.update(cur_lang)
    if lang_all is None:
        lang_all = cur_lang
    else:
        lang_all.intersection_update(cur_lang)
lang_all = ','.join(lang_all)
lang_any = ','.join(lang_any)
print("Языки, которые знают все школьники:", lang_all)
print("Языки, которые знает хотя бы один школьник:", lang_any)
