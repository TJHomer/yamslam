class Combos:
    pass

    def is_it_yam_slam():
        roll_values = Gameplay.get_roll_values()
        if len(set(roll_values)) == 1:
            return True

    def is_it_large_straight():
        roll_values = Gameplay.get_roll_values()
        if len(set(roll_values)) == 5:
            if 1 and 6 not in roll_values:
                return True

    def is_it_small_straight():
        roll_values = list(Gameplay.get_roll_values())
        if 3 in roll_values and 4 in roll_values:
            if 1 in roll_values and 2 in roll_values:
                return True
            elif 2 in roll_values and 5 in roll_values:
                return True
            elif 5 in roll_values and 6 in roll_values:
                return True

    def is_it_two_pair():
        roll_values = Gameplay.get_roll_values()
        is_it_two_pair = []
        for i in range(0, 4):
            if roll_values.count(roll_values[i]) == 2:
                is_it_two_pair.append(roll_values[i])
        if len(set(is_it_two_pair)) == 2:
            return True

    def is_it_three_of_a_kind():
        roll_values = sorted(Gameplay.get_roll_values())
        if roll_values.count(roll_values[2]) == 3:
            return True

    def is_it_four_of_a_kind():
        roll_values = sorted(Gameplay.get_roll_values())
        if len(set(roll_values)) == 2:
            if roll_values.count(roll_values[3]) == 4:
                return True

    def is_it_full_house():
        roll_values = sorted(Gameplay.get_roll_values())
        if len(set(roll_values)) == 2:
            if roll_values.count(roll_values[0]) > 1:
                if roll_values.count(roll_values[4]) > 1:
                    return True

    def is_it_flush():
        roll_colors = Gameplay.get_roll_colors()
        if len(set(roll_colors)) == 1:
            return True


class yam_slam(Combos):
    def __init__(self):
        self.points = 50


class large_straight(Combos):
    def __init__(self):
        self.points = 50


class four_of_a_kind(Combos):
    def __init__(self):
        self.points = 40


class full_house(Combos):
    def __init__(self):
        self.points = 30


class flush(Combos):
    def __init__(self):
        self.points = 25


class small_straight(Combos):
    def __init__(self):
        self.points = 20


class three_of_a_kind(Combos):
    def __init__(self):
        self.points = 10


class two_pair(Combos):
    def __init__(self):
        self.points = 5

