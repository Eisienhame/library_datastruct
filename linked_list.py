

class Node:
    def __init__(self, data, next_node = None):
        self.data = data  #  данные
        self.next_node = next_node  # ссылка на следующий

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sum_of_items = 0
    def insert_beginning(self, data):
        self.sum_of_items += 1
        if self.head is None:
            self.head = Node(data)

        else:
            if self.sum_of_items == 2:
                x = self.head
                self.head = Node(data)
                self.head.next_node = x
            elif self.sum_of_items == 3:
                x = self.head
                self.head = Node(data)
                self.head.next_node = x
                self.head.next_node.next_node = x.next_node



    def insert_at_end(self, data):
        self.sum_of_items += 1

        if self.head is None:
            self.head = Node(data)
        else:
            if self.sum_of_items == 1:
                self.head.next_node = Node(data)
                self.tail = Node(data)
            # elif self.sum_of_items == 2:
            #     self.head.next_node.next_node = Node(data)
            #     self.tail = Node(data)
            # elif self.sum_of_items == 3:
            #     self.head.next_node.next_node.next_node = Node(data)
            #     self.tail = Node(data)
            # elif self.sum_of_items == 4:
            #     self.head.next_node.next_node.next_node.next_node = Node(data)
            #     self.tail = Node(data)
            # elif self.sum_of_items == 5:
            #     self.head.next_node.next_node.next_node.next_node.next_node = Node(data)
            #     self.tail = Node(data)
            #




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
        print(self.sum_of_items)

ll = LinkedList()
print(ll.head)
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()
