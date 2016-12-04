


from yamslam.dice import *

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


    def check(self, winning_roll):
        if len(set(winning_roll)) == 1:
            return True


class large_straight(Combos):
    def __init__ (self):
        self.name = 'Large Straight'
        self.points = 50
        Combos.combos.append(self)



    def check(self, winning_roll):
        if len(set(winning_roll)) == 5:
            if 1 in winning_roll and 6 in winning_roll:
                return None
            else:
                return True


class four_of_a_kind(Combos):
    def __init__ (self):
        self.name = 'Four of a kind'
        self.points = 40
        Combos.combos.append(self)


    def check(self, winning_roll):
        if len(set(winning_roll)) == 2:
            winning_roll = sorted(winning_roll)
            if winning_roll.count(winning_roll[3]) == 4:
                return True


class full_house(Combos):
    def __init__ (self):
        self.name = 'Full House'
        self.points = 30
        Combos.combos.append(self)

    def check(self, winning_roll):
        if len(set(winning_roll)) == 2:
            winning_roll = sorted(winning_roll)
            if winning_roll.count(winning_roll[0]) > 1:
                if winning_roll.count(winning_roll[3]) > 1:
                    return True


class flush(Combos):
    def __init__ (self):
        self.name = 'Flush'
        self.points = 25
        Combos.combos.append(self)


    def check(self, winning_roll):
        evens = []
        for elem in range(0, 5):
            if winning_roll[elem] % 2:
                evens.append(winning_roll[elem])
        if len(evens) == 5 or len(evens) == 0:
            return True



class small_straight(Combos):
    def __init__ (self):
        self.name = 'Small Straight'
        self.points = 20
        Combos.combos.append(self)


    def check(self, winning_roll):
        if 3 in winning_roll and 4 in winning_roll:
            if 1 in winning_roll and 2 in winning_roll:
                return True
            elif 2 in winning_roll and 5 in winning_roll:
                return True
            elif 5 in winning_roll and 6 in winning_roll:
                return True


class three_of_a_kind(Combos):
    def __init__ (self):
        self.name = 'Three of a kind'
        self.points = 10
        Combos.combos.append(self)


    def check(self, winning_roll):
        winning_roll = sorted(winning_roll)
        if winning_roll.count(winning_roll[2]) == 3:
            return True



class two_pair(Combos):
    def __init__ (self):
        self.name = 'Two pair'
        self.points = 5
        Combos.combos.append(self)


    def check(self, winning_roll):
        is_it_two_pair = []
        for i in range(0,4):
            if winning_roll.count(winning_roll[i]) == 2:
                is_it_two_pair.append(winning_roll[i])
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



