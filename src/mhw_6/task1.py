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

    def expand(self, value):
        self.capacity += value
        self.budget -= value * 5

    def info(self):
        print(f'{self.name} has ${self.budget}, {self.capacity}, {self.goods_amount}')


class Good:

    def __init__(self, name, price, store: Store, amount):
        self.name = name
        self.price = price
        self.store = store
        self.store.goods_amount += amount

    def replenish(self, amount):
        if (self.store.capacity - self.store.goods_amount >= amount
                and self.store.budget >= self.price * 2 * amount):
            self.store.goods_amount += amount
            self.store.budget -= self.price * 2 * amount

    def sell(self, amount):
        if self.store.goods_amount >= amount:
            self.store.goods_amount -= amount
            self.store.budget += self.price * 3 * amount


if __name__ == '__main__':
    santa = Store('Santa', 100, 25)
    fish = Good('Fish', 20, santa, 5)
    actions = ['Expand store\n',
               'Store Info\n',
               'Sell good\n',
               'Replenish good\n',
               'Good info\n',
               'Finish\n',
               ]

    finish = False
    while not finish:
        print(''.join(actions))
        match input('What to do: '):
            case 'Expand store':
                santa.expand(int(input('How much: ')))
            case 'Store info':
                santa.info()
            case 'Sell good':
                fish.sell(int(input('How much: ')))
            case 'Replenish good':
                fish.replenish(int(input('How much: ')))
            case 'Finish':
                finish = True
