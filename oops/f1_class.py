class Laptop:
    discount_percentage = 10

    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self):
        off_price = (self.discount_percentage/100)*self.price
        return self.price - off_price


d1 = Laptop('lenovo', 'yoga520', '50000')
d1.discount_percentage = 10
