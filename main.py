from criteria import Criteria

label = label
state = {} # X : 0
instr = "IF"

V = [(label, state, instr)] # Vertices, Nodes
E = [(node_d, node_a, cond, instr)] # Edges
prog = (V, E) # Graphe CFG

test = {} # X : 0
tests = [] # liste de tests


analyse_couverture(prog, [Criteria.TA], tests)
