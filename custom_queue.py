class Node:
    def __init__(self, data, next_node = None):
        self.data = data  #  данные
        self.next_node = next_node  # ссылка на следующий

class Queue:
    def __init__(self):
        self.head = None  #начала очереди
        self.tail = None    #конец очереди
        self.sum_of_items = 0 #kol-vo itemov

    def enqueue(self, data):
        'Добавить элемент'
        new_node = Node(data)
        if self.head == None:
            'Если Очередь пустая'
            self.head = new_node
            self.head.next_node = None


        elif (self.head != None) and (self.head.next_node == None):
            "Если в очереди только 1 элемент"
            self.head.next_node = new_node
            self.tail = new_node

        elif (self.head != None) and (self.head.next_node != None):
            "Если в очереди больше 2 элементов"
            self.tail = new_node

        self.sum_of_items += 1

queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')


print(queue.head.data)
print(queue.head.next_node.data)
print(queue.tail.data)
print(queue.tail.next_node)
print(queue.tail.next_node.data)

