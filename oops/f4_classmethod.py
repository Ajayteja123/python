class Person:
    count_instance = 0

    def __init__(self, first_name, last_name):
        Person.count_instance += 1  # class variable/class attribute
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def count_instances(cls):
        return f"{cls.count_instance}"

    def full_name(self):
        # self indicates object of the class
        return f'{self.first_name} {self.last_name}'


p1 = Person('AJAY', 'TEJA')
print(f'persons full name is: {p1.full_name()}')
# print(Person.full_name(p1))
print(Person.count_instances())
