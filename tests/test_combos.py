import unittest
from yamslam.combos import *

class TestingYamSlam(unittest.TestCase):
    def test_a_yam_slam(self):
        self.assertEqual(ys.check([1, 1, 1, 1, 1]), True)

    def test_not_a_yam_slam(self):
        self.assertEqual(ys.check([1, 1, 1, 1, 2]), None)


class TestingLargeStraight(unittest.TestCase):
    def test_a_large_straight(self):
        self.assertEqual(ls.check([1, 2, 3, 4, 5]), True)

    def test_also_a_large_straight(self):
        self.assertEqual(ls.check([2, 3, 4, 5, 6]), True)

    def test_not_a_large_straight(self):
        self.assertEqual(ls.check([1, 2, 3, 4, 6]), None)


class TestingFourOfAKind(unittest.TestCase):
    def test_four_of_a_kind(self):
        self.assertEqual(fk.check([1, 1, 1, 5, 1]), True)

    def test_not_four_of_a_kind(self):
        self.assertEqual(fk.check([2, 2, 2, 3, 3]), None)

    def test_also_not_four_of_a_kind(self):
        self.assertEqual(fk.check([1, 1, 1, 2, 3]), None)


class TestingFullHouse(unittest.TestCase):
    def test_full_hosue(self):
        self.assertEqual(fh.check([1, 1, 5, 5, 5]), True)

    def test_also_full_house(self):
        self.assertEqual(fh.check([2, 2, 2, 3, 3]), True)

    def test_not_full_house(self):
        self.assertEqual(fh.check([1, 1, 1, 2, 3]), None)

    def test_also_not_full_house(self):
        self.assertEqual(fh.check([1, 1, 2, 2, 3]), None)


class TestingFlush(unittest.TestCase):
    def test_flush(self):
        self.assertEqual(fl.check([1, 1, 3, 5, 5]), True)

    def test_also_flush(self):
        self.assertEqual(fl.check([6, 4, 6, 4, 6]), True)

    def test_not_flush(self):
        self.assertEqual(fl.check([1, 1, 1, 2, 3]), None)

    def test_also_not_flush(self):
        self.assertEqual(fl.check([1, 1, 2, 2, 3]), None)


class TestingSmallStraight(unittest.TestCase):
    def test_small_straight(self):
        self.assertEqual(ss.check([1, 2, 3, 4, 4]), True)

    def test_also_small_straight(self):
        self.assertEqual(ss.check([2, 3, 4, 5, 5]), True)

    def test_another_small_straight(self):
        self.assertEqual(ss.check([2, 4, 1, 3, 6]), True)

    def test_not_a_small_straight(self):
        self.assertEqual(ss.check([2, 4, 3, 3, 6]), None)

    def test_also_not_a_small_straight(self):
        self.assertEqual(ss.check([1, 2, 3, 5, 6]), None)


class TestingThreeOfAKind(unittest.TestCase):
    def test_three_of_a_kind(self):
        self.assertEqual(tk.check([1, 2, 4, 4, 4]), True)

    def test_also_three_of_a_kind(self):
        self.assertEqual(tk.check([1, 1, 1, 4, 4]), True)

    def test_not_three_of_a_kind(self):
        self.assertEqual(tk.check([1, 2, 2, 4, 4]), None)

    def test_also_not_three_of_a_kind(self):
        self.assertEqual(tk.check([1, 2, 3, 4, 4]), None)


class TestingTwoPair(unittest.TestCase):
    def test_two_pair(self):
        self.assertEqual(tp.check([1, 1, 4, 4, 3]), True)

    def test_also_two_pair(self):
        self.assertEqual(tp.check([1, 1, 4, 4, 5]), True)

    def test_not_two_pair(self):
        self.assertEqual(tp.check([1, 1, 3, 5, 4]), None)