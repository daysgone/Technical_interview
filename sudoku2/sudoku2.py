'''
[[".", ".", ".", "1", "4", ".", ".", "2", "."],
[".", ".", "6", ".", ".", ".", ".", ".", "."],
[".", ".", ".", ".", ".", ".", ".", ".", "."],
[".", ".", "1", ".", ".", ".", ".", ".", "."],
[".", "6", "7", ".", ".", ".", ".", ".", "9"],
[".", ".", ".", ".", ".", ".", "8", "1", "."],
[".", "3", ".", ".", ".", ".", ".", ".", "6"],
[".", ".", ".", ".", ".", "7", ".", ".", "."],
[".", ".", ".", "5", ".", ".", ".", "7", "."]]
'''

def check_for_dup(row):
    tempset = set()
    for item in row:
        if item in tempset and item != 0:
            #print 'duplicate found %d' % item
            raise UserWarning('duplicate found %d' %item)
        elif item == 0:
            continue
        else:
            tempset.add(item)


def sudoku2(grid):
    #grid = np.array(grid)

    # change all . found in matrix to 0
    grid = [[0 if x == '.' else int(x) for x in y] for y in grid]
    #print grid
    # grid[grid == '.'] = 0
    # grid = grid.astype(int)  # make sure everything is an int

    try:
        for x in grid:
            check_for_dup(x)

        #columns = [[col[x] for col in grid] for x in xrange(9)]
        columns = zip(*grid)
        #columns = [grid[:x] for x in range(8)]
        #print columns

        for x in columns:
            #print x
            check_for_dup(x)

        # check sub arrays 3x3
        for rowstart in xrange(0,7,3):
            rowendvalues = [3,6,9]
            #t = iter(rowendvalues)
            rowend = rowstart + 3 #next(t)
            #print 'row start {}, end {}'.format(rowstart, rowend)

            #for y in xrange(0, 9, 3):
            for colstart in xrange(0,7,3):
                colendvalues = [3,6,9]
                #u = iter(colendvalues)
                colend = colstart + 3#next(u)
                #print colstart, colend
                #print 'column start {}, end {}'.format(colstart, colend)
                #print sum([row[colstart:colend] for row in l[rowstart:rowend]], [])
                block = sum([row[colstart:colend] for row in grid[rowstart:rowend]], [])
                #print block
                check_for_dup(block)
    except Exception as e:
        # print repr(e)
        return False
    return True


    #return False
    # columns are now rows
    #columns = np.rot90(grid)  # rotates CCW
    #print columns[8:9]

    # check columns
    #columns = [grid[:, x] for x in range(8)]

    # check 3x3 arrays
    #print grid[1::3, 1::3]
    '''
    blocks = []
    blocks.append(grid[0:3, 0:3].flatten())
    blocks.append(grid[0:3, 3:6].flatten())
    blocks.append(grid[0:3, 6:9].flatten())
    blocks.append(grid[3:6, 0:3].flatten())
    blocks.append(grid[3:6, 3:6].flatten())
    blocks.append(grid[3:6, 6:9].flatten())
    blocks.append(grid[6:9, 0:3].flatten())
    blocks.append(grid[3:6, 3:6].flatten())
    blocks.append(grid[3:6, 6:9].flatten())

    for i in blocks:
        print i[0]
    '''
    #return False

# code below is not mine its from AWice on codefights after I solved it myself
def sudoku2AWice(grid):
    def unique(G):
        G = [x for x in G if x != '.']
        return len(set(G)) == len(G)

    def groups(A):
        B = zip(*A)
        for v in xrange(9):
            yield A[v]
            yield B[v]
            yield [A[v / 3 * 3 + r][v % 3 * 3 + c]
                   for r in xrange(3) for c in xrange(3)]

    return all(unique(grp) for grp in groups(grid))