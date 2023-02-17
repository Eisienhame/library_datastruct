class Node:
    def __init__(self, data, next_node = None):
        self.data = data  #  данные
        self.next_node = next_node  # ссылка на следующий

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        'Добавить элемент'
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node