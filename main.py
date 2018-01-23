from criteria import Criteria
from nodetype import NodeType
from instructions import Assign, If, Skip, While
from boolean_expression import BooleanExpression, Not, And, Or, Equal, InferiorOrEqual
from arithmetic_expression import Variables, Add, Minus, Time

from I_Analyse_de_couverture import analyse_couverture

"""
Variables (dict) : keys are variable's name (string), value are variable's value (integer)
"""
Variables = {'X': None}

"""
Vertice (tuple) : label, Variables (see above), NodeType
"""
v1 = (1, Variables, NodeType.IF)
v2 = (2, Variables, NodeType.NONE)
v3 = (3, Variables, NodeType.NONE)
v4 = (4, Variables, NodeType.IF)
v5 = (5, Variables, NodeType.NONE)
v6 = (6, Variables, NodeType.NONE)
v7 = ('_', Variables, NodeType.NONE) #TODO
V = [v1, v2, v3, v4, v5, v6, v7]

"""
Edge (tuple) = origin node, destination node, Condition, Instruction
"""
e1 = (v1, v2, InferiorOrEqual(Variables['X'], 0), Skip())
e2 = (v1, v3, Not(InferiorOrEqual(Variables['X'], 0)), Skip())
e3 = (v2, v4, BooleanExpression("true"), Assign(Variables['X'], Minus(0, Variables['X'])))
e4 = (v3, v4, BooleanExpression("true"), Assign(Variables['X'], Minus(1, Variables['X'])))
e5 = (v4, v5, Equal(Variables['X'], 1), Skip())
e6 = (v4, v5, Not(Equal(Variables['X'], 1)), Skip())
e7 = (v5, v7, BooleanExpression("true"), Assign(Variables['X'], 1))
e8 = (v6, v7, BooleanExpression("true"), Assign(Variables['X'], Add(Variables['X'], 1)))
E = [e1, e2, e3, e4, e5, e6, e7, e8]

"""
Program (tuple) : (Vertices, Edges, entry node, final node)
"""
prog = (V, E)

"""
Tests (list) : list of tests
"""
tests = []

analyse_couverture(prog, [Criteria.TA], tests)
