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
        Test_dict = {ls.name: 0,
                    fk.name: 0,
                    fh.name: 0,
                    fl.name: 0,
                    ss.name: 0,
                    tk.name: 0,
                    tp.name: 0}


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



class TestWinningRolls(unittest.TestCase):
    Combos.chips = {ls.name: 1,
                        fk.name: 1,
                        fh.name: 1,
                        fl.name: 1,
                        ss.name: 1,
                        tk.name: 1,
                        tp.name: 1}


    def test_turn_a(self):
        self.assertEqual(score_the_roll([1, 2, 3, 4, 5]), ls)

    def test_turn_b(self):
        self.assertEqual(score_the_roll([1, 2, 3, 4, 5]), ss)

    def test_turn_c(self):
        self.assertEqual(score_the_roll([1, 2, 3, 4, 5]), None)

    def test_turn_d(self):
        self.assertEqual(score_the_roll([5, 5, 5, 5, 5]), fk)

    def test_turn_e(self):
        self.assertEqual(score_the_roll([5, 5, 5, 5, 4]), tk)

    def test_turn_f(self):
        self.assertEqual(score_the_roll([5, 5, 5, 4, 5]), tp)

    def test_turn_g(self):
        self.assertEqual(score_the_roll([5, 5, 3, 3, 3]), fh)

    def test_turn_h(self):
        self.assertEqual(score_the_roll([5, 5, 3, 3, 3]), fl)

    def test_turn_i(self):
        self.assertEqual(score_the_roll([5, 5, 3, 3, 3]), None)