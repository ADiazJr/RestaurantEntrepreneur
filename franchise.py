from order_factory import OrderFactory
from logger import logger

class Franchise():
    def __init__(self, number):
        self.location_number = number

    def place_order(self):
        order = input("""Welcome to Bubbles Cafe, what would you like to order?
        Type '1' for pizza, '2' for pasta, '3' for salad.
        """)
        orders = OrderFactory.create_order(order)
        logger.log_transaction(orders, self.location_number)