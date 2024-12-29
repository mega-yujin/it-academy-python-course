"""
2.
Дано:
1)  Список стран и городов каждой страны.
2)  Названия городов.

Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
"""


def country_and_city():
    """Return which country the city belongs to."""
    count_country = int(input('Введите количество стран: '))
    country_city_map = {}
    count = 1

    for _ in range(count_country):
        data = input(f'Введите страну {count} и ее города: ').split()
        country = data[0]
        cities = data[1:]
        count += 1
        for city in cities:
            if city not in country_city_map:
                country_city_map[city] = []
            country_city_map[city].append(country)

    number_requests = int(input('Введите количество городов: '))
    count = 1
    for _ in range(number_requests):
        city_query = input(f'Введите название города {count}: ')
        count += 1
        if city_query in country_city_map:
            countries = country_city_map[city_query]
            print(f'ответ:\n {city_query}: {", ".join(countries)}')
        else:
            print('Город не найден')


if __name__ == '__main__':
    country_and_city()
