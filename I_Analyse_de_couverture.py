import networkx as nx

import arithmetic_expression as aexp
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
    """
    paths = []
    for test in tests:
        paths.append(parse(prog, test))
    """
    X = aexp.Variable('X')
    paths = []
    paths.append([
        (1, (1, 2), {X: -5}),
        (2, (2, 4), {X: 5}),
        (4, (4, 6), {X: 5}),
        (6, (6, '_'), {X: 6}),
        ('_', None, {X: 6})])
    paths.append([
        (1, (1, 3), {X: 5}),
        (3, (3, 4), {X: -4}),
        (4, (4, 6), {X: -4}),
        (6, (6, '_'), {X: -3}),
        ('_', None, {X: -3})])
    paths.append([
        (1, (1, 2), {X: -1}),
        (2, (2, 4), {X: 1}),
        (4, (4, 5), {X: 1}),
        (5, (5, '_'), {X: 1}),
        ('_', None, {X: 1})])

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
    for criterium in criteria:
        if criterium == Criteria.TA:
            results['Criteria TA'] = check_criteriaTA(prog, paths)
        if criterium == Criteria.TD:
            results['Criteria TD'] = check_criteriaTD(prog, paths)

    return results

def check_criteriaTA(prog, paths):
    """
    Check the criteria TA, i.e. every 'Assign edges' were passed through at least one time.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : set of path

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
    :param paths : set of path

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

