"""Languages.

Каждый из N школьников некоторой школы знает M языков. Определите:
1) какие языки знают все школьники и языки
2) какие языки знает хотя бы один из школьников.
"""


def languages():
    """
    Languages.
    Input number of students, then for each one number of
    languages they know, then those languages.
    Print how many language know all students, what language
    at least one of them knows.
    """
    all_languages = set()
    common_languages = None
    student_amount = int(input('Введите количество школьников: '))

    for student in range(student_amount):
        languages_num = int(input(
            f'Введите количество языков для {student + 1}-го школьника: ',
        ))
        student_languages = {input(
            f'Введите {language + 1}-й язык для {student + 1}-го школьника: ',
        ) for language in range(languages_num)
        }

        all_languages |= student_languages
        if common_languages is None:
            common_languages = student_languages
        else:
            common_languages &= student_languages

    print(f'Все школьники знают хотя {len(common_languages)} язык(-а/ов)')
    print(
        'Хотя бы один из школьников знает 1 из ' +
        f'{len(all_languages)} язык(-а/ов)',
    )

    for language in all_languages:
        print(language)


if __name__ == '__main__':
    languages()
