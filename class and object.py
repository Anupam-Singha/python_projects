class person:
    name = "Harry"
    occupation = "Software Tester"
    netWorth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = person()
b = person()
a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Rem"
b.occupation = "Sales manager"

print(a.name, a.occupation)
a.info()
print(a.name, a.occupation)
#a.info()