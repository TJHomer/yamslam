from yamslam.combos import *
from yamslam.players import *
from yamslam.dice import *


current_player = p2
roll = []





def check_if_game_over(chips):
    chips_left = 0
    for i in chips.values():
        chips_left += i
    if chips_left == 0:
        return False
    else:
        return True


def announce_winner():
    if p2.points > p1.points:
        print ('Game over! {} is the winner!'.format(p2.name))
    else:
        print ('Game over! {} is the winner!'.format(p1.name))


def switch_players(whos_up):
    if whos_up == p2:
        current_player = p1
    else:
        current_player = p2
    return current_player


def keep_or_reroll():
    reroll = [0, 0, 0, 0, 0]
    for i in range(1, 3):
        Dice.throw_a_roll(len(reroll))
        print(Dice.get_roll_values())
        print('Type the numbers you would like to reroll')
        print('or press enter to keep this roll')
        choice = input('')
        if choice == '':
            return Dice.get_roll_values()
        else:
            choice = choice.replace(',', '')
            choice = choice.replace(' ', '')
            reroll = [int(i) for i in choice]
            for number in reroll:
                for self in Dice.dice_set:
                    if number == self.value:
                        Dice.roll.remove(self)
    Dice.throw_a_roll(len(reroll))
    print(Dice.get_roll_values())
    return Dice.get_roll_values()



def score_the_roll(winning_roll):
    print(winning_roll)
    for combo in Combos.combos:
        if Combos.chips[combo.name] != 0:
            if combo.check(winning_roll):
                Combos.chips[combo.name] -= 1
                return combo.name
    else:
        print('Sorry, you got nothing.')
        return None


def add_points(combo):
    current_player.points += combo.points




def game():
    if check_if_game_over(Combos.chips):
        next_turn = switch_players(current_player)
    else:
        announce_winner()
        return False
    print ("It is {}'s turn.".format(next_turn.name))
    print (Combos.chips)
    roll = keep_or_reroll()
    score_the_roll(roll)
    Dice.roll = []




Combos.initialize_game()
while True:
    game()

