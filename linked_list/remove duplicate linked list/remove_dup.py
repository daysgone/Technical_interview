
def removeKFromList(l, k):
    """
    remove all values in linked list that contain value of k
    :param l: singly linked list of ints
    :param k: int to check list in which to remove
    :return: singly linked list with all values removed equal to k
    """
    i = 0
    while l:
        ++i
        l = l.next
        print i
    return l


'''
if __name__ == '__main__':
    l = []
    node = list_to_linked_list(l)
    start_node = node

    node_list = ""
    while node:
        node_list += "{}->".format(node.value)
        node = node.next
    node_list += "None"
    print node_list

    print linked_list_to_list(start_node)
'''