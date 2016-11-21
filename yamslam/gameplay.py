


class Gameplay():
    chips = {
        'Large Straight': 0,
        'Four of a kind': 0,
        'Full House': 0,
        'Flush': 0,
        'Small Straight': 0,
        'Three of a kind': 0,
        'Two Pair': 0

    }

    def initialize_game(self):
        Gameplay.chips['Large Straight'] = 4
        Gameplay.chips['Four of a kind'] = 4
        Gameplay.chips['Full House'] = 4
        Gameplay.chips['Flush'] = 4
        Gameplay.chips['Small Straight'] = 4
        Gameplay.chips['Three of a kind'] = 4
        Gameplay.chips['Two Pair'] = 4

    def keep_or_reroll():
        reroll = [0,0,0,0,0]
        for i in range(1,3):
            Score.throw_a_roll(len(reroll))
            print(Score.get_roll_values())
            print('Type the numbers you would like to reroll')
            print('or type N to keep this roll')
            choice = input('')
            if choice == N:
                break
            else:
                choice = choice.replace(',', '')
                choice = choice.replace(' ', '')
                reroll = [int(i) for i in choice]
                for number in reroll:
                    for self in Dice.dice_set:
                        if number == self.value:
                            Score.roll.remove(self)
                

    def turn():
        current_player = p1.name
        print (Gameplay.chips)
        print ("It is {}'s turn".format(current_player))
        Gameplay.keep_or_reroll()
        Score.throw_a_roll(5 - len(Score.roll))
        print(Score.get_roll_values())
        print (Score.score_the_roll())



        # asks the player if they want to keep some dice or roll again
        # rolls again
        # asks and rolls again
        # scores the roll
        # adds the score to the player and reduces the number of chips
        # tells the score
        # switches the player

Gameplay.initialize_game()

Gameplay.turn()
