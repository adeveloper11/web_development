class Animal:
    def __init__(self):
        self.age = 1


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # using this 'super()' we can run both age and weight method
        # if we dont use super here then the parent init method is voileted
        self.weight = 2

    def walk(self):
        print("walkin")


m = Mammal()

print(m.weight)
print(m.age)
