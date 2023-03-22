class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("person Greet")


class Manager(Person, Employee):
    pass


m = Manager()
m.greet()
