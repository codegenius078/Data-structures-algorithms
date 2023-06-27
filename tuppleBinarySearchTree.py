# tuple binary search tree using recursion

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


tuple_data = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def parse_tuple(data):
    print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
        
    return node


tree = parse_tuple(tuple_data)
print(tree.right.data)
