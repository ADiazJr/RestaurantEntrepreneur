class Logger():
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, location_number):
        self.transaction_count += 1
        self.daily_sales += order.price
        file = open('log.txt', 'a')
        file.write(f"""
        CT#{self.transaction_count} Dish Ordered: {order.dish_name}, from location {location_number}, Price: {order.price}, Total: {self.daily_sales}
        """)
        file.close()

logger = Logger()