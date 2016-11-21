
class Score():
    roll = []

    def throw_a_roll(dice):
        for i in range(0 ,dice):
            number = random.randint(1 ,6)
            for self in Dice.dice_set:
                if number == self.value:
                    Score.roll.append(self)
        return Score.roll


    def get_roll_values():
        roll_values = []
        for self in Score.roll:
            roll_values.append(self.value)
        return roll_values

    def get_roll_colors():
        roll_colors = []
        for self in Score.roll:
            roll_colors.append(self.color)
        return roll_colors



    def score_the_roll():
        if Combos.is_it_yam_slam():
            return 'You got a Yam Slam!'
        elif Combos.is_it_large_straight():
            return 'You got a large straight!'
        elif Combos.is_it_four_of_a_kind():
            return 'You got four of a kind!'
        elif Combos.is_it_full_house():
            return 'You got a full house!'
        elif Combos.is_it_flush():
            return 'You got a flush!'
        elif Combos.is_it_small_straight():
            return 'You got a small straight!'
        elif Combos.is_it_three_of_a_kind():
            return 'You got three of a kind!'
        elif Combos.is_it_two_pair():
            return 'You got two pair!'
        else:
            return 'You got nothing, try again.'



