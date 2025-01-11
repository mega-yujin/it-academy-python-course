"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле /data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет - необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла:
top250_movies.txt – названия файлов
ratings.txt – гистограмма рейтингов
years.txt – гистограмма годов.
Задачу поместите в файл task4.py в папке src/hmw_5.
Подсказки:
Гистограмма - распределение значений. Пример гистограммы годов:
1986: 5
1987: 3
1995: 10
1998: 6
Такие данные и надо сохранить в файл.
Если есть желание можно сохранить гистограмму в графическом виде. Для этого подходит библиотека matplotlib.
"""


def process_movie_line(line, ratings, years):
    """Обрабатывает одну строку данных, извлекая рейтинг и год."""
    parts = line.split()

    rating = parts[2]
    ratings[rating] = ratings.get(rating, 0) + 1

    year = parts[-1][1:-1]
    years[year] = years.get(year, 0) + 1


def write_histogram(file, data):
    """Записывает гистограмму данных в файл."""
    for key, value in sorted(data.items()):
        file.write(f'{key}: {value}\n')


def process_top_movies(file, ratings, years):
    """Обрабатывает файл, извлекает 250 фильмов, рейтинг и год."""
    top_movies = []
    movies = 0
    found = False
    for line in file:
        if 'The Shawshank Redemption' in line:
            found = True
        if found:
            parts = line.split()
            top_movies.append(' '.join(parts[3:-1]))
            process_movie_line(line, ratings, years)
            movies += 1
        if movies == 250:
            break
    return top_movies


def write_to_files(top_movies, ratings, years):
    """Записывает данные в соответствующие файлы."""
    with open('data_hw5/top250_movies.txt', 'w') as file_names:
        for title in top_movies:
            file_names.write(f'{title}\n')

    with open('data_hw5/ratings.txt', 'w') as file_ratings:
        write_histogram(file_ratings, ratings)

    with open('data_hw5/years.txt', 'w') as file_years:
        write_histogram(file_years, years)


def process_file():
    """Обрабатывает файл ratings.list и записывает результаты в файлы."""
    ratings = {}
    years = {}

    try:
        with open('data_hw5/ratings.list', 'r') as file:
            top_movies = process_top_movies(file, ratings, years)
    except FileNotFoundError:
        print('Файл ratings.list не найден')
        return

    write_to_files(top_movies, ratings, years)


def main():
    """Главная функция, запускающая обработку файла."""
    process_file()


if __name__ == '__main__':
    main()
