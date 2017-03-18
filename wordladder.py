"""

Given two words, beginWord and endWord, and a wordList of approved words, find the length of the shortest transformation sequence from beginWord to endWord such that:

Only one letter can be changed at a time
Each transformed word must exist in the wordList.
Return the length of the shortest transformation sequence, or 0 if no such transformation sequence exists.

Note: beginWord does not count as a transformed word. You can assume that beginWord and endWord are not empty and are not the same.

Example

For beginWord = "hit", endWord = "cog", and wordList = ["hot", "dot", "dog", "lot", "log", "cog"], the output should be
wordLadder(beginWord, endWord, wordList) = 5.

The shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with a length of 5.

Input/Output

[time limit] 4000ms (py)
[input] string beginWord

Constraints:
1 <= beginWord.length <= 5.

[input] string endWord

Constraints:
endWord.length = beginWord.length.

[input] array.string wordList

An array containing all of the approved words. All words in the array are the same length and contain only lowercase English letters. You can assume that there are no duplicates in wordList.

Constraints:
2 <= wordList.length <= 600,
wordList[i].length = beginWord.length.

[output] integer

An integer representing the length of the shortest transformation sequence from beginWord to endWord using only words from wordList as described above.
"""

import time
start_time = time.time()


def reduce_word_list(list):
    """
    take given list of strings and break it up into a list of unique characters per index
    :param list: list of string
    :return: list of sets containing letters per index
    """
    reduced_list =[]
    # get number of letters in word
    word_len = len(list[0])
    for i in range(word_len):
        reduced_list.append(set())
    for word in list:
        for index, value in enumerate(word):
            reduced_list[index].add(value)

    return reduced_list


def wordLadder(beginWord, endWord, wordList):
    loopwordList = reduce_word_list(wordList)
    if endWord not in wordList:
        return 0

    if beginWord == endWord:
        return 0

    count = 1
    pass_list = [beginWord]
    temp_list = []
    end = False

    #print 'Start with %s' % beginWord
    while not end:
        #print 'pass list %s' % pass_list
        #print 'transform %d' % count

        # no valid paths exist
        if len(pass_list) == 0:
            #print 'empty list'
            return 0
        del temp_list[:]  # make sure temp_list is cleared

        for word in pass_list:
            # loop though each letter of word
            #print 'pass_list word: %s' %word

            for i, value in enumerate(word):
                # get ith character from every word in the valid word list and apply it to current word
                ## print '%d char' % i

                for l, set in enumerate(loopwordList):
                    # print set

                    for letter in set:
                        tempword = list(word)  # string to list to allow changes to be made to character values
                        ## print 'start %s' %tempword

                        tempword[l] = letter
                        tempword = "".join(tempword)
                        # print 'change %s' % tempword
                        # check to see if newly created word is in the wordList

                        if tempword in wordList: # and tempword not in pass_list and tempword not in temp_list:
                            if tempword == endWord:
                                ## print 'endWOrd found %s' % tempword
                                end = True
                            temp_list.append(tempword)
                            #print tempword
                            wordList.remove(tempword)
                            ## print 'templist %s' % temp_list
            '''
            if len(temp_list) == 0:
                print 'temp list empty'
                return count
            '''


        pass_list = list(temp_list)

        #if not end:
        count += 1

    return count

if __name__ == "__main__":
    '''
    beginWord = "hit"
    endWord = "hot"
    wordList = ["hot"]

    # test1
    # should be 5 passes
    beginWord = "hit"
    endWord = "cog"
    wordList =["hot","dot","dog","lot","log", "cog"]

    # test 2 s
    # should be 0
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot", "dog", "lot", "log"]


    #test 3
    beginWord = "a"
    endWord = "c"
    wordList = ["a",
               "b",
               "c"]

    # test5
    # should be 3
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot","dog","cog","pot","dot"]

    # test 4
    # should be 0
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]
    '''
    # test 10
    # should be 5
    beginWord = "kiss"
    endWord = "tusk"
    wordList = ["miss",
               "dusk",
               "kiss",
               "musk",
               "tusk",
               "diss",
               "disk",
               "sang",
               "ties",
               "muss"]
    '''
    #large test
    beginWord = "aaaaaaaaaa"
    endWord = "bbbbbbbbbb"
    wordList = [
                "aaaaaaaaab",
                "aaaaaaaabb",
                "aaaaaaabbb",
                "aaaaaabbbb",
                "aaaaabbbbb",
                "aaaabbbbbb",
                "aaabbbbbbb",
                "aabbbbbbbb",
                "abbbbbbbbb",
                "bbbbbbbbbb",
                "cccccccccc",
                "dddddddddd",
                "eeeeeeeeee",
                "ffffffffff",
                "gggggggggg",
                "hhhhhhhhhh"]
    '''

    print wordLadder(beginWord, endWord, wordList)

    print("--- %s seconds ---" % (time.time() - start_time))
