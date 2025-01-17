"""Hotel.
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, заказ товаров на маркетплейсе или учет книг в библиотеке.
Создайте несколько объектов классов, которые описывают ситуацию. Объекты должны содержать как атрибуты
так и методы класса для симуляции различных действий. Программа должна инстанцировать объекты и
эмулировать какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д.
"""

class HotelRoom:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.is_booked = False

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return f'Комната {self.room_number} забронирована.'
        return f'Комната {self.room_number} уже занята.'

    def release_room(self):
        if self.is_booked:
            self.is_booked = False
            return f'Комната {self.room_number} освободилась.'
        return f'Комната {self.room_number} готова к бронированию.'


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.book_room()
        return f'Комнаты {room_number} не существует.'

    def release_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.release_room()
        return f'Комнаты {room_number} не существует.'


hotel = Hotel()
hotel.add_room(HotelRoom(1, 100))
hotel.add_room(HotelRoom(2, 150))
hotel.add_room(HotelRoom(3, 200))
hotel.add_room(HotelRoom(4, 500))

print(hotel.book_room(1))
print(hotel.book_room(1))
print(hotel.release_room(1))
print(hotel.release_room(1))
print(hotel.book_room(1))
print(hotel.release_room(5))
