from criteria import Criteria
from nodetype import NodeType
from instructions import Assign, If, Skip, While
from boolean_expression import BooleanExpression, Not, And, Or, Equal, InferiorOrEqual
from arithmetic_expression import Variable, Add, Minus, Time

from I_Analyse_de_couverture import analyse_couverture

"""
Variables (dict) : keys are variable's name (string), value are variable's value (integer)
"""
X = Variable('X')
"""
Vertice (tuple) : label, Variables (see above), NodeType
"""
v1 = (1, NodeType.IF)
v2 = (2, NodeType.NONE)
v3 = (3, NodeType.NONE)
v4 = (4, NodeType.IF)
v5 = (5, NodeType.NONE)
v6 = (6, NodeType.NONE)
v7 = ('_', NodeType.NONE) #TODO
V = [v1, v2, v3, v4, v5, v6, v7]

"""
Edge (tuple) = origin node, destination node, Condition, Instruction
"""
e1 = (v1, v2, InferiorOrEqual(X, 0), Skip())
e2 = (v1, v3, Not(InferiorOrEqual(X, 0)), Skip())
e3 = (v2, v4, BooleanExpression("true"), Assign(X, Minus(0, X)))
e4 = (v3, v4, BooleanExpression("true"), Assign(X, Minus(1, X)))
e5 = (v4, v5, Equal(X, 1), Skip())
e6 = (v4, v5, Not(Equal(X, 1)), Skip())
e7 = (v5, v7, BooleanExpression("true"), Assign(X, 1))
e8 = (v6, v7, BooleanExpression("true"), Assign(X, Add(X, 1)))
E = [e1, e2, e3, e4, e5, e6, e7, e8]

"""
Program (tuple) : (Vertices, Edges, entry node, final node)
"""
prog = (V, E)

"""
Tests (list) : set of tests
"""
tests = set()
tests.add({X: -1})
tests.add({X: 5})
tests.add({X: -8})

analyse_couverture(prog, [Criteria.TA], tests)
