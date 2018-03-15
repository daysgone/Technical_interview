import unittest
from remove_dup import removeKFromList
from .. import linkedlist as ll
'''
# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x=None):
        self.value = x
        self.next = None


def list_to_linked_list(l):
    if l:
        start_node = ListNode()
        current_node = start_node

        current_node.value = l[0]

        for item in l[1:]:
            new_node = ListNode(item)
            current_node.next = new_node
            current_node = current_node.next

        return start_node
    return None

def linked_list_to_list(l):
    node_list = []
    while l:
        node_list.append(l.value)
        l = l.next
    return node_list
'''


class MyTestCase(unittest.TestCase):
    def test_empty_linked_list(self):
        l = []
        linked_list = ll.list_to_linked_list(l)
        k = 0
        test = ll.linked_list_to_list(removeKFromList(linked_list, k))
        self.assertTrue(test == [], msg=test)

    def test_single_node_removal(self):
        l = [1]
        linked_list = ll.list_to_linked_list(l)
        k = 1
        test = ll.linked_list_to_list(removeKFromList(linked_list, k))
        self.assertTrue(test == [], msg=test)

    def test_multiple_node_removal(self):
        l = [1, 1, 1]
        linked_list = ll.list_to_linked_list(l)
        k = 1
        test = ll.linked_list_to_list(removeKFromList(linked_list, k))
        self.assertTrue(test == [], msg=test)
    '''
    def test_leading_node_removal(self):
        l = [1,1,1,2]
        k = 1
        self.assertTrue(removeKFromList(l,k) == [2])

    def test_trailing_node_removal(self):
        l = [2,1,1,1]
        k = 1
        self.assertTrue(removeKFromList(l,k) == [2])

    '''


if __name__ == '__main__':
    unittest.main()
