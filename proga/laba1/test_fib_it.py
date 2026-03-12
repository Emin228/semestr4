import unittest
from fib_iterator import FibonacchiLst

class TestFibIterator(unittest.TestCase):

    def test_normal(self):
        result = list(FibonacchiLst(range(10)))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8])

    def test_corner_0(self):
        result = list(FibonacchiLst(range(0)))
        self.assertEqual(result, [])

    def test_corner_1(self):
        result = list(FibonacchiLst(range(1)))
        self.assertEqual(result, [0])

    def test_corner_2(self):
        result = list(FibonacchiLst(range(2)))
        self.assertEqual(result, [0, 1])

    def test_corner_3(self):
        result = list(FibonacchiLst([1, 1]))
        self.assertEqual(result, [1, 1])

    def test_corner_4(self):
        result = list(FibonacchiLst([1, 1,1,1,1,1,1]))
        self.assertEqual(result, [1, 1])

    def test_corner_5(self):
        result = list(FibonacchiLst([1, 1, 0,0,0,1]))
        self.assertEqual(result, [1, 1, 0])
if __name__ == '__main__':
    unittest.main()
