import time
start_time = time.time()
'''
Given a binary tree and a number k, your task is to find the sum of tree nodes at level k. The binary tree is represented by a string tree with the format: (<node-value>(<left subtree>)(<right subtree>)).

Example

For tree = "(0(5(6()())(14()(9()())))(7(1()())(23()())))" and k = 2, the output should be

treeLevelSum(tree, k) = 44.

Explanation: The nodes at level 2 are 6, 14, 1, and 23, so the answer is 6 + 14 + 1 + 23 = 44.

Input/Output

[time limit] 4000ms (py)
[input] string tree

A valid string representing a tree.

Constraints:

2 <= tree.length <= 105.

All the values in a given tree are guaranteed to be integers.

[input] integer k

Constraints:

0 <= k <= 105.

[output] integer

The total sum of all the values at level k in a tree.
'''
tree = u"(0(5(6()((0(5(6()())(4()(9()())))(7(1()())(3()())))))(14()(9()())))(7(1()())(23()())))"
k = 5
# test 1 should be 3
#tree = u"(3()())"
#k = 0
''' test 2 should be 4
tree = u"(3(3()())(1()()))"
k =1
'''
'''                       0
                     /         \
                    5           7
                  /   \        /  \
                 6    14      1    23
                / \   / \    / \   / \
               () () ()  9  () () () ()
                        / \
                       () ()
'''

def prettyprint(msg, level):
    if msg is None:
        msg == 'None'

    string = '\t' * level
    return string + str(msg)


def treeLevelSum(treestring, k):
    """
    parse string representation of tree and return the sum of the tree nodes and level k
    string representation of tree is pre-order (root,left subtree,right subtree)
    :param tree: string representation of tree with format (<node-value>(<left subtree>)(<right subtree>))
    :param k: int level to get sum of
    :return: int value of sum of k level of tree
    """
    sum = 0

    if treestring[0] != '(':
        print 'invalid string'

    else:  # start of tree found
        #print 'level 0'
        data = None
        level = 0
        # root, left subtree, right subtree
        for char in treestring[1:]:  # start at second character
            if char.isdigit():
                if level == k:
                    if data is None:
                        data = 0
                    data *= 10
                    data += int(char)

            elif char == '(':
                # finish previous node
                if level == k and data is not None:
                    sum += data

                data = None
                #print prettyprint(data, level)

                level += 1

            elif char == ')':
                #print prettyprint('node finished:', level)
                level -= 1

    return sum

print treeLevelSum(tree, k)
print("--- %s seconds ---" % (time.time() - start_time))
