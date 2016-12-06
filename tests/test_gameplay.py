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
                    fk.name: 1,
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


class PointsAndWinner(unittest.TestCase):
    p1 = Players
    p2 = Players


    def test_adding_p1_points(self):
        self.assertEqual(add_points(p1, ls), 50)

    def test_adding_p2_points(self):
        self.assertEqual(add_points(p2, ss), 20)

    def test_adding_p1_pointsb(self):
        self.assertEqual(add_points(p1, tp), 55)

    def test_adding_p2_pointsb(self):
        self.assertEqual(add_points(p2, tk), 30)

    def test_winner(self):
        self.assertEqual(announce_winner(p1, p2), p1)
