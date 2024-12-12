"""
1. Напишите программу, которая считает общую цену.
Вводится M рублей и N копеек цена, а также количество S товара
Посчитайте общую цену в рублях и копейках за L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
"""
ruble, kopeck, amount = map(int, input('Введите цену одного товара (рубли, копейки) и количество товаров через пробел: ').split())
total = ((ruble * 100 + kopeck) * amount)
print(f'Общая цена {total // 100} рублей {total % 100} копеек')
