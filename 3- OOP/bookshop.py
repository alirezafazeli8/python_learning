import datetime


class Product:
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author


class Mixin:
    def to_json(self):
        return self.__dict__


class TimeStamp:
    def __init__(self, date):
        self.date = date

    def date(self):
        self.date = datetime.datetime.now()
        return self.date


class OrderBook(Product, Mixin, TimeStamp):
    def __init__(self, name, price, author, customer):
        super().__init__(name, price, author)
        self.customer = customer

    def show_order(self):
        return f"""
    
        book name : {self.name}
        book price : {self.price}
        book author : {self.author}
        customer : {self.customer}
        order date : {self.date()}
        in json : {self.to_json()}
        
    
    """


ord1 = OrderBook("Lord of the rings", "1000$", "IDK", "alireza fazeli")


print(ord1.show_order())
