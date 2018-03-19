import unittest
import reverseNodesInKGroups as rn

from .. import linkedlist as ll


class MyTestCase(unittest.TestCase):
    '''
    def test_1(self):
        l = [1,2,3,4,5]
        k = 2
        linked_list = ll.list_to_linked_list(l)
        test = ll.linked_list_to_list(rn.reverseNodesInKGroups(linked_list, k))
        self.assertTrue(test == [2,1,4,3,5], msg=test)

    def test_2(self):
        l = [1, 2, 3, 4, 5]
        k = 1
        linked_list = ll.list_to_linked_list(l)
        test = ll.linked_list_to_list(rn.reverseNodesInKGroups(linked_list, k))
        self.assertTrue(test == [1, 2, 3, 4, 5], msg=test)
    '''
    def test_3(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        k = 3
        linked_list = ll.list_to_linked_list(l)
        test = ll.linked_list_to_list(rn.reverseNodesInKGroups(linked_list, k))
        self.assertTrue(test == [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11], msg=test)
    '''
    def test_empty_reverse_linked_list(self):
        l = []
        k = 1
        linked_list = ll.list_to_linked_list(l)
        test = ll.linked_list_to_list(rn.reverseNodesInKGroups(linked_list, k))
        self.assertTrue(test == [], msg=test)

    def test_custom2_linked_list(self):
        l = [1]
        k = 1
        linked_list = ll.list_to_linked_list(l)
        test = ll.linked_list_to_list(rn.reverseNodesInKGroups(linked_list, k))
        self.assertTrue(test == [1], msg=test)

    def test_custom3_linked_list(self):
        l = [1,2,3]
        k = 2
        linked_list = ll.list_to_linked_list(l)
        test = ll.linked_list_to_list(rn.reverseNodesInKGroups(linked_list, k))
        self.assertTrue(test == [2,1,3], msg=test)
    '''



if __name__ == '__main__':
    unittest.main()
