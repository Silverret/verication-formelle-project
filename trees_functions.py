from trees import T, X


def parse(tree):   
    node = 1
    test_list = []
    while node != '_':
        for e in tree.out_edges(node):
            attr = tree.get_edge_data(e[0], e[1])
            if attr['condition']() == False:
                pass
            else:
                attr['instruction'].execute()
                test_list.append(tuple((node, e, X.value)))
                node = e[1]
    test_list.append(tuple((node, None, X.value)))             
    return test_list          

a = parse(T)
print(a)