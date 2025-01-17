"""Создаём модель из жизни для ресторана"""
class Waiter:
    def __init__(self, name):
        self.name = name

    def take_order(self, table_number, order):
        return f"{self.name} takes an order from table {table_number}: {order}"

    def serve_order(self, table_number, order):
        return f"{self.name} serves the order to table {table_number}: {order}"


class Visitor:
    def __init__(self, name, table_number):
        self.name = name
        self.table_number = table_number

    def make_order(self, order):
        return f"{self.name} at table {self.table_number} makes an order: {order}"

    def enjoy_meal(self):
        return f"{self.name} at table {self.table_number} is enjoying the meal"


john = Waiter("John")

alice = Visitor("Alice", 1)
bob = Visitor("Bob", 2)

print(john.take_order(1, "Burger and fries"))
print(alice.make_order("Salad and water"))
print(john.serve_order(1, "Burger and fries"))
print(bob.make_order("Pizza and soda"))
print(john.serve_order(2, "Pizza and soda"))
print(alice.enjoy_meal())
print(bob.enjoy_meal())