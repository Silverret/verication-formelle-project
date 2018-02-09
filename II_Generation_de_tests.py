from itertools import product

import networkx as nx
import constraint as csp

import III_Graph_utils as gutils
import IV_Classes.boolean_expression as bexp
import IV_Classes.arithmetic_expression as aexp
from IV_Classes.criteria import Criteria

NODE = 0
EDGE = 1
SUBPATH = 2

def generate_tests(prog, criterium, arg=None):
    """
    Realises the symbolic execution of the :param prog 
    to try to generate a set of tests which covered the criterium
    """
    tests = set()
    graph, _, _, _ = prog
    elements, elem_type = get_elements_to_cover(graph, criterium, arg)
    
    for elem in elements:
        paths = get_paths(prog, elem, elem_type)
        for path in paths:
            # Try to find a tests which enable to parse this path
            test = find_test(prog, path)
            if not test is None:
                tests.add(test)
                break

    return tests           


def get_elements_to_cover(graph, criterium, arg):    
    """
    Generate the elements (subpaths, nodes)
    the criterium must covered to be validated

    :param graph
    :param criterium
    :param arg

    :return elements (set of tuple), elem_type in {NODE, EDGE, SUBPATH}
    """
    elements = set()
    if criterium == Criteria.TA:
        elements = gutils.get_assign_edges(graph)
        elem_type = EDGE

    return elements, elem_type


def get_paths(prog, element, elem_type):
    """
    return every paths wich contains the elements (edge, node or subpath)

    :param prog
    :param element : tuple
    :param elem_type in {NODE, EDGE}

    :return paths (set of tuple of nodes)
    """
    graph, initial_node, final_nodes, _ = prog
    k = 2*nx.number_of_nodes(graph)

    all_paths = set()
    for final_node in final_nodes:
        all_paths |= gutils.get_smaller_than_k_paths(graph, initial_node, final_node, k)
    
    paths = set()
    if elem_type == EDGE:
        for path in all_paths:
            if sublist(list(element), path):
                paths.add(path)
    
    return paths

def sublist(ls1, ls2):
    def get_all_in(one, another):
        for element in one:
            if element in another:
                yield element

    for x1, x2 in zip(get_all_in(ls1, ls2), get_all_in(ls2, ls1)):
        if x1 != x2:
            return False
    return True

def find_test(prog, path):
    path_edges = {(path[i], path[i+1]) for i in range(len(path)-1)}

    graph, _, _, variables = prog

    variables = {variable: variable for variable in variables}
    problem = csp.Problem()

    domain = range(-10,11)
    for variable in variables:
        problem.addVariable(variable.name, domain)
    
    assign_list = []
    for path_edge in path_edges:
        decision = graph.edges[path_edge]['decision']
        # Find the set of n-uplets which satisfy the decision
        

        


    



