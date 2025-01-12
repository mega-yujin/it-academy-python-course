"""
4.
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
a. Откройте и прочитайте файл(если его нет - необходимо вывести ошибку).
b. Найдите ТОП250 фильмов и извлеките заголовки.
c. Программа создает 3 файла:
- top250_movies.txt – названия файлов
- ratings.txt – гистограмма рейтингов
- years.txt – гистограмма годов.
"""


def parse_movie_data(line, rating_count, year_count):
    """Извлекает рейтинг и год из строки данных о фильме."""
    segments = line.split()

    movie_rating = segments[2]
    rating_count[movie_rating] = rating_count.get(movie_rating, 0) + 1

    release_year = segments[-1][1:-1]
    year_count[release_year] = year_count.get(release_year, 0) + 1


def save_histogram_to_file(output_file, data):
    """Сохраняет гистограмму в указанный файл."""
    for key, count in sorted(data.items()):
        output_file.write(f'{key}: {count}\n')


def extract_top_movies_from_file(input_file, rating_count, year_count):
    """Извлекает 250 лучших фильмов из файла, а также их рейтинг и год выпуска."""
    movie_titles = []
    movie_counter = 0
    movie_found = False

    for line in input_file:
        if 'New  Distribution  Votes  Rank  Title' in line:
            movie_found = True
            continue
        if movie_found:
            segments = line.split()
            movie_titles.append(' '.join(segments[3:-1]))
            parse_movie_data(line, rating_count, year_count)
            movie_counter += 1
        if movie_counter == 250:
            break
    return movie_titles


def save_data_to_files(movie_titles, rating_count, year_count):
    """Сохраняет названия фильмов, рейтинги и годы в соответствующие файлы."""
    with open('top250_movies.txt', 'w') as movies_file:
        for title in movie_titles:
            movies_file.write(f'{title}\n')

    with open('ratings.txt', 'w') as ratings_file:
        save_histogram_to_file(ratings_file, rating_count)

    with open('years.txt', 'w') as years_file:
        save_histogram_to_file(years_file, year_count)


def process_ratings_file():
    """Читает файл ratings.list и сохраняет результаты в файлы."""
    rating_count = {}
    year_count = {}

    try:
        with open('./data_hw5/ratings.list', 'r') as input_file:
            top_movies = extract_top_movies_from_file(input_file, rating_count, year_count)
    except FileNotFoundError:
        print('Файл не найден')
        return

    save_data_to_files(top_movies, rating_count, year_count)


if __name__ == '__main__':
    process_ratings_file()
