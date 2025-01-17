"""
Создайте модель из жизни.
Это может быть бронирование комнаты в отеле, покупка билета в транспортной компании,
заказ товаров на маркетплейсе или учет книг в библиотеке.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты, так и методы класса для симуляции различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
"""
import uuid


class Cloths:
    """Определяет одежду."""

    def __init__(self, kind: str, price: int, color: str):
        """Инициализирует класс."""
        self.price = price
        self.kind = kind
        self.color = color

    def describe_clothes(self):
        """Описывает товар."""
        return f'Товар {self.kind}, {self.color} цвета, стоимостью {self.price} рублей,'

    def try_on(self):
        """Товар относится в примерочную."""
        print(f'{self.describe_clothes()} ожидает Вас в примерочной')


class Basket:
    """Определяет корзину и действия, которые можно над ней произвести."""

    def __init__(self):
        """Инициализирует класс."""
        self.list_of_cloths = {}
        self.contents = []
        self.total_price = 0

    def update_the_basket(self):
        """Обновляет содержимое корзины."""
        self.contents = list(self.list_of_cloths.keys())
        self.total_price = sum(self.list_of_cloths.values())

    def put_into_the_basket(self, cloths: Cloths):
        """Кладет товар в корзину."""
        self.list_of_cloths[cloths.kind] = cloths.price
        self.update_the_basket()
        print(f'{cloths.describe_clothes()} положен в корзину')

    def remove_from_the_basket(self, cloths: Cloths):
        """Удаляет товар из корзины."""
        if cloths.kind in self.list_of_cloths:
            self.list_of_cloths.pop(cloths.kind)
            print(f'{cloths.describe_clothes()} убран из корзины')
            self.update_the_basket()
        else:
            print(f'{cloths.describe_clothes()} нет в корзине')

    def check_the_basket(self):
        """Проверяет товары, которые лежат в корзине."""
        print(f'В корзине лежат товары: {", ".join(self.contents)} на сумму {self.total_price} рублей')

    def pay_the_basket(self):
        """Оплачивает корзину."""
        self.update_the_basket()
        print(f'Товары: {", ".join(self.contents)} на сумму {self.total_price} рублей оплачены')


class Customer:
    """Определяет покупателя и его действия."""

    def __init__(self, name: str):
        """Инициализирует класс."""
        self.name = name
        self.discount_card = uuid.uuid4()
        self.wishlist = []
        self.basket = Basket()

    def add_to_wishlist(self, cloths: Cloths):
        """Записывает товар в вишлист покупателя."""
        self.wishlist.append(cloths)
        print(f'{cloths.describe_clothes()} в свой вишлист')

    def check_discount_card_number(self):
        """Позволяет узнать номер дисконтной карты."""
        print(f'Номер дисконтной карты покупателя {self.name}: {self.discount_card}')


if __name__ == '__main__':
    customer = Customer('Анастасия')
    jeans = Cloths('джинсы', 100, 'синего')
    dress = Cloths('платье', 120, 'черного')
    jeans.try_on()
    dress.try_on()
    customer.basket.put_into_the_basket(jeans)
    customer.basket.put_into_the_basket(dress)
    customer.basket.check_the_basket()
    customer.basket.remove_from_the_basket(jeans)
    customer.basket.check_the_basket()
    customer.add_to_wishlist(jeans)
    customer.check_discount_card_number()
    customer.basket.pay_the_basket()
