from players import *
from dice import *

class Combos:
    combos = []

    chips = {}

    @classmethod
    def initialize_game(cls):
        Combos.chips[ys.name] = 100
        Combos.chips[ls.name] = 4
        Combos.chips[fk.name] = 4
        Combos.chips[fh.name] = 4
        Combos.chips[fl.name] = 4
        Combos.chips[ss.name] = 4
        Combos.chips[tk.name] = 4
        Combos.chips[tp.name] = 4
        return Combos.chips



class yam_slam(Combos):
    def __init__ (self):
        self.name = 'Yam Slam'
        self.points = 50
        Combos.combos.append(self)


    def check(self):
        roll_values = Dice.get_roll_values()
        if len(set(roll_values)) == 1:
            return True


class large_straight(Combos):
    def __init__ (self):
        self.name = 'Large Straight'
        self.points = 50
        Combos.combos.append(self)



    def check(self):
        roll_values = Dice.get_roll_values()
        if len(set(roll_values)) == 5:
            if 1 and 6 not in roll_values:
                return True


class four_of_a_kind(Combos):
    def __init__ (self):
        self.name = 'Four of a kind'
        self.points = 40
        Combos.combos.append(self)


    def check(self):
        roll_values = sorted(Dice.get_roll_values())
        if len(set(roll_values)) == 2:
            if roll_values.count(roll_values[3]) == 4:
                return True


class full_house(Combos):
    def __init__ (self):
        self.name = 'Full House'
        self.points = 30
        Combos.combos.append(self)

    def check(self):
        roll_values = sorted(Dice.get_roll_values())
        if len(set(roll_values)) == 2:
            if roll_values.count(roll_values[0]) > 1:
                if roll_values.count(roll_values[4]) > 1:
                    return True


class flush(Combos):
    def __init__ (self):
        self.name = 'Flush'
        self.points = 25
        Combos.combos.append(self)


    def check(self):
        roll_colors = Dice.get_roll_colors()
        if len(set(roll_colors)) == 1:
            return True



class small_straight(Combos):
    def __init__ (self):
        self.name = 'Small Straight'
        self.points = 20
        Combos.combos.append(self)


    def check(self):
        roll_values = list(Dice.get_roll_values())
        if 3 in roll_values and 4 in roll_values:
            if 1 in roll_values and 2 in roll_values:
                return True
            elif 2 in roll_values and 5 in roll_values:
                return True
            elif 5 in roll_values and 6 in roll_values:
                return True


class three_of_a_kind(Combos):
    def __init__ (self):
        self.name = 'Three of a kind'
        self.points = 10
        Combos.combos.append(self)


    def check(self):
        roll_values = sorted(Dice.get_roll_values())
        if roll_values.count(roll_values[2]) == 3:
            return True



class two_pair(Combos):
    def __init__ (self):
        self.name = 'Two pair'
        self.points = 5
        Combos.combos.append(self)


    def check(self):
        roll_values = Dice.get_roll_values()
        is_it_two_pair = []
        for i in range(0,4):
            if roll_values.count(roll_values[i]) == 2:
                is_it_two_pair.append(roll_values[i])
        if len(set(is_it_two_pair)) == 2:
            return True

ys = yam_slam()
ls = large_straight()
fk = four_of_a_kind()
fh = full_house()
fl = flush()
ss = small_straight()
tk = three_of_a_kind()
tp = two_pair()



