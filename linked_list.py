

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
            self.head = Node(data, None)
        else:
            x = self.head
            self.head = Node(data)
            self.head.next_node = x


    def insert_at_end(self, data):
        self.sum_of_items += 1

        if self.head is None:
            self.head = Node(data)
        else:
            x = self.head
            while x.next_node:
                x = x.next_node
            x.next_node = Node(data)

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
        print(self.sum_of_items)

    def to_list(self):
        'возвращает список с данными, содержащимися в односвязном списке LinkedList'
        need_list = []
        node = self.head
        while node:
            need_list.append(node.data)
            node = node.next_node
        return need_list
    def get_data_by_id(self, id):
        'возвращает первый найденный в LinkedList словарь с ключом id'
        x = self.to_list()
        catch_them_all = None
        try:
            for item in x:
                if item['id'] == id:
                    catch_them_all = item
            if catch_them_all != None:
                return catch_them_all
            else:
                raise TypeError
        except TypeError:
            print('Данные не являются словарем или в словаре нет id.')

ll = LinkedList()

ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
ll.insert_beginning({'id': 0, 'username': 'serebro'})
lst = ll.to_list()
print(lst)

user_data = ll.get_data_by_id(7)
print(user_data)

