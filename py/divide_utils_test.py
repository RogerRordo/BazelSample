# Copyright 2024 the bazel_example project authors. All rights reserved.
# Authors: luozhuofeng@gmail.com (Zhuofeng Luo)
import unittest

from py.divide_utils import integer_division


class TestDivideUtils(unittest.TestCase):
    """Unittest class for divide_utils"""

    def test_integer_division(self):
        """Test integer_division"""
        self.assertEqual(integer_division(5, 2), 2)
        self.assertRaises(ZeroDivisionError, integer_division, 1, 0)


if __name__ == '__main__':
    unittest.main()
