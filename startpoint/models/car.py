class Car:

    def __init__(self, brand,  make, model, buying_cost, selling_cost, quantity,  sold = False, id = None):
        self.brand = brand
        self.make = make
        self.model = model
        self.buying_cost = buying_cost
        self.selling_cost = selling_cost
        self.quantity = quantity
        self.sold = sold
        self.id = id


    def mark_sold(self):
        self.sold = True