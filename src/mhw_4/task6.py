"""
6.
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


def get_unique_words(text):
    """Return count unique words."""
    words = text.replace('\\n', ' ').split()  # noqa: WPS342
    unique_words = set(words)
    return len(unique_words)


text = input('Введите текст: ')
unique_word = get_unique_words(text)
