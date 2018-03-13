import unittest
from removeKFromList import removeKFromList


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertTrue(removeKFromList(l, k))

if __name__ == '__main__':
    unittest.main()
