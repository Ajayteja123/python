class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price


d1 = Laptop('lenovo', 'yoga520', '50000')
print(d1.brand_name)
