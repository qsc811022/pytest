# test_mymath_unittest.py
import unittest
from mymath import add

class TestMyMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)      # 正常
        self.assertEqual(add(-1, 1), 0)     # 負數
        self.assertEqual(add(0, 0), 0)      # 零

if __name__ == '__main__':
    unittest.main()