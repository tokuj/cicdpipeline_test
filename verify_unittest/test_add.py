import unittest
from add import add

class TestAdd(unittest.TestCase):
  """
  test class of add.py
  """

  def test_add(self):
    """
    test method for add
    """
    value1 = 2
    value2 = 6
    expected = 9
    actual = add(value1, value2)

    self.assertEqual(expected, actual)

if __name__ == "__main__":
  unittest.main()
