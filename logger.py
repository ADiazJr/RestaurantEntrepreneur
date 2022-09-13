import os

class Logger():
    def __init__(self):
        self.transaction_count = 1
        self.daily_sales = 0

    def log_transaction(self, order, location_number):
        self.daily_sales += order.price
        file = open('log.txt', 'r')
        if os.path.getsize('log.txt') > 0:
            self.transaction_count = 1
            lines = file.readlines()
            for line in lines:
                self.transaction_count += 1
        file.close()
        file = open('log.txt', 'a')
        file.write(f"""CT#{self.transaction_count} Dish Ordered: {order.dish_name}, from location {location_number}, Price: {order.price}, Total: {self.daily_sales}\n""")
        file.close()

logger = Logger()