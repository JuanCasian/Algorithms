class Node:
    def __init__(self, label, neighbors_w_cost):
         self.label = label
         self.neighbors = neighbors_w_cost
         self.parent = None
         self.checked = False
         self.current_cost = float("inf")


def get_lowest_cost_node(hashT):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node_key in hashT.keys():
        cost = hashT[node_key].current_cost
        if (cost < lowest_cost and hashT[node_key].checked is False):
            lowest_cost = hashT[node_key].current_cost
            lowest_cost_node = hashT[node_key]
    return lowest_cost_node

def get_shortest_path(hashT, start, end):
    node = start
    node.current_cost = 0
    while node is not None:
        cost = node.current_cost
        neighbors = node.neighbors
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if (hashT[n].current_cost > new_cost):
                hashT[n].current_cost = new_cost
                hashT[n].parent = node
        node.checked = True
        node = get_lowest_cost_node(hashT)
    path = []
    while (end):
        path = [end.label] + path
        end = end.parent
    return path

        
        

def test():
    nodes_table = {}
    nodes_table['C'] = Node('C', dict())
    nodes_table['A'] = Node('A', dict())
    nodes_table['B'] = Node('B', dict())
    nodes_table['D'] = Node('D', dict())
    nodes_table['A'].neighbors = {
        "B": 6,
        "C": 2
    }
    nodes_table['B'].neighbors = {
        "D": 1,
    }
    nodes_table['C'].neighbors = {
        "B": 3,
        "D": 5
    }
    res = get_shortest_path(nodes_table, nodes_table['A'], nodes_table['D'])
    print(res)

test()