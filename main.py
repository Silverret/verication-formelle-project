import networkx as nx
import matplotlib.pyplot as plt

import boolean_expression as bexp
import arithmetic_expression as aexp
import instructions as inst

from nodetype import NodeType
from criteria import Criteria

from I_Analyse_de_couverture import analyse_couverture

from trees import T, W, X


PROG1 = T, 1, {'_'}
PROG2 = W, 1, {'_'}

"""
Tests (list) : set of tests
"""
TESTS = []
TESTS.append({X: -1})
TESTS.append({X: 5})
TESTS.append({X: -8})


CRITERIA = [
    (Criteria.TA, None),
    (Criteria.TD, None),
    (Criteria.KTC, 5)
]

if __name__ == '__main__':
    analyse_couverture(PROG1, CRITERIA, TESTS)
    analyse_couverture(PROG2, CRITERIA, TESTS)
