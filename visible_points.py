import math
import time
import random
import bisect
start_time = time.time()
'''Given an array of points on a 2D plane, find the maximum number of points that are
visible from point (0, 0) with a viewing angle that is equal to 45 degrees.
'''

n= 1000
N = 100000
points = points = {(random.randint(-n,n), random.randint(-n, n)) for i in xrange(N)}

'''
# test 1
# should be 6
points = [[1,1],
 [3,1],
 [3,2],
 [3,3],
 [1,3],
 [2,5],
 [1,5],
 [-1,-1],
 [-1,-2],
 [-2,-3],
 [-4,-4]]

# test 2
# should be 1
points = [[5,4]]


# test 3
# should be 1
points = [[3,0],
 [-2,2]]


# test 4
# should be 2
points = [[-2,2],
 [-2,-2],
 [-5,0]]

# test 6
points = [[27,-88],
 [76,56],
 [-82,62],
 [-5,48],
 [-85,60],
 [-86,6],
 [-100,-54],
 [-22,30],
 [58,47],
 [12,80]]
'''


def toPolarCoord(vertex):
    fullcircle = math.pi *2
    x, y = vertex
    # get rid of negative values
    return (math.atan2(y, x) + fullcircle) % fullcircle


def find_lt(a,x):
    """
    find rightmost value less then x
    :param a: list to search
    :param x: value to find
    :return: index of rightmost value less then or equal to x
    """
    i = bisect.bisect_right(a, x)
    if i:
        return i-1
    raise ValueError


def visiblePoints(points):
    """
    find the points that are in a 45degree sweep starting from point (0,0)
    :param points: list of points[x,y] coords
    :return: count of number of points
    """
    maxcount = 0
    # special case 1 point
    if len(points) == 1:
        return 1
    # to polar coord(angle only)
    polarcoord = map(toPolarCoord, points)

    # store in array in order
    polarcoord.sort()

    # loop through each index and search for index value + pi/4 out
    for index, vert in enumerate(polarcoord):
        searchvalue = vert + math.pi/4
        maxindex = find_lt(polarcoord,searchvalue)
        count = maxindex - index + 1
        #print 'count %d' % count
        if count > maxcount:
            maxcount = count

    return maxcount
    '''
    # this works but not fast enough
    # add first point in list to end to get distance between first and last point
    polarcoord.append(polarcoord[0])

    ## print polarcoord
    #create new area that contains distance between each point, array should end with difference between end point and begining
    distarray = [((y - x) + math.pi *2) % (math.pi *2) for x, y in zip(polarcoord, polarcoord[1:])]

    #print distarray
    maxcount = 0
    angle = math.pi/4

    # keep count of max points
    # if not greater then 45 keep moving to next index and loop back to start of array

    #for index, dist in enumerate(distarray):
    for index in range(len(distarray)):
        sumdif = 0
        count = 1

        # print 'start@ %d' % dist
        for i in distarray[index:]:
            sumdif += i
            #print '+ %f = %f' % (math.degrees(i), math.degrees(sumdif))
            if sumdif <= angle:
                count += 1
                # print count
            else:
                break

        # if still under 45 start from start of the list again
        if sumdif < angle:
            # print 'start of list'
            for i in distarray[:index-1]:
                sumdif += i
                # print '+ %d = %d' % (i, sumdif)
                if sumdif < angle:
                    count += 1
                    # print count
                else:
                    break

        if count > maxcount:
            maxcount = count
    return maxcount
    '''

print 'maxcount %d' % visiblePoints(points)
print("--- %s seconds ---" % (time.time() - start_time))
