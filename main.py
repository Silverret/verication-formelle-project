from criteria import Criteria
from nodetype import NodeType
from instructions import Assign, If, Skip, While

label = label
state = {} # X : 0
instr = "IF"

V = [(label, state, instr)] # Vertices, Nodes
E = [(node_d, node_a, cond, instr)] # Edges
prog = (V, E) # Graphe CFG

test = {} # X : 0
tests = [] # liste de tests


analyse_couverture(prog, [Criteria.TA], tests)

V = [v1, v2, v3, v4, v5, v6, v7]
v1 = (1, {}, NodeType.IF)
v2 = (2, {}, NodeType.NONE)
v3 = (3, {}, NodeType.NONE)
v4 = (4, {}, NodeType.IF)
v5 = (5, {}, NodeType.NONE)
v6 = (6, {}, NodeType.NONE)
v7 = (_, {}, NodeType.NONE)

E = [e1, e2, e3, e4, e5, e6, e7, e8]

e1 = (v1, v2, X <= 0, Skip)
e2 = (v1, v3, X > 0, Skip)
e3 = (v2, v4, True, Assign)
e4 = (v3, v4, True, Assign)
e5 = (v4, v5, X == 1, Skip)
e6 = (v4, v5, X != 1, Skip)
e7 = (v5, v7, True, Assign)
e8 = (v6, v7, True, Assign)







