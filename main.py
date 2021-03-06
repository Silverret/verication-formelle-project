import networkx as nx
import matplotlib.pyplot as plt

import IV_Classes.boolean_expression as bexp
import IV_Classes.arithmetic_expression as aexp
import IV_Classes.instructions as inst

from IV_Classes.nodetype import NodeType
from IV_Classes.criteria import Criteria

from I_Analyse_de_couverture import analyse_coverage
from II_Generation_de_tests import generate_tests

from trees import T, W, X


PROG1 = T, 1, {'_'}, {X}
PROG2 = W, 1, {'_'}, {X}

"""
Tests (list) : set of tests
"""
TESTS = []
TESTS.append({X: -1})
TESTS.append({X: 5})
TESTS.append({X: -8})
TESTS.append({X: -10})


CRITERIA = [
    (Criteria.TA, None),
    (Criteria.TD, None),
    (Criteria.KTC, 5),
    (Criteria.ITB, 1),
    (Criteria.TDEF, None),
    (Criteria.TU, None),
    (Criteria.TDU, None),
    (Criteria.TC, None)
]

if __name__ == '__main__':
    generate_tests(PROG1, Criteria.TA)

    """
    RESULT1 = analyse_coverage(PROG1, CRITERIA, TESTS)
    RESULT2 = analyse_coverage(PROG2, CRITERIA, TESTS)

    print("Results for Prog1")
    for crit, res in RESULT1.items():
        percentage, uncovered_set = res
        print(f"\t {crit}: {percentage}, {uncovered_set}")

    
    print("\n\nResults for Prog2")
    for crit, res in RESULT2.items():
        percentage, uncovered_set = res
        print(f"\t {crit}: {percentage}, {uncovered_set}")
    """
    

    
