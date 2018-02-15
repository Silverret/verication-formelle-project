import networkx as nx

import III_Graph_utils as gutils
import IV_Classes.boolean_expression as bexp
from IV_Classes.nodetype import NodeType
from IV_Classes.criteria import Criteria
from IV_Classes.instructions import Assign

def analyse_coverage(prog, criteria, tests):
    """
    Run each test of tests and return which criteria is verified and which isn't.

    Notation:
        - path is a list of tuple (node, edge, variables_state_after_the_edges)
        - paths is a set of path

    :param prog: tree (V, E) of the program
    :param criteria: list of Criteria to test
    :param tests: list of (dict) initial values

    :return {Criterium.name : (coverage percentage, no-covered elements)}
    """
    paths = []
    for test in tests:
        path = gutils.parse(prog, test)
        paths.append(path)

    return check_criteria(prog, criteria, paths)


def check_criteria(prog, criteria, paths):
    """
    Check every criteria in :param criteria

    :param prog
    :param criteria[] : list of criteria
    :return result
    """
    results = {}
    for criterium, arg in criteria:
        if criterium == Criteria.TA:
            results['Criteria TA'] = check_criteriumTA(prog, paths)
        elif criterium == Criteria.TD:
            results['Criteria TD'] = check_criteriumTD(prog, paths)
        elif criterium == Criteria.KTC:
            results['Criteria %s-TC' % arg] = check_criteriumKTC(prog, paths, arg)
        elif criterium == Criteria.ITB: #TODO
            results['Criteria %s-TB' % arg] = check_criteriumITB(prog, paths, arg)
        elif criterium == Criteria.TDEF:
            results['Criteria TDef'] = check_criteriumTDef(prog, paths)
        elif criterium == Criteria.TU:
            results['Criteria TU'] = check_criteriumTU(prog, paths)
        elif criterium == Criteria.TC:
            results['Criteria TC'] = check_criteriumTC(prog, paths)

    return results


def check_criteriumTA(prog, paths):
    """
    Check the criterium TA, i.e. every 'Assign edges' were passed through at least one time.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path

    :return covered percentage, not covered elements
    """
    graph, _, _, _ = prog
    assign_edges = gutils.get_assign_edges(graph)

    tested_edges = {edge for path in paths for (_, edge, _) in path}

    not_covered_assign_edges = assign_edges.difference(tested_edges)

    return "{:.0%}".format(1-len(not_covered_assign_edges)/len(assign_edges)), \
            not_covered_assign_edges


def check_criteriumTD(prog, paths):
    """
    Check the criterium TD, i.e. every 'If nodes' and 'While nodes' were
    evaluated true at least one time AND evaluted false at least one time.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path

    :return covered percentage, not covered elements
    """
    graph, _, _, _ = prog
    decision_edges = gutils.get_decision_edges(graph)

    tested_edges = {edge for path in paths for (_, edge, _) in path}

    not_covered_decisions_nodes_out_edges = decision_edges.difference(tested_edges)

    return "{:.0%}".format(1-len(not_covered_decisions_nodes_out_edges)/len(decision_edges)), \
            not_covered_decisions_nodes_out_edges


def check_criteriumKTC(prog, paths, k):
    """
    Check the criterium k-TC, i.e. every 'smaller than k paths' were
    executed at least one time.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path
    :param k : k

    :return covered percentage, not covered elements
    """
    graph, init_node, final_nodes, _ = prog
    smaller_than_k_paths = set()
    for final_node in final_nodes:
        smaller_than_k_paths |= gutils.get_smaller_than_k_paths(graph, init_node, final_node, k)
    
    tested_paths = {tuple((node for (node, _, _) in path)) for path in paths}

    not_covered_smaller_thank_k_paths = smaller_than_k_paths.difference(tested_paths)

    return "{:.0%}".format(1-len(not_covered_smaller_thank_k_paths)/len(smaller_than_k_paths)), \
            not_covered_smaller_thank_k_paths


def check_criteriumITB(prog, paths, i):
    """
    Check the criterium i-TB, i.e. every path in which the while loop are
    executed at MOST i time are in paths.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path
    :param i : i

    :return bool
    """
    graph, init_node, final_nodes, _ = prog
    i_loops_paths = set()
    for final_node in final_nodes:
        i_loops_paths |= gutils.get_i_loops_paths(graph, init_node, final_node, i)
    
    tested_paths = {tuple((node for (node, _, _) in path)) for path in paths}

    not_covered_i_loops_paths = i_loops_paths.difference(tested_paths)

    return "{:.0%}".format(1-len(not_covered_i_loops_paths)/len(i_loops_paths)), \
            not_covered_i_loops_paths

def check_criteriumTDef(prog, paths):
    """
    Check the criterium T-Def, i.e. every definitions are used at least one time

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path

    :return covered percentage, not covered elements
    """
    graph, _, _, _ = prog
    definitions = set()
    used_definitions = set()

    for def_node in graph.nodes:
        variables = gutils.def_function(graph, def_node)
        for variable in variables:
            definitions.add((variable, def_node))
            for path in paths:
                if gutils.path_used_def(graph, variable, def_node, path):
                    used_definitions.add((variable, def_node))
                    break
    not_used_definitions = definitions.difference(used_definitions)
    
    return "{:.0%}".format(1-len(not_used_definitions)/len(definitions)), \
            not_used_definitions


def check_criteriumTU(prog, paths):
    """
    Check the criterium TU, i.e. every utilisations reachable for each definitions
    are executed at least one time

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path

    :return bool
    """
    graph, _, _, _ = prog
    definitions = set()
    fully_used_definitions = set()

    for def_node in graph.nodes:
        variables = gutils.def_function(graph, def_node)
        for variable in variables:
            definitions.add((variable, def_node))

            # Create the reachable ref list
            reachable_ref_nodes = set()
            for ref_node in graph.nodes:
                if ref_node is def_node:
                    continue
                if variable not in gutils.ref_function(graph, ref_node):
                    continue
                if not nx.has_path(graph, def_node, ref_node):
                    continue
                k = max(len(path) for path in paths)
                for nodes_path in gutils.get_smaller_than_k_paths(graph, def_node, ref_node, k):
                    path = [(node, _, _) for node in nodes_path]
                    if gutils.path_used_def_ref(graph, variable, def_node, ref_node, path):
                        reachable_ref_nodes.add(ref_node)

            for ref_node in reachable_ref_nodes:
                for path in paths:
                    if gutils.path_used_def_ref(graph, variable, def_node, ref_node, path):
                        fully_used_definitions.add((variable, def_node))

    not_fully_used_definitions = definitions.difference(fully_used_definitions)
    
    return "{:.0%}".format(1-len(not_fully_used_definitions)/len(definitions)), \
            not_fully_used_definitions

def check_criteriumTC(prog, paths):
    """
    Check the criterium TC, i.e. every conditions (elementary boolean expression) 
    of every'If nodes' and 'While nodes' were
    evaluated true at least one time AND evaluted false at least one time.

    Notation:
    - path is a list of tuple (node, edge, variables_state_after_the_edge)

    :param prog
    :param paths : list of path

    :return covered percentage, not covered elements
    """
    graph, _, _, _ = prog
    decisions = set()
    for edge in graph.edges:
        node_type = graph.nodes[edge[0]]['node_type']
        if node_type in {NodeType.IF, NodeType.WHILE}:
            decision = graph.edges[edge]['decision']
            decisions.add((edge[0], decision))
    
    conditions = set()
    for src_node, decision in decisions:
        for condition in bexp.get_conditions(decision):
            conditions.add((src_node, str(condition), True))
            conditions.add((src_node, str(condition), False))

    tested_conditions = set()
    for path in paths:
        for _, edge, variables in path[:-1]:
            node_type = graph.nodes[edge[0]]['node_type']
            if node_type not in {NodeType.IF, NodeType.WHILE}:
                continue
            decision = graph.edges[edge]['decision']
            for var in variables: var.value = variables[var]
            for condition in bexp.get_conditions(decision):
                tested_conditions.add((edge[0], str(condition), condition()))

    not_covered_conditions = conditions.difference(tested_conditions)

    return "{:.0%}".format(1-len(not_covered_conditions)/len(conditions)), \
            not_covered_conditions