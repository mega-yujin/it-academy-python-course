"""
Города.
Дано:
1) Список стран и городов каждой страны.
2) Названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Пример:
Введите количество стран: 2
Введите страну 1 и ее города: Belarus Minsk Grodno
Введите страну 2 и ее города: USA Chicago Philadelphia
Введите количество городов: з
Введите город 1: Minsk
Вверите город 2: Grodno
Введите город 3： Chicago
Ответ：
Minsk: Belarus
Grodno: Belarus
Chicago: USA
Учтите, что города с одинаковыми названиями могут быть в двух странах!
"""
number_of_countries = int(input('Введите количество стран: '))
countries_and_cities = {}
cities = []
for each_country in range(1, number_of_countries + 1):
    list_countries_and_cities = list(
        input(f'Введите страну {each_country} и ее города: ').split(),
    )
    country = list_countries_and_cities.pop(0)
    countries_and_cities.setdefault(country, list_countries_and_cities)
number_of_cities = int(input('Введите количество городов: '))
for each_city in range(1, number_of_cities + 1):
    city = input(f'Введите город {each_city}: ')
    cities.append(city)
for element in cities:
    country = [country for country in countries_and_cities if element in countries_and_cities[country]]
    if country:
        print(f'{element}: {", ".join(country)}')
    else:
        print(f'{element}: не найдено')
