import unittest
from utils import Node, Stack

class TestStack(unittest.TestCase):
    def test_push(self):
        s1 = Stack()
        s1.push('data1')

        self.assertEqual(s1.top.data, 'data1')

    def test_pop(self):
        s1 = Stack()
        s1.push('data1')
        s1.push('data2')
        s1.pop()
        self.assertEqual(s1.top.data, 'data1')
        self.assertEqual(s1.sum_of_items, 1)



if __name__ == '__main__':
    unittest.main()
