from yamslam.combos import *
from yamslam.players import *
from yamslam.dice import *


current_player = p2
roll = []





def check_if_game_over():
    for combo in Combos.combos:
        if Combos.chips[combo.name] != 0:
            return True
        else:
            announce_winner()


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
            return Dice.roll
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
    return Dice.roll



def score_the_roll(winning_roll):
    print(winning_roll)
    for combo in Combos.combos:
        if Combos.chips[combo.name] != 0:
            if combo.check():
                Combos.chips[combo.name] -= 1
                return combo
    else:
        return None


def add_points(combo):
    current_player.points += combo.points




def game():
    if check_if_game_over():
        next_turn = switch_players(current_player)
    else:
        return False
    print ("It is {}'s turn.".format(next_turn.name))
    print (Combos.chips)
    score_the_roll(keep_or_reroll())

    '''
    keep_or_reroll()
    if score_the_roll(roll_values):
        winning_roll = score_the_roll(roll_values)
        print ('You got {}!'.format(winning_roll.name))
        add_points(winning_roll)
    else:
        print ('Sorry, you got nothing.')
    print('Current score: {}: {}  {}: {}'.format(p1.name, p1.points, p2.name, p2.points))
    Dice.roll = []
'''


Combos.initialize_game()
game()


