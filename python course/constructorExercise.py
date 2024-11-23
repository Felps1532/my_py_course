# class Person -> name, talk()

class Person:
    def __init__(self, name):
        self.name = str(name)

    def talk(self):
        print(f"Let's talk, {self.name}!")


# each object is a different instance of a person class
felps = Person('Felps')
felps.talk()
print(felps.name)

john = Person('John Smith')
john.talk()
print(john.name)
