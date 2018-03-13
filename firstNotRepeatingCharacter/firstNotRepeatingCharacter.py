"""
Write a solution that only iterates over the string once and uses O(1) additional memory, 
since this is what you would be asked to do during a real interview.
Input/Output

[time limit] 4000ms (py)
[input] string s

A string that contains only lowercase English letters.

Guaranteed constraints:
1 <= s.length <= 10^5.

[output] char

The first non-repeating character in s, or '_' if there are no characters that do not repeat.
"""

def firstNotRepeatingCharacter(s):
    dic = {}
    val = '_'
    try:
        for i, c in enumerate(s):
            if c in dic:  # check and see if key already exists in dict
                dic[c] = -1
            else:  # store index of first time char seen
                dic[c] = i
    except KeyError as e:
        print e
    try:
        dic = {k: v for k, v in dic.items() if v >= 0}
        val = min(dic, key=dic.get)
    except ValueError as e:
        print e
    return val


matrix = [[1,2,3], [4,5,6],[7,8,9]]

print matrix[1][~1]