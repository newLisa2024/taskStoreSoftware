# Написать программное обеспечение для сети магазинов. Каждый магазин
# в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Задача — создать класс `Store`,
# который можно будет использовать для создания различных магазинов.

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def print_details(self):
        print(f"Магазин: {self.name}, Адрес: {self.address}")

    def print_price_list(self):
        print("Прайс-лист:")
        for item, price in self.items.items():
            print(f"{item}: {price}")

store1 = Store("Фруктовый рай", "улица Пушкина, 33")
store2 = Store("Рынок", "площадь Революции, 4")
store3 = Store("Ягодное лукошко", "улица Ленина, 57")

store1.add_item('яблоки', 5.0)
store1.add_item('бананы', 4.5)
store2.add_item('хлеб', 1.0)
store2.add_item('круассан', 1.5)
store3.add_item('морковь', 4.5)
store3.add_item('латук', 3.0)

def print_store_details_and_price_list(store):
    store.print_details()
    store.print_price_list()
    print()

print_store_details_and_price_list(store1)

print(f"Цена яблок до: {store1.get_price('яблоки')}")
store1.update_price("яблоки", 5.5)
print(f"Цена яблок после обновления: {store1.get_price('яблоки')}")

store1.add_item("груши", 8.0)
print(f"Цена груш: {store1.get_price('груши')}")

store1.remove_item("бананы")
print(f"Цена бананов после удаления: {store1.get_price('бананы')}")