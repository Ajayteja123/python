class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        # self indicates object of the class
        return f'{self.first_name} {self.last_name}'


p1 = Person('AJAY', 'TEJA')
print(f'persons full name is: {p1.full_name()}')
# print(Person.full_name(p1))
