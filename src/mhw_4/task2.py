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


def cities(data: dict[str, list[str]], num: int) -> str:
    """
    Return the num cities and their countries in order.

    Args:
        data: dict[str, list[str]]: Countries and their cities.
        num: int: Amount of cities.

    Returns:
        Num cities and their countries.
    """
    answer = []
    for country_1, cities_1 in data.items():
        for city_1 in cities_1:
            if num <= 0:
                return ''.join(answer)
            answer.append(f'{city_1}: {country_1} \n')
            num -= 1

    return ''.join(answer)


def cities2(data: dict[str, list[str]], num: int) -> str:
    """
    Return the num cities and their countries in order.

    Args:
        data (dict[str, list[str]]): Countries and their cities.
        num (int): Amount of cities.

    Returns:
        Num cities and their countries.
    """
    return '\n'.join([
        f'{city_2}: {country_2}'
        for country_2, cities_2 in data.items()
        for city_2 in cities_2
        ][:num],
        )


if __name__ == '__main__':
    print(cities(
        {
            'Italy': ['Rome', 'Florence'],
            'Russia': ['Moscow', 'Kursk', 'Vladivostok'],
        },
        3,
    ))

    print(cities2(
        {
            'Italy': ['Rome', 'Florence'],
            'Russia': ['Moscow', 'Kursk', 'Vladivostok'],
        },
        3,
    ))
