from utils import Node, Stack


stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

print(stack.top.data)
print(data)