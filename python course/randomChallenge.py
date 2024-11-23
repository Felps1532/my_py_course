# Class -> Dice
# method roll()
# we get a tuple with 2 random values
from random import randint

class Dice:
    def roll(self):
        values = (randint(1, 6), randint(1, 6))
        return values
# Teacher's solution


class Dice1:
    def roll(self):
        first = randint(1, 6)
        second = randint(1, 6)
        return first, second


# objects
dice = Dice()
print(dice.roll())

dice1 = Dice1()
dice1 = print(dice1.roll())
