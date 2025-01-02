"""Города.
Дано:
1)Список стран и городов каждой страны.
2)Названия городов.

Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N.
Далее идет N строк, каждая строка начинается с названия страны,
затем идут названия городов этой страны.
В следующей строке записано число M, далее идут M
запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
"""


def cities(data: dict[str, list[str]], wanted: list) -> str:
    """
    Return the num cities and their countries in order.

    Args:
        data (dict[str, list[str]]): Countries and their cities.
        wanted (list): Cities to return.

    Returns:
        Cities and their countries.
    """
    answer = []
    for country_1, cities_1 in data.items():
        for city_1 in cities_1:
            if city_1 in wanted:
                answer.append(f'{city_1}: {country_1} \n')

    return ''.join(answer)


def cities2(data: dict[str, list[str]], wanted: list) -> str:
    """
    Return the num cities and their countries in order.

    Args:
        data (dict[str, list[str]]): Countries and their cities.
        wanted (list): Cities to return.

    Returns:
        Cities and their countries.
    """
    return '\n'.join([
        f'{city_2}: {country_2}'
        for country_2, cities_2 in data.items()
        for city_2 in cities_2
        if city_2 in wanted
    ],
    )


places = {}
for country_num in range(int(input('Введите кол-во стран: '))):
    place = input(f'Введите страну {country_num + 1} и ее города: ').split()
    places[place[0]] = place[1:]

wanted_inp = []
for city_num in range(int(input('Введите кол-во городов: '))):
    wanted_inp.append(input(f'Введите город {city_num + 1}: '))

if __name__ == '__main__':
    print(cities(
        places,
        wanted_inp,
    ))

    print(cities2(
        places,
        wanted_inp,
    ))
