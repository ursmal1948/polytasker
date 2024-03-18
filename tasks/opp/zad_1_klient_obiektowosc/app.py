from dataclasses import dataclass
from typing import Self
from collections import defaultdict


@dataclass
class Client:
    name: str
    surname: str
    age: int
    cash: int

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


@dataclass
class Product:
    name: str
    category: str
    price: int

    def __hash__(self):
        return hash((self.name, self.category, self.price))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.name, self.category, self.price) == (other.name, other.category, other.price)

    @classmethod
    def from_text(cls, text: str) -> Self:
        purchase_data = text.split(';')
        return cls(purchase_data[0], purchase_data[1], int(purchase_data[2]))


#


class Shopping:

    def __init__(self):
        self.clients = {}

    def enter_datas(self, filenames: list[str]):
        for i in range(len(filenames)):
            with open(filenames[i], 'r') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split(' ', 1)
                client_data, products_data = data[0], data[1]
                client = Client.from_text(client_data)
                purchases = products_data.strip('[]').split(' ')
                products = [Product.from_text(p) for p in purchases]

                if client not in self.clients:
                    self.clients[client] = {}

                client_products = self.clients[client]
                for product in products:
                    if product not in client_products:
                        client_products[product] = 0
                    client_products[product] += 1
        return self.clients
    #
    # def get_clients_age_and_chetnie_produkty_kupowane(self):
    #     # Ale musz sie  z countem pobawic bo ma byc kluczem age a wartoscia
    #     # kategoeia ktora najchetniej kupowana czyli musi byc tez mapa
    #     # {category:count_of_category_in_age} i z tego maxa
    #     grouped_by_age = defaultdict(list)
    #     grouped_by_cat = defaultdict(int)
    #     for client, products in self.clients.items():
    #         category_count = defaultdict(int)
    #         for product in products:
    #             category_count[product.category]
    #
    #     return dict(grouped_by_age)


print(Shopping().enter_datas(['clients_1.txt', 'clients_3.txt', 'clients_2.txt']))


def main() -> None:
    shopping = Shopping()
    filanems = ['clients_1.txt', 'clients_3.txt', 'clients_2.txt']
    clients = shopping.enter_datas(filanems)


if __name__ == '__main__':
    main()
