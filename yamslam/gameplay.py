from yamslam.combos import *
from yamslam.players import *
from yamslam.dice import *
import time


def check_if_game_over(chips):
    chips_left = 0
    for i in chips.values():
        chips_left += i
    if chips_left == 0:
        return False
    else:
        return True


def announce_winner(player_one, player_two):
    if player_two.points > player_one.points:
        print ('Game over! {} is the winner!'.format(player_two.name))
        return p2

    else:
        print ('Game over! {} is the winner!'.format(player_one.name))
        return p1


def switch_players(new_player):
    if new_player == p2:
        current_player = p1
    else:
        current_player = p2
    return current_player


def keep_or_reroll():
    for i in range(1, 3):
        Dice.throw_a_roll(5 - len(Dice.roll))
        print(Dice.get_roll_values())
        time.sleep(.8)
        print('\nType the numbers you would like to reroll,')
        print('or press enter to keep this roll.\n')
        choice = list(input(''))
        if choice == []:
            return Dice.get_roll_values()
        reroll = []
        for i in choice:
            try:
                if 0 < int(i) < 7:
                    reroll.append(i)
            except(ValueError):
                continue
        for self in Dice.dice_set:
            for number in reroll:
                if int(number) in Dice.get_roll_values():
                    if int(number) == self.value:
                       Dice.roll.remove(self)
    Dice.throw_a_roll(5 - len(Dice.roll))
    print(Dice.get_roll_values())
    return Dice.get_roll_values()


def score_the_roll(winning_roll):
    for combo in Combos.combos:
        if Combos.chips[combo.name] != 0:
            if combo.check(winning_roll):
                Combos.chips[combo.name] -= 1
                return combo
    else:
        print('Sorry, you got nothing.')
        return None


def add_points(current_player, combo):
    if combo == None:
        current_player.points += 0
    else:
        current_player.points += combo.points
    return current_player.points


def game(current_player):
    print (Combos.chips)
    print("\nIt is {}'s turn.\n".format(current_player.name))
    time.sleep(.5)
    roll = keep_or_reroll()
    winning_combo = score_the_roll(roll)
    add_points(current_player, winning_combo)
    time.sleep(1)
    print ('\n{} has {} points.\n'.format(current_player.name, current_player.points))
    time.sleep(.5)
    Dice.roll = []


Combos.initialize_game()
current_player = p1
while True:
    game(current_player)
    current_player = switch_players(current_player)
    if check_if_game_over(Combos.chips):
        pass
    else:
        announce_winner(p1, p2)
        break

