"""
This module provides a Calculator class with basic arithmetic operations.
"""


class Calculator:
    """
    基本的な算術演算ができるシンプルな電卓アプリ。
    """

    def add(self, a, b):
        """
        Adds two number together.

        Args:
          a(int or float): The first number.
          b(int or float): The second number.

        Returns:
          int or float: The sum of the numbers.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first.

        Args:
          a(int or float): The first number
          b(int or float): The second number.

        Returns:
          int or float: The result of the subtraction.
        """
        return a - b


if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(5, 3))
