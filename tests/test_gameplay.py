import unittest
from yamslam.gameplay import *
from yamslam.combos import *
from yamslam.players import *


class SwitchingPlayersTest(unittest.TestCase):
    def test_p1_to_p2(self):
        self.assertEqual(switch_players(p1), p2)

    def test_p2_to_p1(self):
        self.assertEqual(switch_players(p2), p1)



class CheckIfGameOverTest(unittest.TestCase):
    def test_game_is_not_over(self):
        Test_dict = {ls.name: 0,
                    'Four of a kind': 1,
                    fh.name: 0,
                    fl.name: 0,
                    ss.name: 4,
                    tk.name: 2,
                    tp.name: 3}


        self.assertEqual(check_if_game_over(Test_dict),True)

    def test_game_over(self):
        Test_dict = {'Large Straight': 0,
                    'Four of a kind': 0,
                    'Full House': 0,
                    'Flush': 0,
                    'Small Straight': 0,
                    'Three of a kind': 0,
                    'Two pair': 0}


        self.assertEqual(check_if_game_over(Test_dict),False)