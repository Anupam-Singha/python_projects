class Person:

    def __init__(self, n, o) -> None:
        print("Hey I am protocol")
        self.name = n
        self.occ = o


    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Harry", "Developer")
b = Person('Divya' , "HR")

b.info()