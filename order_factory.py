from pizza import Pizza
from pasta import Pasta
from salad import Salad


class OrderFactory():
    @staticmethod
    def create_order(input):
        if input == "1":
            return Pizza()
        elif input == "2":
            return Pasta()
        elif input == "3":
            return Salad()