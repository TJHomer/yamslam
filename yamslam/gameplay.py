from combos import *
from players import *
from dice import *


def check_if_game_over():
    #check to see if there are chips left
    #if there are no chips left, announce winner


def switch_players():
    pass


def get_remaining_chips():
    pass

def keep_or_reroll():
    pass


def score_the_roll():
    pass


def add_points():
    pass



def game():
    #check if game is over
    #announce what player is up
    #announce what chips are left
    #roll dice and get values
    #reroll if the player wants too
        #repeat if needed
    #score the roll depending on what chip is there
        #remove chip from inventory
    #add points to the current player and announce current score
    #switch players
    #reset dice
























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