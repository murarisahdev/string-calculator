import unittest
from main import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        # Test that an empty string returns 0.
        calculator = StringCalculator()
        self.assertEqual(calculator.add(""), 0)
    
    def test_single_number(self):
        # Test that a single number returns the number itself
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1"), 1)
    
    def test_two_numbers(self):
        # Test that two comma-separated numbers are added correctly
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1,2"), 3)

    def test_multiple_numbers(self):
        # Test that multiple comma-separated numbers are added correctly
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1,2,3"), 6)

    def test_new_lines_between_numbers(self):
        # Test that newline characters between numbers are handled correctly
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1\n2,3"), 6)

    def test_different_delimiters(self):
        # Test that different delimiters can be specified and handled correctly
        calculator = StringCalculator()
        self.assertEqual(calculator.add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        # Test that negative numbers raise an exception
        calculator = StringCalculator()
        with self.assertRaises(Exception) as context:
            calculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2")
    
    def test_multiple_negative_numbers(self):
        # Test that multiple negative numbers raise an exception with all negatives listed
        calculator = StringCalculator()
        with self.assertRaises(Exception) as context:
            calculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2, -3")

    def test_multiple_delimiters_with_length_longer_than_one_char(self):
        # Test that multiple delimiters with length longer than one character can be specify and handle correctly
        calculator = StringCalculator()
        self.assertEqual(calculator.add("//[**][%%]\n1**2%%3"), 6)

    def test_zero_input(self):
        # Test for zero input, should return 0
        calculator = StringCalculator()
        self.assertEqual(calculator.add("0"), 0)
    
    def test_multiple_delimiters_in_one_string(self):
        # Test for multiple delimiters in one string
        calculator = StringCalculator()
        self.assertEqual(calculator.add("//[*][%]\n1*2%3*4%5"), 15)
    
    def test_only_delimiters(self):
        # Test for input string containing only delimiters
        calculator = StringCalculator()
        self.assertEqual(calculator.add("//[*][%]\n"), 0)
    
    def test_new_line_at_the_end(self):
        # Test for handling new lines at the end of the input string
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1,2\n"), 3)
    
    def test_complex_delimiter_with_special_characters(self):
        # Test for complex delimiters with many special characters
        calculator = StringCalculator()
        self.assertEqual(calculator.add("//[***][%%%]\n1***2%%%3"), 6)

if __name__ == '__main__':
    unittest.main()
