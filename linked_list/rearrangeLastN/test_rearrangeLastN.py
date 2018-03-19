import unittest
from rearrangeLastN import rearrangeLastN
from .. import linkedlist as ll


class MyTestCase(unittest.TestCase):
    def test_1(self):
        l = [1,2,3,4,5]
        linked_list = ll.list_to_linked_list(l)
        k = 3
        test = ll.linked_list_to_list(rearrangeLastN(linked_list, k))
        self.assertTrue(test == [3,4,5,1,2], msg=test)

    def test_2(self):
        l = [1,2,3,4,5,6,7]
        linked_list = ll.list_to_linked_list(l)
        k = 1
        test = ll.linked_list_to_list(rearrangeLastN(linked_list, k))
        self.assertTrue(test == [7,1,2,3,4,5,6], msg=test)

    def test_5(self):
        l = [123, 456, 789, 0]
        linked_list = ll.list_to_linked_list(l)
        k = 4
        test = ll.linked_list_to_list(rearrangeLastN(linked_list, k))
        self.assertTrue(test == [123, 456, 789, 0], msg=test)

    def test_10(self):
        l = [2,1]
        linked_list = ll.list_to_linked_list(l)
        k = 1
        test = ll.linked_list_to_list(rearrangeLastN(linked_list, k))
        self.assertTrue(test == [1,2], msg=test)


if __name__ == '__main__':
    unittest.main()
