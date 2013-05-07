import unittest
from mymath import mymath

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mymath.add(5,4), 9)

    def test_is_odd(self):
        self.assertTrue(mymath.is_odd(9))

    def test_sub(self):
        self.assertEqual(mymath.sub(5,4), 1)

    def test_mul(self):
        self.assertEqual(mymath.mul(5,4), 20)

if __name__ == '__main__':
    unittest.main()
