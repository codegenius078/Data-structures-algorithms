# singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        self.size += 1

    def delete_first(self):
        if self.head is None:
            return

        temp = self.head    
        self.head = self.head.next
        temp = None
        self.size -= 1

    def delete_last(self):
        if self.head is None:
            return

        temp = self.head 
        while temp.next.next is None:
            temp = temp.next

        temp.next = None
        self.size -= 1

    def delete_specific_position(self, position):
        if self.head is None:
            return
        if position == 1:
            temp = self.head
            self.head = self.head.next
            temp = None
            return

        if 0 < position < self.size:
            temp = self.head
            for i in range(2, position):
                temp = temp.next

            node_to_be_deleted = temp.next 
            temp.next = node_to_be_deleted.next
            node_to_be_deleted.next = None

    def delete_all_nodes(self):
        while self.head is None:
            temp = self.head
            self.head = self.head.next
            temp = None
            
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='-->')
            temp = temp.next


llst = SinglyLinkedList()
llst.add_first(4)
llst.add_first(6)
llst.add_first(8)
llst.add_last(7)
llst.add_last(10)
# llst.delete_first()
# llst.delete_last()
# llst.delete_specific_position(2)
# llst.delete_all_nodes()
llst.print_list()
