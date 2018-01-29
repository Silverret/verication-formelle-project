import networkx as nx 
import boolean_expression as bexp
import arithmetic_expression as aexp
import instructions as inst
from nodetype import NodeType
import matplotlib.pyplot as plt

"""
Variables (dict) : keys are variable's name (string), value are variable's value (integer)
"""
X = aexp.Variable('X')

T = nx.Graph()

"""
Nodes : label, type
"""
T.add_node(1, node_type = NodeType.IF)
T.add_node(2, node_type = NodeType.NONE)
T.add_node(3, node_type = NodeType.NONE)
T.add_node(4, node_type = NodeType.IF)
T.add_node(5, node_type = NodeType.NONE)
T.add_node(6, node_type = NodeType.NONE)
T.add_node('_', node_type = NodeType.NONE)

"""
Edges : origin node, destination node, condition, instruction
"""

T.add_edge(1, 2, condition = bexp.InferiorOrEqual(X, 0), instruction = inst.Skip()) 
T.add_edge(1, 3, condition = bexp.Not(bexp.InferiorOrEqual(X, 0)), instruction = inst.Skip())
T.add_edge(2, 4, condition = bexp.BooleanExpression("true"), instruction = inst.Assign(X, aexp.Minus(0, X)))
T.add_edge(3, 4, condition = bexp.BooleanExpression("true"), instruction = inst.Assign(X, aexp.Minus(1, X)))
T.add_edge(4, 5, condition = bexp.Equal(X, 1), instruction = inst.Skip())
T.add_edge(4, 6, condition = bexp.Not(bexp.Equal(X, 1)), instruction = inst.Skip())
T.add_edge(5, '_', condition = bexp.BooleanExpression("true"), instruction = inst.Assign(X, 1))
T.add_edge(6, '_', condition = bexp.BooleanExpression("true"), instruction = inst.Assign(X, aexp.Add(X, 1)))



print(T.edges(data=True))
