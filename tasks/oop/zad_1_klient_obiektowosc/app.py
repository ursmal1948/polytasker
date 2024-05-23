import re
from dataclasses import dataclass, field
from typing import Self
from collections import defaultdict, Counter
from typing import Callable

"""
1. Zaimplementuj klasę Klient oraz klasę Produkt. Klasa Klient posiada pola imię, nazwisko, wiek, gotówka. 
Klasa Produkt posiada pola nazwa, kategoria, cena. Przygotuj kilka plików tekstowych. 
W każdym pliku znajdują się wiersze, przechowujące dane o kliencie oraz w kwadratowych nawiasach
dane o produktach, które klient zakupił. 
Przykładowy wiersz z danymi umieszczonymi w pliku tekstowym zaprezentowano poniżej: 

Jan;Kos;18;2000 [Komputer;Elektronika;2400 PanTadeusz;Ksiazka;120] 

Ten sam klient może pojawiać się w wielu wierszach w kilku plikach. Ten sam produkt może być kupowany
kilka razy nawet przez tego samego klienta. Przygotuj klasę Zakupy, która posiada pole składowe - mapę.
Kluczem mapy jest obiekt klasy Klient, natomiast wartością mapa, która jako klucz posiada obiekt klasy Produkt,
natomiast wartością jest liczba całkowita, określająca, ile razy klient zakupił ten produkt. Przygotuj konstruktor, 
który jako argument pobiera nazwy plików tekstowych i wypełnia mapę danymi z plików tekstowych. Następnie 
napisz metody, które wykorzystując operacje na kolekcjach oraz mapach 
(programiści Java mogą stosować strumienie Java 8) rozwiążą następujące problemy:

-> Wyznacz klienta, który zapłacił najwięcej za wszystkie zakupy. W osobnej metodzie wyznacz klienta, 
który zapłacił najwięcej za zakupy z wybranej kategorii. Nazwę kategorii przekaż jako argument funkcji done

-> Wykonaj zestawienie (mapę), w którym pokażesz wiek klientów oraz kategorie produktów, 
które najchętniej w tym wieku kupowano. done

-> Wykonaj zestawienie (mapę), w którym pokażesz średnią cenę produktów w danej kategorii. 
Dodatkowo wyznacz dla każdej kategorii produkt najdroższy oraz produkt najtańszy. done

-> Wyznacz klientów, którzy kupowali najczęściej produkty danej kategorii. Otrzymane zestawienie zwracaj w postaci mapy.

-> Sprawdź, czy klient jest w stanie zapłacić za zakupy. Żeby to stwierdzić, porównaj wartość pola przechowującego 
ilość gotówki, którą posiada klient z sumaryczną ceną za zakupy klienta. Wykonaj mapę, w której jako klucz
podasz klienta, natomiast jako wartość przechowasz dług, który klient musi spłacić za niezapłacone zakupy.
Dług stanowi różnica pomiędzy kwotą do zapłaty oraz gotówką, którą posiada klient. done

"""


@dataclass
class Client:
    name: str
    surname: str
    age: int
    cash: int

    @classmethod
    def from_text(cls, text: str) -> Self:
        data = text.split(' ')
        client_data = data[0].split(";")
        return cls(
            name=client_data[0],
            surname=client_data[1],
            age=int(client_data[2]),
            cash=int(client_data[3])
        )

    def __hash__(self):
        return hash((self.name, self.surname, self.age, self.cash))

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return (
                self.name == other.name and
                self.surname == other.surname and
                self.age == other.age and
                self.cash == other.cash
        )


class Validator:
    @staticmethod
    def validate_line(line: str,
                      regex: str = r'^[A-Z][a-z]+;[A-Z][a-z]+;\d+;\d+ \[([A-Z][a-z]+;[A-Z][a-z]+;\d+ )*[A-Z][a-z]+;['
                                   r'A-Z][a-z]+;\d+]$') -> bool:
        if re.match(regex, line):
            return True
        return False


@dataclass
class Product:
    name: str
    category: str
    price: int

    @classmethod
    def from_text(cls, text: str) -> Self:
        purchase_data = text.split(';')
        return cls(purchase_data[0], purchase_data[1], int(purchase_data[2]))

    def __hash__(self):
        return hash((self.name, self.category, self.price))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.name, self.category, self.price) == (other.name, other.category, other.price)


class ClientsFileReader:

    @staticmethod
    def get_clients(filenames: list[str]) -> dict[Client, dict[Product, int]]:
        clients = {}
        for i in range(len(filenames)):
            with open(filenames[i], 'r') as file:
                lines = file.readlines()

            for line in lines:
                if not Validator.validate_line(line):
                    raise ValueError("Incorrect format")
                data = line.strip().split(' ', 1)
                client_data, products_data = data[0], data[1]
                client = Client.from_text(client_data)
                purchases = products_data.strip('[]').split(' ')
                products = [Product.from_text(p) for p in purchases]

                if client not in clients:
                    clients[client] = {}

                client_products = clients[client]
                for product in products:
                    if product not in client_products:
                        client_products[product] = 0
                    client_products[product] += 1
        return clients


@dataclass
class ShoppingService:
    clients: dict[Client, dict[Product, int]] = field(default_factory=dict)

    # -------------------------------------------------------------------
    # -> Wyznacz klienta, który zapłacił najwięcej za wszystkie zakupy. W osobnej metodzie wyznacz klienta,
    # który zapłacił najwięcej za zakupy z wybranej kategorii. Nazwę kategorii przekaż jako argument funkcji done
    def _calculate_client_spendings(self, client: Client) -> int:
        client_products = self.clients[client]
        sum_ = 0
        for product, count in client_products.items():
            sum_ += product.price * count
        return sum_

    def _calculate_client_spendings_by_category(self, client: Client, category: str) -> int:
        client_products = self.clients[client]
        sum_ = 0
        for product, count in client_products.items():
            if product.category == category:
                sum_ += product.price * count
        return sum_

    def find_client_with_extreme_spendings(self, extreme_fn: Callable[[list[int]], int]) -> Client | list[Client]:
        grouped_by_total_spendings = defaultdict(list)

        for client in self.clients:
            total_spendings = self._calculate_client_spendings(client)
            grouped_by_total_spendings[total_spendings].append(client)
        extreme_value = extreme_fn(list(grouped_by_total_spendings.keys()))
        return grouped_by_total_spendings[extreme_value]

    def find_client_with_extreme_spendings_by(self, category: str, extreme_fn: Callable[[list[int]], int]) -> list[int]:
        grouped_by_category_spending = defaultdict(list)

        for client in self.clients.keys():
            total_spendings = self._calculate_client_spendings_by_category(client, category)
            if total_spendings:
                grouped_by_category_spending[total_spendings].append(client)
        extreme_spendings = extreme_fn(list(grouped_by_category_spending.keys()))
        return grouped_by_category_spending[extreme_spendings]

    # -------------------------------------------------------------------

    # -> Wykonaj zestawienie (mapę), w którym pokażesz wiek klientów oraz kategorie produktów,
    # które najchętniej w tym wieku kupowano

    def get_categories_most_bought_for_age(self, age: int) -> list[str]:
        category_count_by_age = Counter()
        for client, products in self.clients.items():
            if client.age == age:
                print("HERE")
                print(products.items())
                for product, count in products.items():
                    category_count_by_age[product.category] += count
        max_count = max(category_count_by_age.values())
        print(category_count_by_age.items())
        most_bought_categories = [category for category, count in category_count_by_age.items() if count == max_count]
        return most_bought_categories

    def get_age_categories_most_bought_by_age(self) -> dict[int, list[str]]:
        grouped_by_age_and_categories_most_bought_for_age = defaultdict(list)
        for client in self.clients:
            age = client.age
            grouped_by_age_and_categories_most_bought_for_age[age] = self.get_categories_most_bought_for_age(age)

        return dict(grouped_by_age_and_categories_most_bought_for_age)

    # -------------------------------------------------------------------

    # -> Wykonaj zestawienie (mapę), w którym pokażesz średnią cenę produktów w danej kategorii.
    # Dodatkowo wyznacz dla każdej kategorii produkt najdroższy oraz produkt najtańszy. done

    def get_unique_products_for_category(self, category: str) -> list[Product]:
        unique_products = set()
        for products_count in self.clients.values():
            for product, count in products_count.items():
                if product.category == category:
                    unique_products.add(product)
        return list(unique_products)

    def get_average_products_price_for_category(self, category: str) -> int | float:
        unique_products = self.get_unique_products_for_category(category)
        total_price = sum([product.price for product in unique_products])
        return total_price / len(unique_products)

    def get_average_products_price_by_category(self):
        grouped_by_category_average_price = defaultdict(float)
        for client, products in self.clients.items():
            for product in set(products):
                category = product.category
                grouped_by_category_average_price[category] = self.get_average_products_price_for_category(category)

        return dict(grouped_by_category_average_price)

    def get_max_priced_products_for_category(self, category: str) -> Product | list[Product]:
        unique_products = self.get_unique_products_for_category(category)
        extreme_priced = max([product.price for product in unique_products])
        return [product for product in unique_products if product.price == extreme_priced]

    def get_max_priced_products_by_category(self):
        grouped_by_category = defaultdict(list)
        unique_categories = self.get_categories()
        for category in unique_categories:
            grouped_by_category[category] = self.get_max_priced_products_for_category(category)
        return dict(grouped_by_category)

    # -------------------------------------------------------------------

    # -> Wyznacz klientów, którzy kupowali najczęściej produkty danej kategorii. Otrzymane zestawienie zwracaj
    # w postaci mapy.

    def get_clients_for_category(self, category: str) -> list[Client]:
        clients_by_category = set()
        for client, products in self.clients.items():
            for product in products:
                if product.category == category:
                    clients_by_category.add(client)
        return list(clients_by_category)

    def count_client_category_count(self, client: Client, category: str):
        client_products = self.clients[client]
        return sum([client_products[product] for product in client_products if product.category == category])

    def get_clients_who_bought_most_for_category(self, category: str) -> list[Client]:
        clients_by_category = self.get_clients_for_category(category)
        print(f'CLient by cat: {clients_by_category}')
        grouped_by_category_count = defaultdict(list)
        for client in clients_by_category:
            count = self.count_client_category_count(client, category)
            grouped_by_category_count[count].append(client)
        return max(grouped_by_category_count.items())[1]

    def get_clients_who_bought_most_by_category(self) -> dict[str, list[Client]]:
        categories = self.get_categories()
        grouped_by_category = defaultdict(list)
        for c in categories:
            client = self.get_clients_who_bought_most_for_category(c)
            grouped_by_category[c].extend(client)
        return dict(grouped_by_category)

    def get_categories(self) -> list[str]:
        categories = set()
        for products in self.clients.values():
            for product in products:
                categories.add(product.category)
        return list(categories)

    # -------------------------------------------------------------------

    def is_solvent(self, client: Client) -> bool:
        total_spendings = self._calculate_client_spendings(client)
        return client.cash >= total_spendings

    def calculate_debt_for_client(self, client: Client):
        if not self.is_solvent(client):
            total_spendings = self._calculate_client_spendings(client)
            return total_spendings - client.cash
        return 0

    def are_clients_solvent(self):
        debts = defaultdict(int)
        for client in self.clients:
            debt = self.calculate_debt_for_client(client)
            if debt:
                debts[client] = debt
        return debts


def main() -> None:
    filenames = ['clients_1.txt']
    clients = ClientsFileReader.get_clients(filenames)
    shoppings_service = ShoppingService(clients)
    print(shoppings_service.clients)


if __name__ == '__main__':
    main()
