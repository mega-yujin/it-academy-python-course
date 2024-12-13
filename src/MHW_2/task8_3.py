"""
Simple
Roman Numerals
For this task, you should return a Roman numeral using the specified integer value ranging from 1 to 3999.
"""


def checkio(data: int) -> str:
    roman_numerals = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]
    result = ""
    for roman, value in roman_numerals:
        while data >= value:
            result += roman
            data -= value

    return result
