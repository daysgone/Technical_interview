import linkedlist as ll


def nextNode(l, k):  # would rather not loop through linked list to make this work...
    # returns the last valid node and if it made it to the correct depth
    node = l
    prev = None
    got_to_end = False

    temstr = 'find next nodes: '

    for i in range(k - 1):
        node = node.next
        if node is not None:
            temstr += str(node.value) + ','
        else:
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
        print 'check loop'
        node = node.next
        if node is None:
            return False

    return True


def rearrangeLastN(l, n):
    if n == 0:
        return l

    curnode = l
    head = ll.ListNode('head')
    prev = ll.ListNode('prev')

    return head.next


def rearrangeLastN(l, n):
    if n == 0:
        return l

    tail = l
    head = ll.ListNode('head')
    prev = ll.ListNode('prev')
    length = 1

    # find length of list
    while tail.next is not None:
        tail = tail.next
        length += 1

    #print 'length of list: {}'.format(length)

    # find the start of the section to move to front
    start_of_swap = l
    for node in xrange(length - n):
        prev = start_of_swap
        start_of_swap = start_of_swap.next
    else:
        prev.next = None
    if l == start_of_swap:
        #print 'not re-arranging'
        head.next = l
    else:
        #print 'rearrange range: {}:{}'.format(start_of_swap.value, tail.value)
        #print 'prev: {}'.format(prev.value)
        tail.next = l
        head.next = start_of_swap

    #print ll.linked_list_to_list(head.next)
    return head.next

'''
from codefights *seastargazer
def rearrangeLastN(head, n):

    if n == 0:
        return head
    
    slow_runner = head
    fast_runner = head
    
    for _ in xrange(n):
        fast_runner = fast_runner.next
        if fast_runner is None:
            return head

    while fast_runner.next is not None:
        fast_runner = fast_runner.next
        slow_runner = slow_runner.next
        
    new_head = slow_runner.next
    slow_runner.next = None
    fast_runner.next = head
    
    return new_head
'''

if __name__ == '__main__':
    l = [1,2,3,4,5]
    l = ll.list_to_linked_list(l)
    n = 3
    print ll.linked_list_to_list(rearrangeLastN(l,n))
