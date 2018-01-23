from criteria import Criteria

label = label
state = {} # X : 0
instr = "IF"

V = [(label, state, instr)] # Vertices, Nodes
E = [(v0, v1)] # Edges
prog = (V, E) # Graphe CFG

test = {} # X : 0
tests = [] # liste de tests

analyse_couverture(prog, [Criteria.TA, Criteria.TD, (Criteria.KTC, 2), ], tests)
