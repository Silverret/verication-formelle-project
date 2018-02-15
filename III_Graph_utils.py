import IV_Classes.instructions as inst
import IV_Classes.arithmetic_expression as aexp
from IV_Classes.nodetype import NodeType
from IV_Classes.instructions import Assign
import networkx as nx

def parse(prog, test):
    """
    Parses a prog for a test

    :param prog: graph, node, final_nodes
    :param test: dictionary of variables and value
    """
    for variable in test:
        variable.value = test[variable]
    graph, node, final_nodes, _ = prog
    path = []
    while node not in final_nodes:
        for e in graph.out_edges(node):
            attr = graph.get_edge_data(e[0], e[1])
            if not attr['decision']():
                pass
            else:
                path.append((node, e, {variable : variable.value for variable in test}))
                attr['instruction'].execute()
                node = e[1]
    path.append((node, None, {variable : variable.value for variable in test}))
    return tuple(path)


def ref_function(graph, node):
    """
    Returns a list of variables that are:
    - In a boolean expression in the decision of an exiting edge
    - In the right term of an a assign expression (other_vars = exp(var)) in the instruction of an exiting edge
    
    :param graph
    :param node: any node of the graph
    """
    ref_var = []
    for edge, edge_attr in graph.edges.items():
        if node == edge[0]: 
            decision = edge_attr['decision']
            instruction = edge_attr['instruction']
            variables = check_variables(decision)
            ref_var += variables
            if isinstance(instruction, inst.Assign):
                # y is the right term of our "Assign" method
                variables = check_variables(instruction.y)
                ref_var += variables
    return ref_var


def check_variables(expressions):
    """
    recursive function to check the variables used in expressions
    """
    variables = []
    for variable in expressions.__dict__.values():
        if isinstance(variable, aexp.Variable):
            variables.append(variable)
        elif variable is None or isinstance(variable, int) or isinstance(variable, str):
            pass
        else:
            check_variables(variable)
    return variables


def def_function(graph, node):
    """
    Returns a list of variables that are in the left term
    of an assign expression (var = exp(other_vars)) on the exiting edges of the node
    
    :param graph
    :param node: any node of the graph
    """
    def_var = []
    for edge, edge_attr in graph.edges.items():
        if node == edge[0]: 
            instruction = edge_attr['instruction']
            if isinstance(instruction, inst.Assign):
                # x is the left term of our "Assign" method
                variable = instruction.x
                def_var.append(variable)
    return def_var


def get_smaller_than_k_paths_util(graph, u, d, path, paths, k):
    """
    A recursive function to print all smaller than k paths from 'u' to 'd'.

    :param graph
    :param u: origin vertice
    :param d: destination vertice
    :param path[] stores actual vertices.
    :param paths{} is the set of found paths.
    :param k
    """

    # Mark the current node as visited and store in path
    path.append(u)

    # If current vertex is same as destination, then print
    # current path[]
    if len(path) > k:
        pass
    elif u == d:
        paths.add(tuple(path.copy()))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for _, i in graph.out_edges(u):
            get_smaller_than_k_paths_util(graph, i, d, path, paths, k)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()


def get_smaller_than_k_paths(graph, s, d, k):
    """
    Lists all smaller than k paths from 's' to 'd'
    """
    # Create an array to store paths
    path = []
    paths = set()

    # Call the recursive helper function to list all paths
    get_smaller_than_k_paths_util(graph, s, d, path, paths, k)

    return paths


def path_used_def(graph, variable, def_node, path):
    """
    Return a boolean, true if :param path:
        - goes through :param def_node
        - doesn't go through a other def node (on the same Variable)
          until it goes through a ref node of :param variable
    
    :param graph
    :param variable
    :param def_node
    :param ref_node
    :param path
    """
    nodes = [n for (n, _, _) in path]

    # Condition 1
    if def_node not in nodes:
        return False

    # Condition 2
    for node in nodes[nodes.index(def_node)+1:]:
        if variable in ref_function(graph, node):
            return True
        if variable in def_function(graph, node):
            return False
    
    return False

def path_used_def_ref(graph, variable, def_node, ref_node, path):
    """
    Return a boolean, true if :param path:
        - goes through :param def_node then :param ref_node
        - doesn't go through a other def node (on the same Variable)
          between :param def_node and :param ref_node
    
    :param graph
    :param variable
    :param def_node
    :param ref_node
    :param path
    """
    nodes = [n for (n, _, _) in path]

    # Condition 1
    if def_node not in nodes or ref_node not in nodes[nodes.index(def_node):]:
        return False

    # Condition 2
    for node in nodes[nodes.index(def_node)+1:nodes.index(ref_node)]:
        if variable in def_function(graph, node):
            return False
    return True

def get_decision_edges(graph):
    decision_edges = set()
    for node, attr_dict in graph.nodes.items():
        node_type = attr_dict['node_type']
        if node_type in {NodeType.IF, NodeType.WHILE}:
            decision_edges |=  set(graph.out_edges(node))
    return decision_edges

def get_assign_edges(graph):
    assign_edges = set()
    for edge, attr_dict in graph.edges.items():
        instr = attr_dict['instruction']
        if isinstance(instr, Assign):
            assign_edges.add(edge)
    return assign_edges

def add_loops(graph, s, d, paths):
    simple_cycles = nx.simple_cycles(graph)
    new_paths = list(nx.all_simple_paths(graph, s, d))
    for cycle in simple_cycles:
        for path in paths:
            if cycle[0] in path:
                index = path.index(cycle[0])
                new_path = list(path)
                new_path[index:index] = cycle
                new_paths.append(new_path)
    return new_paths

def get_i_loops_paths(graph, s, d, i):
    """
    Lists all paths with smaller that i loops from 's' to 'd'
    """
    paths = nx.all_simple_paths(graph, s, d)
    j = 0
    if i == 0:
        return paths
    else:
        while j < i:
            paths = add_loops(graph, s, d, paths)
            j += 1
    set_paths = set()
    for path in paths:
        set_paths.add(tuple(path.copy()))
    # to convert the list into set
    return set_paths



