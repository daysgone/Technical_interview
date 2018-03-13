# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(l, k):
    """
    remove all values in linked list that contain value of k
    :param l: singly linked list of ints
    :param k: int to check list in which to remove
    :return: singly linked list with all values removed equal to k
    """
    if l is None:  # empty linked list
        print 'empty linked list'
        return l

    if l.value == k:  # if first node matches value start with next
        print 'first value matches'
        l = l.next

    head = l
    prev = l

    # while l is not last in list
    while head is not None:
        if head.value == k:
            print "value found"
            prev.next = head.next
            head = head.next
        else:
            print head.value

        prev = head
        head = head.next

    print head
    return l


def main():
    l = [3, 1, 2, 3, 4, 5]
    k = 3
    sll = ListNode(None)
    for i in l:
        print i
        sll.next = ListNode(i)

    print removeKFromList(sll, k)

if __name__ == '__main__':
    main()
