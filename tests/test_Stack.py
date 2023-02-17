import unittest
from utils import Node, Stack

class TestStack(unittest.TestCase):
    def test_push(self):
        s1 = Stack()
        s1.push('data1')

        self.assertEqual(s1.top.data, 'data1')


if __name__ == '__main__':
    unittest.main()
