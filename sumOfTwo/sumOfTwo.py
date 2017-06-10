'''You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of 
numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. 
Return true if such a pair exists, otherwise return false.

Example

For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
'''
import bisect


def sumOfTwo(a, b, v):
    """
    sum up one value from each list and add it to one from the other
    :param a: list of integers
    :param b: list of integers
    :param v: number to sum up to
    :return: boolean
    """
    # remove values from both lists that are larger then the value to sum up to
    a.sort()
    index = bisect.bisect_left(a, v-1)
    a = a[:index]

    b.sort()
    index = bisect.bisect_left(b, v-1)
    b = b[:index]

    for i in a:
        for j in b:
            if i+j == v:
                return True
    return False
'''
def sumOfTwo(a, b, v):
    # this is simplest way to do this without optimizing
    for i in a:
        for j in b:
            if i+j == v:
                return True
    return False
'''