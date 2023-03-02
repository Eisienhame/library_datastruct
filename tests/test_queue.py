import unittest
from custom_queue import Node, Queue


class MyTestCase(unittest.TestCase):
    def test_enqueue(self):
        s1 = Queue()
        s1.enqueue('data1')
        s1.enqueue('data2')


        self.assertEqual(s1.head.data, 'data1')
        self.assertEqual(s1.tail.data, 'data2')

    def test_dequeue(self):
        s1 = Queue()
        s1.enqueue('data1')
        s1.enqueue('data2')

        self.assertEqual(s1.dequeue(), 'data1')

if __name__ == '__main__':
    unittest.main()
