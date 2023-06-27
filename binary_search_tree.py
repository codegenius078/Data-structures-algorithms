# a binary search tree data structure

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if self.data is None:
            self.data = value
        else:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

    def height_of_tree(self, node):
        if node is None:
            return 0

        left_height = self.height_of_tree(node.left)
        right_height = self.height_of_tree(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def tree_size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.tree_size(node.left) + self.tree_size(node.right)

    def check_balanced_binary_tree(self, node):
        if node is None:
            return True
        left_height = self.height_of_tree(node.left)
        right_height = self.height_of_tree(node.right)

        if abs(left_height - right_height) > 1:
            return False

        left_check = self.check_balanced_binary_tree(node.left)
        right_check = self.check_balanced_binary_tree(node.right)

        if left_check is True and right_check is True:
            return True

    def balance_binary_search_tree(self, nodes):
        if not nodes:
            return None
        mid = len(nodes) // 2
        node = Node(nodes[mid])
        node.left = self.balance_binary_search_tree(nodes[:mid])
        node.right = self.balance_binary_search_tree(nodes[mid+1:])
        return node

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()


root = Node(15)
#root.insert(10)
root.insert(25)
root.insert(6)
root.insert(7)
root.insert(14)
root.insert(13)
#root.insert(60)
print(root.inorder_traversal())
print(root.height_of_tree(root))
print(root.tree_size(root))
print(root.check_balanced_binary_tree(root))
