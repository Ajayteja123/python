class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __int__(self):
            self.brand = "hp"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


# main
s1 = Student('ajay', 182)
s1.show()
lap1 = Student.Laptop()
# lap1=s1.show()
