"""Simulation.
Создайте модель из жизни. Это может быть бронирование
комнаты в отеле, покупка билета в транспортной компании,
заказ товаров на маркетплейсе или учет книг в библиотеке.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты, так и методы класса
для симуляции различных действий. Программа должна инстанцировать
объекты и эмулировать какую-либо ситуацию - вызывать
методы, взаимодействие объектов и т.д.
"""


class Store:
    def __init__(self, name, budget, capacity):
        self.name = name
        self.budget = budget
        self.capacity = capacity
        self.goods_amount = 0

    def expand(self):
        value = int(input('How much (1:5 price): '))
        self.capacity += value
        self.budget -= value * 5

    def info(self):
        print(f'{self.name} has ${self.budget}, {self.capacity}, {self.goods_amount}')


class Good:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.store = store
        self.amount = 0

    def replenish(self):
        amount = int(input('How much: '))
        if (self.store.capacity - self.store.goods_amount >= amount
                and self.store.budget >= self.price * amount):
            self.store.goods_amount += amount
            self.amount += amount
            self.store.budget -= self.price * amount
        else:
            print('Not enough money or storage')

    def sell(self):
        amount = int(input('How much: '))
        if self.amount >= amount:
            self.store.goods_amount -= amount
            self.amount -= amount
            self.store.budget += self.price * 1.5 * amount
        else:
            print('Not enough good')

    def info(self):
        print(f'{self.amount} {self.name} by ${self.price}')


def create_new_good():
    attributes = {}

    for attribute_name in good_attributes:
        entered_value = input(f'Enter {attribute_name}: ')
        try:
            attribute_value = int(entered_value)
        except ValueError:
            attribute_value = entered_value
        attributes[attribute_name] = attribute_value

    new_good_name = attributes['name']
    goods[new_good_name] = Good(**attributes)


def store_action():
    print(''.join(actions2))
    match input('What to do: '):
        case 'Expand':
            store.expand()
        case 'Info':
            store.info()
        case _:
            print('Wrong action')


def good_action():
    good_name = input('Which one: ')
    if good_name not in goods:
        print('No such good')
    print(''.join(actions3))
    match input('What to do: '):
        case 'Sell':
            goods[good_name].sell()
        case 'Replenish':
            goods[good_name].replenish()
        case 'Info':
            goods[good_name].info()
        case _:
            print('Wrong action')


if __name__ == '__main__':
    finish = False
    store = Store(input('What is store name?: '), 100, 25)
    good_attributes = [
        'name',
        'price',
    ]
    goods = {}
    actions1 = [
        '\nStore\n',
        'Good\n',
        'Add good\n',
        'Goods\n',
        'Finish\n'
    ]
    actions2 = [
        '\nExpand\n',
        'Info\n',
    ]
    actions3 = [
        '\nSell\n',
        'Replenish\n',
        'Info\n',
        'P.S. Selling is 1.5x price\n',
    ]

    while not finish:
        print(''.join(actions1))
        match input('What to do: '):
            case 'Store':
                store_action()
            case 'Good':
                good_action()
            case 'Add good':
                create_new_good()
            case 'Goods':
                print(goods.keys())
            case 'Finish':
                finish = True
            case _:
                print('Wrong action')
