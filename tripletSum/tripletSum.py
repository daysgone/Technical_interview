"""Note: Write a solution with O(n2) time complexity, since this is what you would be asked to do during a real interview.

You have an array a composed of exactly n elements. Given a number x, determine whether or not a contains three elements for which the sum is exactly x.
"""
import bisect


def tripletSum(x,a):
    """
        Find out of there is at least one 3 number combination in a list that will sum up to the given number
        :param x: integer - number to sum up to
        :param a: integer[] - list of numbers to try and sum
        :return: boolean - true if there is at least one triplet of numbers that add up to the given number x
    """
    a.sort()

    # cut down list so items that are larger are not a factor
    index = bisect.bisect_left(a, x-1)
    newlist = a[:index]

    for index, value in enumerate(newlist):
        for jindex,jvalue in enumerate(newlist[index+1:]):
            searchfor = x - (value+jvalue)
            try:
                if newlist[index+ jindex+1:].index(searchfor):
                    return True
            except ValueError:
                # not found in list
                pass

    return False


