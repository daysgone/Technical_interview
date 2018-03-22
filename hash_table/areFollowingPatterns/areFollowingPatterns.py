"""
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words,
there should be no i and j for which strings[i] = strings[j] and patterns[i] != patterns[j] or for which strings[i] !=
 strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.
Input/Output

[execution time limit] 4 seconds (py)

[input] array.string strings

An array of strings, each containing only lowercase English letters.

Guaranteed constraints:
1 <= strings.length <= 105,
1 <= strings[i].length <= 10.

[input] array.string patterns

An array of pattern strings, each containing only lowercase English letters.

Guaranteed constraints:
patterns.length = strings.length,
1 <= patterns[i].length <= 10.

[output] boolean

Return true if strings follows patterns and false otherwise
"""

'''
def areFollowingPatterns(strings, patterns):
    dictionary = {}

    for index, key in enumerate(strings):
        if key in dictionary.keys():
            print 'key {} in dict already'.format(key)
            if dictionary[key] != patterns[index]:
                print '\tfound different value'
                return False
        elif patterns[index] in dictionary.values():
            print 'already value in dictionary'
            return False
        else:
            print 'key not in dict adding {}'.format(key)
            dictionary[key] = patterns[index]
    else:
        return True
'''


def areFollowingPatterns(strings, patterns): #k_lee codefights
    dictionary = {}
    for string, pattern in zip(strings, patterns):
        if string in dictionary and dictionary[string] != pattern:
            return False
        dictionary[string] = pattern
    return len(dictionary) == len(set(dictionary.values()))

