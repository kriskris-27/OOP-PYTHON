class Product:
    def __init__(self,name,price,stock,sku):
        self.name = name
        self._price = price
        self._stock = stock
        
        self.sku = sku

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value <=0:
            raise ValueError("Price must be greater than zero")
        self._price = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self,value):
        if value<0:
            raise ValueError("Stock cant be assigned negative value")
        self._stock = value
    

    def purchase(self,quantity):
        if quantity <=0:
            raise ValueError("Purchase value should need to greater than zero")
        if quantity >self.stock:
            raise ValueError(f"Insuffient stock for {self.name} .Availble stock {self.stock}")
        
        self.stock -= quantity
        return self.price*quantity

    def restock(self,quantity):
        if quantity<=0:
            raise ValueError("Restock quantity must be positive")

        self.stock +=quantity
        print(f"[Restock] {self.name}: Added {quantity} units. New stock: {self.stock}")

    def is_availble(self):
        return self.stock > 0