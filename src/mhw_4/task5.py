""" Каждый из N школьников некоторой школы знает M языков. Определите:
1) какие языки знают все школьники и языки
2) какие языки знает хотя бы один из школьников.
"""
n = int(input("Введите количество школьников: "))
students_languages = []

for _ in range(N):
    M = int(input())
    languages = set()
    for _ in range(M):
        languages.update(input().split())
    students_languages.append(languages)

all_known_languages = set.intersection(*students_languages)

any_known_language = set.union(*students_languages)

print("Языки, которые знают все школьники:", ', '.join(all_known_languages))
print("Языки, которые знает хотя бы один школьник:", ', '.join(any_known_language))