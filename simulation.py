from franchise import Franchise

class Simulation():
   def run_simulation(self):
    franchise_one = Franchise(1)
    franchise_two = Franchise(2)
    franchise_three = Franchise(3)

    franchise_one.place_order()
    franchise_three.place_order()
    franchise_two.place_order()
    franchise_three.place_order()
    franchise_two.place_order()
    franchise_one.place_order()