def firstDuplicate(A):
    '''AWise codefights'''
    ''' to flag that you have already seen a number
     use the index as the value that you have seen
     do this by turning the value in that index to a negative number
     if the number is turned back posative then you ahve already seen this number'''

    for i, x in enumerate(A):
        # take the value of the current iteration and change the number that is in the index to a negative
        A[abs(x) - 1] *= -1
        if A[abs(x) - 1] > 0:  # if the number was previously negative now positive then that means number was found again
            return abs(x)  # return value of current iterator since it is a duplicate
    return -1

a= [2,25,4,5,25]

print firstDuplicate(a)
