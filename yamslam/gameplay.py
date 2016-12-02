from combos import *
from players import *
from dice import *


current_player = p2


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
        new_roll = len(reroll)
        Dice.throw_a_roll(new_roll)
        print(Dice.get_roll_values())
        print('Type the numbers you would like to reroll')
        print('or press enter to keep this roll')
        choice = input('')
        if choice == '':
            return reroll
        else:
            choice = choice.replace(',', '')
            choice = choice.replace(' ', '')
            reroll = [int(i) for i in choice]
            for number in reroll:
                for self in Dice.dice_set:
                    if number == self.value:
                        Dice.roll.remove(self)
    return reroll


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
        switch_players(current_player)
    else:
        return False
    print ("It is {}'s turn.".format(current_player.name))
    print (Combos.chips)
    roll_values = keep_or_reroll()
    if score_the_roll(roll_values):
        winning_roll = score_the_roll(roll_values)
        print ('You got {}!'.format(winning_roll.name))
        add_points(winning_roll)
    else:
        print ('Sorry, you got nothing.')
    print('Current score: {}: {}  {}: {}'.format(p1.name, p1.points, p2.name, p2.points))
    Dice.roll = []


























'''
class Gameplay:
    current_player = p1.name

    @classmethod
    def score_the_roll(cls):
        for combo in Combos.combos:
            if Combos.chips[combo.name] != 0:
                if combo.check():
                    Combos.chips[combo.name] -= 1
                    Gameplay.current_player.points += combo.points
                    return 'You got a {}!\n You got {} points!'.format(combo.name, combo.points)
        else:
            return 'You got nothing, try again.'


    @classmethod
    def keep_or_reroll(cls):
        reroll = [0, 0, 0, 0, 0]
        for i in range(1, 3):
            new_roll = len(reroll)
            Dice.throw_a_roll(new_roll)
            print(Dice.get_roll_values())
            print('Type the numbers you would like to reroll')
            print('or press enter to keep this roll')
            choice = input('')
            if choice == '':
                break
            else:
                choice = choice.replace(',', '')
                choice = choice.replace(' ', '')
                reroll = [int(i) for i in choice]
                for number in reroll:
                    for self in Dice.dice_set:
                        if number == self.value:
                            Dice.roll.remove(self)

    @classmethod
    def switch_turn(cls):
        if Gameplay.current_player == p1.name:
            Gameplay.current_player = p2.name
        else:
            Gameplay.current_player = p1.name
        Dice.roll = []

    @classmethod
    def turn(cls):
        print (Combos.chips)
        print ("It is {}'s turn".format(Gameplay.current_player))
        Gameplay.keep_or_reroll()
        Dice.throw_a_roll(5 - len(Dice.roll))
        print(Dice.get_roll_values())
        print (Gameplay.score_the_roll())
        Gameplay.switch_turn()



print(Combos.combos)
Combos.initialize_game()
Gameplay.turn()
Gameplay.turn()
Gameplay.turn()
Gameplay.turn()
Gameplay.turn()
'''

Combos.initialize_game()
while True:
    game()