from trees import PROG, TESTS

def parse(prog, test):
    for variable in test:
        variable.value = test[variable]
    graph, node, final_nodes = prog
    path = []
    while node not in final_nodes:
        for e in graph.out_edges(node):
            attr = graph.get_edge_data(e[0], e[1])
            if attr['condition']() == False:
                pass
            else:
                attr['instruction'].execute()
                path.append((node, e, {variable.name : variable.value for variable in test}))
                node = e[1]
    path.append((node, None, {variable.name : variable.value for variable in test}))
    return path

p = parse(PROG, TESTS[1])

print(p)
import pdb; pdb.set_trace()
