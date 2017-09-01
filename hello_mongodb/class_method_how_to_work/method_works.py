class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self)
        print(type(self))
        print(self.name + ' is eating')


p = Person('liqirong')
p.eat()
print(Person.eat)
print(p.eat)
