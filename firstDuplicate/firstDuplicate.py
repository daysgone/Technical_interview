def firstDuplicate(a):
    loc = len(a)

    for i, v in enumerate(a):
        # print i, v
        try:
            second = a[i + 1:].index(v)  # index is relative to first time found
            second += i + 1  # put back index into global space

        except ValueError:
            # print 'value error'
            second = -1
        except IndexError:
            # print 'index error'
            pass

        if second < loc and second != -1:
            # print second
            loc = second
    if loc == len(a):
        return -1
    else:

        return a[loc]


'''try with starting at index 1 and look backwards'''


def firstDuplicate1(a):
    loc = -1

    for i, v in enumerate(a, 1):
        #print i, v
        try:
            second = a[:i-1].index(v)  # ValueError if not found
            # print 'duplicate of %d found at %d and %d' % (v, second, i-1)
            loc = i-1
            break
        except ValueError:
            # print 'value error'
            pass
        except IndexError:
            # print 'index error'
            pass
    if loc >= 0:
        return a[loc]
    else:
        return loc

def firstDuplicate2(a):
    loc = -1
    dups = set()
    for i, v in enumerate(a):
        #print i, v
        try:
            if v in dups:
                loc = i
                break
            dups.add(v)
        except ValueError:
            # print 'value error'
            pass
        except IndexError:
            # print 'index error'
            pass
    if loc != -1:
        return a[loc]
    else:
        return loc

