import unittest
import calc


class TestAdd(unittest.TestCase):
    """test class of calc.py"""

    def test_add(self):
        """test method for add"""

        value1 = 2
        value2 = 6
        expected = 8

        actual = calc.add(value1, value2)
        self.assertEqual(expected, actual)


class TestSub(unittest.TestCase):
    """test class of calc.py"""

    def test_subtract(self):
        """test method for subtract"""
        value1 = 2
        value2 = 12
        expected = -10

        actual = calc.subtract(value1, value2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
