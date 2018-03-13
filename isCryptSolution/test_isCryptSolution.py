import unittest
from isCryptSolution import isCryptSolution


class MyTestCase(unittest.TestCase):
    def test_1(self):
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
        self.assertTrue(isCryptSolution(crypt, solution))

    def test_2(self):
        crypt = ["TEN",
                "TWO",
                "ONE"]
        solution = [["O", "1"],
                   ["T", "0"],
                   ["W", "9"],
                   ["E", "5"],
                   ["N", "4"]]
        self.assertFalse(isCryptSolution(crypt, solution))

    def test_5(self):
        crypt = ["A", "A", "A"]
        solution = [["A", "0"]]
        self.assertTrue(isCryptSolution(crypt, solution))

    def test_19(self):
        crypt = ["WASD", "IJKL", "AOPAS"]
        solution = [["W", "2"],
                   ["A", "0"],
                   ["S", "4"],
                   ["D", "1"],
                   ["I", "5"],
                   ["J", "8"],
                   ["K", "6"],
                   ["L", "3"],
                   ["O", "7"],
                   ["P", "9"]]
        self.assertFalse(isCryptSolution(crypt, solution))

if __name__ == '__main__':
    unittest.main()
