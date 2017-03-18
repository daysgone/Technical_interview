def dist(word1, word2):
    # returns # of different characters in 2 words
    return sum(x != y for x, y in zip(word1, word2))

#print dist('a', 'hot')


def wordLadder(beginWord, endWord, wordList):
    def dist(word1, word2):
        return sum(x != y for x, y in zip(word1, word2))

    ans = 1
    #active = {beginWord}
    active = [beginWord]
    '''
    Python's list constructs are slightly faster. However, if you'll be storing(unique)
    values in order to check for their existence, then sets are significantly faster.
    '''
    #wordset = set(wordList)
    while active:
        if endWord in active:  # same word
            return ans
        #wordset -= active  # remove if exists in list
        for word in active:
            test = False
            if word in wordList:
                test = True
                wordList.remove(word)
        #active = {y for x in active for y in wordset if dist(x, y) == 1}

        for y in wordList:
            for x in active:
                if dist(y, x) == 1:
                    #print 'True'
                    active.append(y)
        ans += 1
    return 0

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

print wordLadder(beginWord,endWord,wordList)

'''
active = 'miss'
wordlist = ['kiss','list']
wordset= set(wordlist)

print wordset

wordset -= {'lust'}

print wordset

print {y for x in active for y in wordset if True}
'''