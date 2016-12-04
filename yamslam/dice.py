import random

class Dice:
    dice_set = []
    roll = []

    @classmethod
    def throw_a_roll(cls, dice):
        for i in range(0, dice):
            number = random.randint(1, 6)
            for self in Dice.dice_set:
                if number == self.value:
                    Dice.roll.append(self)
        return Dice.roll

    @classmethod
    def get_roll_values(cls):
        roll_values = []
        for self in Dice.roll:
            roll_values.append(self.value)
        return roll_values




class one(Dice):
    def __init__(self):
        Dice.dice_set.append(self)
        self.value = 1
        self.color = 'black'


class two(Dice):
    def __init__(self):
        Dice.dice_set.append(self)
        self.value = 2
        self.color = 'red'


class three(Dice):
    def __init__(self):
        Dice.dice_set.append(self)
        self.value = 3
        self.color = 'black'


class four(Dice):
    def __init__(self):
        Dice.dice_set.append(self)
        self.value = 4
        self.color = 'red'


class five(Dice):
    def __init__(self):
        Dice.dice_set.append(self)
        self.value = 5
        self.color = 'black'


class six(Dice):
    def __init__(self):
        Dice.dice_set.append(self)
        self.value = 6
        self.color = 'red'


d1 = one()
d2 = two()
d3 = three()
d4 = four()
d5 = five()
d6 = six()




