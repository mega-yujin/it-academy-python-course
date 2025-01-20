"""
1.
Создайте  модель из жизни.
Это может быть бронирование комнаты в отеле, покупка билета в транспортной компании,
заказ товаров на маркетплейсе или учет книг в библиотеке.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
"""


class TicketMachine:
    """Класс, представляющий автомат по продаже билетов."""

    def __init__(self):
        """Инициализация автомата по продаже билетов."""
        self.bus_ticket_price = 100
        self.train_ticket_price = 150
        self.plain_ticket_price = 200

    def buying_ticket(self, name, balance, transport):
        """Метод для покупки билета."""
        ticket_price = self.get_ticket_price(transport)

        if ticket_price is None:
            print('Неверный тип транспорта.')
            return False

        if self.check_balance(balance, ticket_price):
            balance -= ticket_price
            print(f'{name} купил(-a) билет на {transport} за {ticket_price} рублей.')
            return balance
        else:
            print(f'{name} не хватает средств для покупки билета на {transport}.')

    def check_balance(self, balance, ticket_price):
        """Проверка, достаточно ли средств для покупки билета."""
        return balance >= ticket_price

    def get_ticket_price(self, transport):
        """Получение цены билета в зависимости от типа транспорта."""
        if transport == 'bus':
            return self.bus_ticket_price
        elif transport == 'train':
            return self.train_ticket_price
        elif transport == 'plain':
            return self.plain_ticket_price
        return None


class Passenger:
    """Класс, представляющий пассажира."""

    def __init__(self, name: str, balance: int, transport: str):
        """Инициализация пассажира с именем, балансом и желаемым видом транспорта."""
        self.name = name
        self.balance = balance
        self.transport = transport

    def buy_ticket(self, ticket_machine: TicketMachine):
        """Метод для покупки билета через автомат."""
        new_balance = ticket_machine.buying_ticket(self.name, self.balance, self.transport)
        if new_balance is not None:
            self.balance = new_balance

    def check_balance(self):
        """Метод для отображения текущего баланса пассажира."""
        print(f'Ваш баланс: {self.balance}')

    def add_balance(self, money: int):
        """Метод для добавления средств на баланс пассажира."""
        self.balance += money


if __name__ == '__main__':
    ticket_machine = TicketMachine()
    alice = Passenger('Алиса', 300, 'bus')
    bob = Passenger('Боб', 50, 'train')

    alice.buy_ticket(ticket_machine)
    alice.check_balance()
    bob.buy_ticket(ticket_machine)
    bob.add_balance(200)
    bob.check_balance()
    bob.buy_ticket(ticket_machine)
