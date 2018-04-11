import unittest
from possibleSums import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        coins = [10, 50, 100]
        quantity = [1, 2, 1]
        test = possibleSums(coins, quantity)

        self.assertEqual(9, test)

    def test_2(self):
        coins = [10, 50, 100, 500]
        quantity = [5,3,2,2]
        test = possibleSums(coins, quantity)

        self.assertEqual(122, test)


if __name__ == '__main__':
    unittest.main()
