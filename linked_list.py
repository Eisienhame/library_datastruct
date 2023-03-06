

class Node:
    def __init__(self, data:dict, next_node = None):
        self.data = data  #  данные
        self.next_node = next_node  # ссылка на следующий

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = Node(head)
        self.tail = Node(tail)

    def insert_beginning(self, data):
        self.head.next_node = self.head
        self.head = Node(data)

    def insert_at_end(self, data):
        self.tail.next_node = Node(data)
        self.tail = Node(data)

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)


ll = LinkedList()
print(ll.head)
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()
