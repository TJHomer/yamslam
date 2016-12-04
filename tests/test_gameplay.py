import unittest
from yamslam.gameplay import *
from yamslam.combos import *
from yamslam.players import *


class SwitchingPlayersTest(unittest.TestCase):
    def test_p1_to_p2(self):
        self.assertEqual(switch_players(p1), p2)

    def test_p2_to_p1(self):
        self.assertEqual(switch_players(p2), p1)



