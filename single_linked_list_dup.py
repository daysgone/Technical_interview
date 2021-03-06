#!/usr/bin/python
"""
Remove duplicates in a singly linked list
"""

__author__ = "Brian Day"
__email__ = "xbriandayx@gmail.com"
_version__ = 0.1


class Node(object):
    """
    linked list node
    """

    def __init__(self, data=None, next_node=None, prev_node=None):
        self._data = data
        self._next_node = next_node
        self._prev_node = prev_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, value):
        self._prev_node = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        self._next_node = value

    '''
    def get_next(self):
        return self._next_node

    def set_next(self, new_next):
        self._next_node = new_next
    '''

    def __str__(self):
        return str(self._data)


class SinglyLinkedList(object):
    """
    every node contains some data and a link to the next element
    can be used to implement stack, queue or sorted list
    """
    def __init__(self, head=None):
        self._head = head
        self._tail = head

    @property
    def head(self):
        """
        start item in list
        :return: first item in list
        """
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node):
        self._tail = node

    def insert_start(self, data):
        """
        take data and initializes new node with given data and adds to list
        places new node at head of list
        :param data:
        :return: None
        """
        new_node = Node(data, self._head)  # add new node to front of list

        if self.head is None:  # first node added to list
            self.head = new_node
            self.tail = new_node

        self._head = new_node  # head of list now the new node

    def insert_after(self, data, prev_node=None):
        """
        take data and initialize new node with given data and adds to end of singly linked list
        tail must be updated
        :param data: data to be stored inside new node
        :param prev_node: Node object to place new node after if None then tail of list is assumed
        :return: None
        """
        new_node = Node(data)

        if prev_node is None:  # adding to tail of list
            prev_node = self.tail
            self.tail = new_node

        new_node.next_node = prev_node.next_node
        prev_node.next_node = new_node

    def size(self):
        """
        loops through nodes in list
        :return: size of list
        """
        current = self._head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    '''
    def search(self, data, delete=False):
        """
        look for node with data given
        :param data: data to look for
        :return: node object if found, else None
        """
        found = False
        current = self._head
        try:
            while current and found is False:
                if current.data == data:
                    found = True
                else:
                    current = current.next_node

            if current is None:
                raise ValueError("data not found in list")
        except ValueError as e:
            print e
            return None
        except AttributeError:
            print current
        return current

    def delete(self, data):
        """
        remove node with given data and reconnect nodes
        :param data:
        :return:
        """
        current = self._head
        previous = None
        found = False
        try:
            while current and found is False:
                if current.data == data:
                    found = True
                else:
                    previous = current
                    current = current.next_node  # get next item in list

            if current is None:
                raise ValueError("Data not in list, cannot delete")
            if previous is None:
                self._head = current.get_next()
            else:
                previous.next_node = current.next_node
        except ValueError as e:
            print e
    '''
    def search(self, data, pop=False):
        current = self._head
        previous = None
        found = False
        try:
            while current and found is False:
                if current.data == data:
                    found = True
                else:
                    previous = current
                    current = current.next_node  # get next item in list

            if current is None: # reached the end of the linked list
                raise ValueError("Data not in list")

            if pop:
                if previous is None:  # if item is first in list
                    self._head = current.next_node
                else:
                    previous.next_node = current.next_node

            return current
        except ValueError as e:
            print e

    def __str__(self):
        current = self._head
        prtstr = str(current.data)
        current = current.next_node
        concat = '->'
        while current is not None:
            prtstr += concat
            prtstr += str(current.data)
            current = current.next_node

        return prtstr


def del_dup_sl_list(list):
    hash_table = dict()
    hash_table[list.head.data] = True
    prev_node = list.head
    cur_node = list.head.next_node

    while cur_node is not None:
        # check and see if item already exists in dict
        if cur_node.data in hash_table.keys():
            # delete item from linked list
            prev_node.next_node = cur_node.next_node

        else:
            hash_table[cur_node.data] = True

        prev_node = cur_node
        cur_node = cur_node.next_node


if __name__ == "__main__":
    sl_list = SinglyLinkedList()

    sl_list.insert_start(1)
    sl_list.insert_start(2)
    sl_list.insert_start(Node('name'))

    sl_list.insert_after("tail")
    print sl_list
    test_node = sl_list.search(1, True)
    print sl_list
    print test_node
    '''
    sl_list.insert_after('forth', test_node)
    print 'prior to de-dup %s' % sl_list

    del_dup_sl_list(sl_list)
    #newitem =sl_list.search('one')
    #print newitem
    #print 'size of linked list %d' % sl_list.size()
    #print sl_list.tail
    print 'post de-dup %s' % sl_list
    '''
