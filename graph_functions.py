def parse(prog, test):
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
