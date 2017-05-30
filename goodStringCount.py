import time
import math
start_time = time.time()


def goodStringsCount(len):
    """
    what are the total possible outcomes of "good string" of a length of len
    -   only lowercase English letters
    -   each char in string is unique
    -   eaxactly one character must be lexicographically greater then the char that precedes it
    -   special case: len of 1 will return 0
    
    :param len: integer value of how long strings can be
    :return:number of combinations of good strings
    """

    def nPr(n, k): # order is important and repetitions not allowed
        g = math.factorial
        return g(n)/g(n-k)

    def nCr(n, k):  # order does not matter
        f = math.factorial
        return f(n) / (f(k) * f(n - k))

    count = 0
    length = 26

    if len == 1:
        return 0
    '''
    if len <= 2:
        return nCr(length, len) * (len-1)
    else:
    '''
    allpossibwithrep = math.pow(length, len)  # with repetition
    #print 'all possible choices with repetition %d' % allpossibwithrep

    allpossibwithoutrep = nPr(length, len)
    #print 'all possible choices without rep %d' % allpossibwithoutrep

    allpossibnorepord = nCr(length, len)
    # print 'all possible choices without repetition order matters %d' % allpossibnorepord
    print (allpossibwithoutrep - (allpossibnorepord * (len-1)))  # works for 2 and 3
    print (allpossibwithoutrep - (allpossibnorepord * (len-2))) / 2.0  # works for 2,4
    print (allpossibwithoutrep - (allpossibnorepord * 2)) / 2.0  # works for 4
    #return int((((2.0/3.0)*math.pow(len, 3)) - (4 * math.pow(len, 2)) + ((31.0/3.0) * len) - 9) * allpossibnorepord)

    #anylexorder = nCr(length, len) * 2

    #print 'pick remaining letters with no repetition in lexicographical order %d' % anylexorder
    #return #allpossibnorep + anylexorder #  + (nPr(length, 2) * nCr(length-2, len -2))  #math.pow(length, len) - (nPr(length, 2) * nCr(length-2, len -2)) #* nCr(length, 2)  # - (nCr(length, len) * len-1)


print goodStringsCount(2)
print goodStringsCount(3)
print goodStringsCount(4)
print goodStringsCount(5)

print("--- %s seconds ---" % (time.time() - start_time))

