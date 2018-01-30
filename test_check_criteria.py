import unittest

import I_Analyse_de_couverture as cc
from trees import PROG
from criteria import Criteria


class CheckCriteriaTest(unittest.TestCase):

    def setUp(self):
        self.paths = []
        self.paths.append([
            (1, (1, 2), {'X': -5}),
            (2, (2, 4), {'X': 5}),
            (4, (4, 6), {'X': 5}),
            (6, (6, '_'), {'X': 6}),
            ('_', None, {'X': 6})])
        self.paths.append([
            (1, (1, 3), {'X': 5}),
            (3, (3, 4), {'X': -4}),
            (4, (4, 6), {'X': -4}),
            (6, (6, '_'), {'X': -3}),
            ('_', None, {'X': -3})])
        self.paths.append([
            (1, (1, 2), {'X': -1}),
            (2, (2, 4), {'X': 1}),
            (4, (4, 5), {'X': 1}),
            (5, (5, '_'), {'X': 1}),
            ('_', None, {'X': 1})])

        self.prog = PROG

    def test_check_criteriaTA(self):
        result = cc.check_criteriaTA(self.prog, self.paths)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
