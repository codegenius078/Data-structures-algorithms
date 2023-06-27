# array representation of a binary tree ( a heap )

tree = [None] * 10


def root(key):
    if tree[0] is not None:
        print("Tree already has a root")
    else:
        tree[0] = key


def set_left(key, parent):
    if tree[parent] is None:
        print("Cant set child to a null parent")
    else:
        tree[(parent * 2) + 1] = key


def set_right(key, parent):
    if tree[parent] is None:
        print("cant set child to a null parent")
    else:
        tree[(parent * 2) + 2] = key


def print_tree():
    for i in range(10):
        if tree[i] is not None:
            print(tree[i], end=" ")
        else:
            print("-", end=" ")
    print()


root('A')
set_left('B', 0)
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()