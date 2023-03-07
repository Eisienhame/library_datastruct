import unittest
from linked_list import Node, LinkedList

class MyTestCase(unittest.TestCase):
    def test_insert_begin(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.head.next_node, None)

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})

        self.assertEqual(ll.head.data, {'id': 2})

if __name__ == '__main__':
    unittest.main()