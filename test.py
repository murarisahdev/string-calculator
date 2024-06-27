import unittest
from main import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add(""), 0)
    
    def test_single_number(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1"), 1)
    
    def test_two_numbers(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1,2"), 3)

    def test_multiple_numbers(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1,2,3"), 6)

    def test_new_lines_between_numbers(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1\n2,3"), 6)


if __name__ == '__main__':
    unittest.main()
