# doubly linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None    
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def delete_first(self):
        if self.head is None:
            return

        temp = self.head
        self.head = self.head.next
        temp = None

    def delete_last(self):
        if self.head is None:
            return
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="-->")
            temp = temp.next


dllst = DoublyLinkedList()
dllst.add_first(7)
dllst.add_first(5)
dllst.add_first(4)
dllst.add_last(3)
dllst.delete_last()
dllst.delete_first()
dllst.print_list()