# "Herança"
# problem -> two classes doing the same function!
# we can fix it creating a parent class

class Mammal:
    def walk(self):
        print('walk')


# now the Dog will inherate all the functions of the Mammal class
class Dog(Mammal):
    def bark(self):
        print('bark')
    # we use 'pass' just to not leave the class empty
    pass


class Cat(Mammal):
    def be_cute(self):
        print('meow')
    pass

dog1 = Dog()
cat1 = Cat()

dog1.walk()
dog1.bark()
cat1.be_cute()
