import graph_functions as graph_func
from nodetype import NodeType
from criteria import Criteria
from instructions import Assign

def analyse_couverture(prog, criteria, tests):
    """
    Run each test of tests and return which criteria is verified and which isn't.
    For the criteria unverified, the function also return a #TODO

    Notation:
        - path is a list of tuple (node, edge, variables_state_after_the_edges)
        - paths is a set of path

    :param prog: tree (V, E) of the program
    :param criteria: list of Criteria to test
    :param tests: list of (dict) initial values

    :return
    """
    paths = []
    for test in tests:
        path = graph_func.parse(prog, test)
        paths.append(path)

    results = check_criteria(prog, criteria, paths)

    print(results)

def check_criteria(prog, criteria, paths):
    """
    Check every criteria in param criteria

    :param prog
    :param criteria : list of criteria
    :return result
    """
    results = {}
    for criterium, arg in criteria:
        if criterium == Criteria.TA:
            results['Criteria TA'] = check_criteriaTA(prog, paths)
        if criterium == Criteria.TD:
            results['Criteria TD'] = check_criteriaTD(prog, paths)
        if criterium == Criteria.KTC:
            results['Criteria %s-TC' % arg] = check_criteriaKTC(prog, paths, arg)
        if criterium == Criteria.ITB:
            results['Criteria %s-TB' % arg] = check_criteriaITB(prog, paths, arg)

    return results

def check_criteriaTA(prog, paths):
    """
    Check the criteria TA, i.e. every 'Assign edges' were passed through at least one time.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path
    :param k : k

    :return bool
    """
    graph, init_node, final_nodes = prog
    assign_edges = set()
    for edge, attr_dict in graph.edges.items():
        instr = attr_dict['instruction']
        if isinstance(instr, Assign):
            assign_edges.add(edge)

    for path in paths:
        for node, edge, variables in path:
            try:
                assign_edges.remove(edge)
            except KeyError:
                pass

    return not bool(assign_edges)

def check_criteriaTD(prog, paths):
    """
    Check the criteria TD, i.e. every 'If nodes' and 'While nodes' were
    evaluated true at least one time AND evaluted false at least one time.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path
    :param k : k

    :return bool
    """
    graph, init_node, final_nodes = prog
    decisions_nodes_edges = set()
    for node, attr_dict in graph.nodes.items():
        node_type = attr_dict['node_type']
        if node_type in {NodeType.IF, NodeType.WHILE}:
            decisions_nodes_edges |= {edge for edge in graph.edges if edge[0] == node}

    for path in paths:
        for node, edge, variables in path:
            try:
                decisions_nodes_edges.remove(edge)
            except KeyError:
                pass

    return not bool(decisions_nodes_edges)

def check_criteriaKTC(prog, paths, k):
    """
    Check the criteria k-TC, i.e. every 'smaller than k paths' were
    executed at least one time.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path
    :param k : k

    :return bool
    """
    graph, init_node, final_nodes = prog
    smaller_than_k_paths = []
    for final_node in final_nodes:
        final_node_paths = graph_func.listSmallerThanKPaths(graph, init_node, final_node, k)
        smaller_than_k_paths += final_node_paths
    # print(smaller_than_k_paths)

    for path in paths:
        node_path = [node for (node, edge, var) in path]
        # print(node_path)
        try:
            smaller_than_k_paths.remove(node_path)
        except KeyError:
            pass

    return not bool(smaller_than_k_paths)

def check_criteriaITB(prog, paths, i):
    """
    Check the criteria i-TB, i.e. every path in which the while loop are
    executed at MOST i time are in paths.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path
    :param i : i

    :return bool
    """
    #TODO
    return False
