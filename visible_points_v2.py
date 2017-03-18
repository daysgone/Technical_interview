"""
k_lee codefights example
"""
import math
import random
import time
start_time = time.time()

eps = 1e-12
n= 1000
N = 100000
points = points = {(random.randint(-n,n), random.randint(-n, n)) for i in xrange(N)}


def visiblePoints(points):
    angles = []
    for x, y in points:
        t = math.atan2(y, x)
        angles.append(t)
        # duplicate all angles in the range -180 to -135 to the high end 180 to 225 to help with overlap
        if t < -math.pi * 3 / 4 + eps:
            angles.append(t + 2*math.pi)
    angles.sort()

    ans = 0
    i = j = 0
    while i < len(angles):
        while j < len(angles) and angles[j] - angles[i] < math.pi / 4 + eps:
            j += 1
        ans = max(ans, j - i)
        i += 1
    return ans

print 'maxcount %d' % visiblePoints(points)
print("--- %s seconds ---" % (time.time() - start_time))
