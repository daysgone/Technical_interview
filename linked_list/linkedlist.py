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