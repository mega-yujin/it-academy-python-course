"""Languages.

Каждый из N школьников некоторой школы знает M языков. Определите:
1) какие языки знают все школьники и языки
2) какие языки знает хотя бы один из школьников.
"""


def languages(students: list[set]):
    """
    Languages.
    Input number of students, then for each one number of
    languages they know, then those languages.
    Print how many language know all students, what language
    at least one of them knows.
    """
    all_languages = set()
    common_languages = None
    for student_languages in students:

        all_languages |= student_languages
        if common_languages is None:
            common_languages = student_languages
        else:
            common_languages &= student_languages
    result = f'Все школьники знают хотя {len(common_languages)} язык(-а/ов)\n'
    result = '{0}Хотя бы один из школьников знает 1 из '.format(result)
    result = '{0}{1} язык(-а/ов)\n'.format(result, len(all_languages))
    all_languages = list(all_languages)
    all_languages.sort()
    for language in all_languages:
        result = '{0}{1}\n'.format(result, language)
    return result


if __name__ == '__main__':
    print(languages([{'rus', 'eng', 'esp'}, {'rus', 'eng', 'ukr'}]))
    print(123)