class Person:
    name = None
    def __init__(self) -> None:
        self.name = "Adam"

    def __init__(self, name):
        self.name = name

    


p1 = Person("SY")
print(p1.name)