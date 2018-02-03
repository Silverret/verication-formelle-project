import instructions as inst
import arithmetic_expression as aexp

def parse(prog, test):
    """
    Parses a prog for a test

    :param prog: graph, node, final_nodes
    :param test: dictionary of variables and value
    """
    for variable in test:
        variable.value = test[variable]
    graph, node, final_nodes = prog
    path = []
    while node not in final_nodes:
        for e in graph.out_edges(node):
            attr = graph.get_edge_data(e[0], e[1])
            if not attr['condition']():
                pass
            else:
                attr['instruction'].execute()
                path.append((node, e, {variable.name : variable.value for variable in test}))
                node = e[1]
    path.append((node, None, {variable.name : variable.value for variable in test}))
    return path


def listSmallerThanKPathsUtil(graph, u, d, path, paths, k):
    """
    A recursive function to print all smaller than k paths from 'u' to 'd'.

    :param graph
    :param u: origin vertice
    :param d: destination vertice
    :param path[] stores actual vertices.
    :param paths[] is the list of found paths.
    :param k

    Source: https://www.geeksforgeeks.org/find-paths-given-source-destination/
    Strongly changed
    """

    # Mark the current node as visited and store in path
    path.append(u)

    # If current vertex is same as destination, then print
    # current path[]
    if len(path) > k:
        pass
    elif u == d:
        paths.append(path.copy())
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for ubis, i in graph.out_edges(u):
            listSmallerThanKPathsUtil(graph, i, d, path, paths, k)

    # Remove current vertex from path[] and mark it as unvisited
    path.pop()

def listSmallerThanKPaths(graph, s, d, k):
    """
    Lists all smaller than k paths from 's' to 'd'
    Loop included.

    Source: https://www.geeksforgeeks.org/find-paths-given-source-destination/
    Strongly changed
    """
    # Create an array to store paths
    path = []
    paths = []

    # Call the recursive helper function to list all paths
    listSmallerThanKPathsUtil(graph, s, d, path, paths, k)

    return paths

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
                variables = instruction.x
                def_var += variables
    return def_var


def ref_function(graph, node):
    """
    Returns a list of variables that are:
    - In a boolean expression in the condition of an exiting edge
    - In the right term of an a assign expression (other_vars = exp(var)) in the instruction of an exiting edge
    
    :param graph
    :param node: any node of the graph
    """
    ref_var = []
    for edge, edge_attr in graph.edges.items():
        if node == edge[0]: 
            condition = edge_attr['condition']
            instruction = edge_attr['instruction']
            variables = check_variables(condition)
            ref_var += variables
            if isinstance(instruction, inst.Assign):
                # y is the right term of our "Assign" method
                variables = check_variables(instruction.y)
                ref_var += variables
    return ref_var

def check_variables(expressions):
    """
    recursive function to check the variables used in expressions

    :param value: 
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