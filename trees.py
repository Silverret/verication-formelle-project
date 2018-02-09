import networkx as nx
import matplotlib.pyplot as plt
import inspect

import IV_Classes.boolean_expression as bexp
import IV_Classes.arithmetic_expression as aexp
import IV_Classes.instructions as instr
from IV_Classes.nodetype import NodeType


"""
Variables (dict) : keys are variable's name (string), value are variable's value (integer)
"""

X = aexp.Variable('X')
Y = aexp.Variable('Y')

"""
First graph, same as the one in the homework's instruction
"""
T = nx.DiGraph()

"""
Nodes : label, type
"""
T.add_node(1, node_type=NodeType.IF)
T.add_node(2, node_type=NodeType.NONE)
T.add_node(3, node_type=NodeType.NONE)
T.add_node(4, node_type=NodeType.IF)
T.add_node(5, node_type=NodeType.NONE)
T.add_node(6, node_type=NodeType.NONE)
T.add_node('_', node_type=NodeType.NONE)

"""
Edges : origin node, destination node, decision, instruction
"""

T.add_edge(1, 2, decision=bexp.InferiorOrEqual(X, 0), instruction=instr.Skip())
T.add_edge(1, 3, decision=bexp.Not(bexp.InferiorOrEqual(X, 0)), instruction=instr.Skip())
T.add_edge(2, 4, decision=bexp.BooleanExpression("true"), instruction=instr.Assign(X, aexp.Minus(0, X)))
T.add_edge(3, 4, decision=bexp.BooleanExpression("true"), instruction=instr.Assign(X, aexp.Minus(1, X)))
T.add_edge(4, 5, decision=bexp.Equal(X, 1), instruction=instr.Skip())
T.add_edge(4, 6, decision=bexp.Not(bexp.Equal(X, 1)), instruction=instr.Skip())
T.add_edge(5, '_', decision=bexp.BooleanExpression("true"), instruction=instr.Assign(X, 1))
T.add_edge(6, '_', decision=bexp.BooleanExpression("true"), instruction=instr.Assign(X, aexp.Add(X, 1)))

"""
Second graph, similar to the first one, but with a while loop 
"""
W = nx.DiGraph()

"""
Nodes : label, Wype
"""
W.add_node(1, node_type=NodeType.IF)
W.add_node(2, node_type=NodeType.NONE)
W.add_node(3, node_type=NodeType.NONE)
W.add_node(4, node_type=NodeType.IF)
W.add_node(5, node_type=NodeType.NONE)
W.add_node('_', node_type=NodeType.NONE)

"""
Edges : origin node, destination node, decision, instruction
"""

W.add_edge(1, 2, decision=bexp.InferiorOrEqual(X, 0), instruction=instr.Skip())
W.add_edge(1, 3, decision=bexp.Not(bexp.InferiorOrEqual(X, 0)), instruction=instr.Skip())
W.add_edge(2, 4, decision=bexp.BooleanExpression("true"), instruction=instr.Assign(X, aexp.Minus(0, X)))
W.add_edge(3, 4, decision=bexp.BooleanExpression("true"), instruction=instr.Assign(X, aexp.Minus(1, X)))
W.add_edge(4, 5, decision=bexp.InferiorOrEqual(X, 1), instruction=instr.Skip())
W.add_edge(5, 4, decision=bexp.BooleanExpression("true"), instruction=instr.Assign(X, aexp.Add(X, 1)))
W.add_edge(4, '_', decision=bexp.Not(bexp.InferiorOrEqual(X, 1)), instruction=instr.Skip())


#nx.draw(W, with_labels = True)
#nx.draw(T, with_labels = True)
#plt.draw()
#plt.show()