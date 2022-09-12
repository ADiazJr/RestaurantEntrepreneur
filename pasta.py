from order import Order

class Pasta(Order):
    def __init__(self):
       super().__init__('Pasta', 10)