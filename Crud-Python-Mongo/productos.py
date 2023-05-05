class Product:
    def __init__(self, name, price, quantity)
    self.name = name
    self.price = price
    self.quantity = quantity

    def toDBCollection(self):
        'name': self.name,
        'pice': self.price,
        'quantity':self.quantity,
        