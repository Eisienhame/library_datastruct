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

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 2})
        ll.insert_at_end({'id': 3})
        a = ll.to_list()
        self.assertEqual(a, [{'id': 2}, {'id': 3}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 2})
        a = ll.get_data_by_id(2)
        self.assertEqual(a, {'id': 2})
        b = ll.get_data_by_id(7)
        self.assertEqual(b, print('Данные не являются словарем или в словаре нет id.'))

if __name__ == '__main__':
    unittest.main()