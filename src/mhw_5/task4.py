"""Movies.
В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле. /data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет - необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла:
top250_movies.txt – названия файлов
ratings.txt – гистограмма рейтингов
years.txt – гистограмма годов.
"""


def find_beginning(func):
    def wrapper():
        allow = False
        result = []
        with open('data_hw5/ratings.list', 'r') as file:
            for ind, line in enumerate(file):
                if 'New  Distribution  Votes  Rank' in line and not allow:
                    allow = True
                    continue
                if allow:
                    line_list = line.split()
                    result.append(line_list[2:])
                if len(result) >= 250:
                    break
            func(result)
    return wrapper


@find_beginning
def top250_movies(result):
    """
    Put names of 250 top movies from file ratings.list to
    file top250_movies.txt
    """
    with open('top250_movies.txt', 'w') as file2:
        for title in result:
            file2.write(f'{" ".join(title[1: -1])}\n')


@find_beginning
def ratings(result):
    """
    Count ratings of 250 top movies from file ratings.list and put
    them to file ratings.txt
    """
    checked = set()
    with open('ratings.txt', 'w') as file2:
        for ind, element in enumerate(result):
            result[ind] = element[0]
        result.sort()
        for rating in result:
            if rating not in checked:
                result.count(rating)
                file2.write(f'{rating}: {result.count(rating)}\n')
                checked.add(rating)


@find_beginning
def years(result):
    """
    Count release years of 250 top movies from file ratings.list
    and put them to file ratings.txt
    """
    checked = set()
    with open('ratings.txt', 'w') as file2:
        for ind, element in enumerate(result):
            result[ind] = element[-1]
        result.sort()
        for year in result:
            if year not in checked:
                result.count(year)
                file2.write(f'{year}: {result.count(year)}\n')
                checked.add(year)


top250_movies()
years()
ratings()
