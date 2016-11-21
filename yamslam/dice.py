
class Dice:
    dice_set = []


    def input_die_get_color(number):
        for self in Dice.dice_set:
            if self.value == number:
                return self.color


class one(Dice):
    def __init__ (self):
        Dice.dice_set.append(self)
        self.value = 1
        self.color = 'black'


class two(Dice):
    def __init__ (self):
        Dice.dice_set.append(self)
        self.value = 2
        self.color = 'red'


class three(Dice):
    def __init__ (self):
        Dice.dice_set.append(self)
        self.value = 3
        self.color = 'black'


class four(Dice):
    def __init__ (self):
        Dice.dice_set.append(self)
        self.value = 4
        self.color = 'red'


class five(Dice):
    def __init__ (self):
        Dice.dice_set.append(self)
        self.value = 5
        self.color = 'black'


class six(Dice):
    def __init__ (self):
        Dice.dice_set.append(self)
        self.value = 6
        self.color = 'red'


d1 = one()
d2 = two()
d3 = three()
d4 = four()
d5 = five()
d6 = six()




