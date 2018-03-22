import unittest
from areFollowingPatterns import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        strings = ["cat","dog","dog"]
        patterns = ["a","b","b"]

        test = areFollowingPatterns(strings, patterns)
        sol = True
        self.assertTrue(test == sol, msg=test)

    def test_2(self):
        strings = ["cat","dog","doggy"]
        patterns = ["a","b","b"]

        test = areFollowingPatterns(strings, patterns)
        sol = False
        self.assertTrue(test == sol, msg=test)

    def test_3(self):
        strings = ["cat",
                  "dog",
                  "dog"]
        patterns = ["a",
                   "b",
                   "c"]

        test = areFollowingPatterns(strings, patterns)
        sol = False
        self.assertTrue(test == sol, msg=test)

    def test_4(self):
        strings = ["aaa"]
        patterns = ["aaa"]

        test = areFollowingPatterns(strings, patterns)
        sol = True
        self.assertTrue(test == sol, msg=test)

    def test_5(self):
        strings = ["aaa",
                  "aaa",
                  "aaa"]
        patterns = ["aaa",
                   "bbb",
                   "aaa"]

        test = areFollowingPatterns(strings, patterns)
        sol = False
        self.assertTrue(test == sol, msg=test)

        
if __name__ == '__main__':
    unittest.main()