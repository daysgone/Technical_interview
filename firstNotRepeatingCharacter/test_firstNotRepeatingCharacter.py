import unittest
from firstNotRepeatingCharacter import firstNotRepeatingCharacter


class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "abacabad"
        self.assertTrue(firstNotRepeatingCharacter(s) == 'c')

    def test_2(self):
        s = "abacabaabacaba"
        self.assertTrue(firstNotRepeatingCharacter(s) == '_')

    def test_3(self):
        s = "z"
        self.assertTrue(firstNotRepeatingCharacter(s) == 'z')

    def test_3(self):
        s = "ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof"
        self.assertTrue(firstNotRepeatingCharacter(s) == 'g')

if __name__ == '__main__':
    unittest.main()


