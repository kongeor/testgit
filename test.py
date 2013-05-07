import unittest
from mymath import mymath

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mymath.add(5,4), 9)

    def test_sub(self):
        self.assertEqual(mymath.sub(5,4), 1)

if __name__ == '__main__':
    unittest.main()
