# circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
            
        temp.next = new_node
        new_node.next = self.head
        self.head = new_node
    
    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
            
        temp.next = new_node
        new_node.next = self.head

    def remove(self, data):
        if self.head is None:
            return
        temp = self.head
        while temp.next is not self.head:
            if temp.data == data and temp.next is not None:
                self.head = self.head.next
                temp = None
                break

            if temp.next.data == data:
                temp2 = temp.next
                temp.next = temp.next.next
                temp2 = None
            temp = temp.next

        temp = None
        
    def print_list(self):
        temp = self.head
        while temp.next is not self.head:
            print(temp.data, end='-->')
            temp = temp.next
        print(temp.data)
            
            
cllist = CircularSinglyLinkedList()
cllist.add_first(4)
cllist.add_first(5)
cllist.add_first(7)
cllist.add_last(8)
cllist.remove(5)
cllist.print_list()
        