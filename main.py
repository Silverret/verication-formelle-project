from criteria import Criteria
from nodetype import NodeType
from instructions import Assign, If, Skip, While
from condition import Condition, BooleanOperator
from arithmetic_expression import Add, Minus, Time

label = label
state = {} # X : 0
instr = "IF"

V = [(label, state, instr)] # Vertices, Nodes
E = [(node_d, node_a, cond, instr)] # Edges
prog = (V, E) # Graphe CFG

test = {} # X : 0
tests = [] # liste de tests


analyse_couverture(prog, [Criteria.TA], tests)

Variables = {'X': None}
v1 = (1, Variables, NodeType.IF)
v2 = (2, Variables, NodeType.NONE)
v3 = (3, Variables, NodeType.NONE)
v4 = (4, Variables, NodeType.IF)
v5 = (5, Variables, NodeType.NONE)
v6 = (6, Variables, NodeType.NONE)
v7 = ('_', Variables, NodeType.NONE)

V = [v1, v2, v3, v4, v5, v6, v7]

e1 = (v1, v2, Condition(Variables['X'], 0, "<="), Skip())
e2 = (v1, v3, Condition(Condition(Variables['X'], 0, "<="), operator = "NOT"), Skip())
e3 = (v2, v4, Condition(True), Assign(Variables['X'], Minus(0,Variables['X'])))
e4 = (v3, v4, Condition(True), Assign(Variables['X'], Minus(1, Variables['X'])))
e5 = (v4, v5, Condition(Variables['X'], 1, "="), Skip())
e6 = (v4, v5, Condition(Condition(Variables['X'], 1, "="), operator = "NOT"), Skip())
e7 = (v5, v7, Condition(True), Assign(Variables['X'], 1))
e8 = (v6, v7, Condition(True), Assign(Variables['X'], Add(Variables['X'], 1)))

E = [e1, e2, e3, e4, e5, e6, e7, e8]







