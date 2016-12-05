


from yamslam.dice import *

class Combos:
    combos = []

    chips = {}

    @classmethod
    def initialize_game(cls):
        Combos.chips[ls.name] = 0
        Combos.chips[fk.name] = 2
        Combos.chips[fh.name] = 0
        Combos.chips[fl.name] = 5
        Combos.chips[ss.name] = 0
        Combos.chips[tk.name] = 3
        Combos.chips[tp.name] = 0
        return Combos.chips



class yam_slam(Combos):
    def __init__ (self):
        self.name = 'Yam Slam'


    def check(self, winning_roll):
        if len(set(winning_roll)) == 1:
            return True


class large_straight(Combos):
    def __init__ (self):
        self.name = 'Large Straight'
        self.points = 50
        Combos.combos.append(self)



    def check(self, winning_roll):
        if ys.check(winning_roll):
            print('You got {}!'.format(ys.name))
            return True
        elif len(set(winning_roll)) == 5:
            if 1 in winning_roll and 6 in winning_roll:
                return None
            else:
                print('You got {}!'.format(ls.name))
                return True


class four_of_a_kind(Combos):
    def __init__ (self):
        self.name = 'Four of a kind'
        self.points = 40
        Combos.combos.append(self)


    def check(self, winning_roll):
        if ys.check(winning_roll):
            print('You got {}!'.format(ys.name))
            return True
        elif len(set(winning_roll)) == 2:
            winning_roll = sorted(winning_roll)
            if winning_roll.count(winning_roll[3]) == 4:
                print('You got {}!'.format(fk.name))
                return True


class full_house(Combos):
    def __init__ (self):
        self.name = 'Full House'
        self.points = 30
        Combos.combos.append(self)

    def check(self, winning_roll):
        if ys.check(winning_roll):
            print('You got {}!'.format(ys.name))
            return True
        elif len(set(winning_roll)) == 2:
            winning_roll = sorted(winning_roll)
            if winning_roll.count(winning_roll[0]) > 1:
                if winning_roll.count(winning_roll[3]) > 1:
                    print('You got {}!'.format(fh.name))
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
        if ys.check(winning_roll):
            print('You got {}!'.format(ys.name))
            return True
        elif len(evens) == 5 or len(evens) == 0:
            print('You got {}!'.format(fl.name))
            return True



class small_straight(Combos):
    def __init__ (self):
        self.name = 'Small Straight'
        self.points = 20
        Combos.combos.append(self)


    def check(self, winning_roll):
        if ys.check(winning_roll):
            print('You got {}!'.format(ys.name))
            return True
        elif 3 in winning_roll and 4 in winning_roll:
            if 1 in winning_roll and 2 in winning_roll:
                print('You got {}!'.format(ss.name))
                return True
            elif 2 in winning_roll and 5 in winning_roll:
                print('You got {}!'.format(ss.name))
                return True
            elif 5 in winning_roll and 6 in winning_roll:
                print('You got {}!'.format(ss.name))
                return True


class three_of_a_kind(Combos):
    def __init__ (self):
        self.name = 'Three of a kind'
        self.points = 10
        Combos.combos.append(self)


    def check(self, winning_roll):
        winning_roll = sorted(winning_roll)
        if ys.check(winning_roll):
            print('You got {}!'.format(ys.name))
            return True
        elif fk.check(winning_roll):
            print('You got {}!'.format(tk.name))
            return True
        elif winning_roll.count(winning_roll[2]) == 3:
            print('You got {}!'.format(tk.name))
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
        if ys.check(winning_roll):
            print('You got {}!'.format(ys.name))
            return True
        elif fk.check(winning_roll) or fh.check(winning_roll):
            print('You got {}!'.format(tp.name))
            return True
        elif len(set(is_it_two_pair)) == 2:
            print('You got {}!'.format(tp.name))
            return True

ys = yam_slam()
ls = large_straight()
fk = four_of_a_kind()
fh = full_house()
fl = flush()
ss = small_straight()
tk = three_of_a_kind()
tp = two_pair()



