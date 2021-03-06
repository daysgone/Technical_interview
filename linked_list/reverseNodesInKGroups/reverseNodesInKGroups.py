import linkedlist as ll


def nextNode(l, k):  # would rather not loop through linked list to make this work...
    # returns the last valid node and if it made it to the correct depth
    node = l
    prev = None
    got_to_end = False

    temstr = 'find next nodes: '

    for i in range(k - 1):
        prev = node
        node = node.next
        if node is not None:
            temstr += str(node.value) + ','
        if node is None:
            got_to_end = False
            temstr += str(None)
            return l
        got_to_end = True
    print temstr
    return node  # , got_to_end)


def checkNextNode(l, k):
    if l is None:
        return False
    node = l
    for i in range(k - 1):
        node = node.next
        if node is None:
            return False

    return True


def reverseNodesInKGroups(l, k):
    if k == 1: #special case, nothign is flipped
        return l

    head = ll.ListNode('head')
    nextnode = ll.ListNode('next')
    curnode = l

    while checkNextNode(curnode, k):
        #print '\nsub-section start: {}'.format(curnode.value)  # these are the start of subsections
        prev = None
        tail = curnode  # keep track of end of next subsection

        for i in range(k):
            #print '\tstart loop {}:\t\t cur:\t {}, l:\t {}, next:\t {}'.format(i, curnode.value, l.value, nextnode.value)
            nextnode = curnode.next
            curnode.next = prev
            prev = curnode
            curnode = nextnode
            #print '\tend loop {}:\t\t\t cur:\t {}, l:\t {}, next:\t {}'.format(i, curnode.value, l.value, nextnode.value)

        if head.next is None:
            head.next = prev
        else:
            l.next = prev
            l = tail  #TODO what if k is greater then 2?

        print ll.linked_list_to_list(head.next)
    l.next = curnode
    #print ll.linked_list_to_list(head.next)
    return head.next


if __name__ == '__main__':
    l = [1,2,3]
    l = ll.list_to_linked_list(l)
    k = 2
    print reverseNodesInKGroups(l,k)