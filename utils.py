class Node:
    def __init__(self, data, next_node = None):
        self.data = data  #  данные
        self.next_node = next_node  # ссылка на следующий

class Stack:

    def __init__(self):
        self.top = None
        self.sum_of_items = 0


    def push(self, data):
        'Добавить элемент'
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node
        self.sum_of_items += 1
    def pop(self):
        'Удалить элемент'
        self.sum_of_items -= 1
        del_data = self.top.data
        self.top = self.top.next_node

        return del_data

