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


def top250_movies():
    """
    Put names of 250 top movies from file ratings.list to
    file top250_movies.txt
    """
    allow = False
    with open('data_hw5/ratings.list', 'r') as file:
        with open('top250_movies.txt', 'w') as file2:
            for ind, line in enumerate(file):
                if 'New  Distribution  Votes  Rank' in line and not allow:
                    allow = True
                    continue
                if allow:
                    line_list = line.split()
                    file2.write(' '.join(line_list[3: -1]) + '\n')
                if 'BOTTOM 10 MOVIES (1500+ VOTES)' in line and allow:
                    break


def ratings():
    """
    Count ratings of 250 top movies from file ratings.list and put
    them to file ratings.txt
    """
    allow = False
    ratings_list = []
    checked = set()
    with open('data_hw5/ratings.list', 'r') as file:
        with open('ratings.txt', 'w') as file2:
            for ind, line in enumerate(file):
                if 'New  Distribution  Votes  Rank' in line and not allow:
                    allow = True
                    continue
                if allow:
                    ratings_list.append(line.split()[2])
                if len(ratings_list) == 250:
                    break
            ratings_list.sort()
            for rating in ratings_list:
                if rating not in checked:
                    ratings_list.count(rating)
                    file2.write(f'{rating}: {ratings_list.count(rating)}\n')
                    checked.add(rating)


def years():
    """
    Count release years of 250 top movies from file ratings.list
    and put them to file ratings.txt
    """
    allow = False
    years_list = []
    checked = set()
    with open('data_hw5/ratings.list', 'r') as file:
        with open('years.txt', 'w') as file2:
            for ind, line in enumerate(file):
                if 'New  Distribution  Votes  Rank' in line and not allow:
                    allow = True
                    continue
                if allow:
                    line = line.replace('(', '')
                    line = line.replace(')', '')
                    years_list.append(line.split()[-1])
                if len(years_list) == 250:
                    break
            years_list.sort()
            for year in years_list:
                if year not in checked:
                    years_list.count(year)
                    file2.write(f'{year}: {years_list.count(year)}\n')
                    checked.add(year)


top250_movies()
years()
ratings()
