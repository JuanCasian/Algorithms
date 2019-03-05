from collections import deque

class Node:
    def __init__(self, value, neighbors):
         self.val = value
         self.neighbors = neighbors
         self.parent = None
         self.checked = False

    def print_neighbors(self):
        for node in self.neighbors:
            print('Node Value: {}, node object: {}'.format(node.val, node))



def bread_first_search(start_node, val):
    search_queue = deque()
    search_queue.append(start_node)
    while (search_queue):
        current_node = search_queue.popleft()
        if (current_node.val == val):
            return current_node
        elif (current_node.checked == False):
            for node in current_node.neighbors:
                if (node.parent == None):
                    node.parent = current_node
                search_queue.append(node)
        current_node.checked = True
    return False

def test():
    sec_33 = Node(33, [Node(45, []), Node(18, [])])
    sec_27 = Node(27, [Node(25, []), Node(16, [])])
    sec_10 = Node(10, [Node(14, []), sec_27])
    start = Node(15, [sec_33, sec_27, sec_10])
    ans = bread_first_search(start, 16)
    if (ans):
        path = []
        tmp = ans
        while (tmp):
            path = [tmp.val] + path
            tmp = tmp.parent
        print('Node with value {} found. Path = {}'.format(ans.val, path))


test()