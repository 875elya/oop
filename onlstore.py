class Product:
    def __init__(self, idd, name, price, invcount):
        self.id = idd
        self.name = name
        self.price = price
        self.invcount = invcount

    def setdiscount(self, percent):
        percent = 100 - percent
        self.price = (self.price * percent) / 100

    def getprice(self):
        return self.price

    def sell(self, quantity):
        self.invcount = self.invcount - quantity

    def getinv(self):
        return self.invcount



fruit = Product(1, "orange", 2000, 200)
fruit.setdiscount(40)
print(fruit.getprice())
fruit.sell(50)
print(fruit.getinv())


