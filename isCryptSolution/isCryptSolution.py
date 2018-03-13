"""
Input/Output

[time limit] 4000ms (py)
[input] array.string crypt

An array of three non-empty strings containing only uppercase English letters.

Guaranteed constraints:
crypt.length = 3,
1 <= crypt[i].length <= 14.

[input] array.array.char solution

An array consisting of pairs of characters that represent the correspondence between letters and numbers in the 
cryptarithm. The first character in the pair is an uppercase English letter, and the second one is a digit in the range 
from 0 to 9.

Guaranteed constraints:
solution[i].length = 2,
'A' <= solution[i][0] <= 'Z',
'0' <= solution[i][1] <= '9',
solution[i][0] != solution[j][0], i != j,
solution[i][1] != solution[j][1], i != j.

It is guaranteed that solution only contains entries for the letters present in crypt and that different letters have 
different values.

[output] boolean

Return true if the solution represents the correct solution to the cryptarithm crypt, otherwise return false.
"""


def isCryptSolution(crypt, solution):
    answer = []
    # print crypt
    for word in crypt:
        # get first 2 words and convert to a number
        wordchar = [x for x in word]
        # print wordchar
        value = 0

        # make sure work is longer then a single letter
        # check first letter in word and make sure its value is not 0
        if len(wordchar) > 1:
            firstletter = wordchar[0]
            # print first letter
            for sol in solution:
                if sol[0] == firstletter:
                    if sol[1] == "0": # first
                        # print 'should end here'
                        return False

        for letter in wordchar:
            for sol in solution:
                if sol[0] == letter:
                    value *= 10  # shift digit over a decimal place larger
                    value += int(sol[1])

        # print value
        answer.append(value)

    # print answer

    if answer[0] + answer[1] == answer[2]:
        return True
    else:
        return False


def main():
    # <editor-fold desc="Description">
    crypt = ["SEND",
             "MORE",
             "MONEY"]
    solution = [["O", "0"],
                ["M", "1"],
                ["Y", "2"],
                ["E", "5"],
                ["N", "6"],
                ["D", "7"],
                ["R", "8"],
                ["S", "9"]]
    print isCryptSolution(crypt, solution)
    # </editor-fold>

if __name__ == '__main__':
    main()

