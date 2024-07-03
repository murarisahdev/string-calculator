import unittest
from main import StringCalculator

class TestStringCalculator(unittest.TestCase):
    # Using setUp method for initializaing calculator for all test cases
    def setUp(self):
        self.calculator = StringCalculator()
    
    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"),3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3"),6)

    def test_new_lines_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_different_delimiters(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            self.calculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2")
    
    def test_multiple_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            self.calculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2, -3")

    def test_multiple_delimiters_with_length_longer_than_one_char(self):
        self.assertEqual(self.calculator.add("//[**][%%]\n1**2%%3"), 6)

    def test_zero_input(self):
        self.assertEqual(self.calculator.add("0"), 0)
    
    def test_multiple_delimiters_in_one_string(self):
        self.assertEqual(self.calculator.add("//[*][%]\n1*2%3*4%5"), 15)
    
    def test_only_delimiters(self):
        self.assertEqual(self.calculator.add("//[*][%]\n"), 0)
    
    def test_new_line_at_the_end(self):
        self.assertEqual(self.calculator.add("1,2\n"), 3)
    
    def test_complex_delimiter_with_special_characters(self):
        self.assertEqual(self.calculator.add("//[***][%%%]\n1***2%%%3"), 6)
        
    def test_custom_delimiter_with_special_characters(self):
        self.assertEqual(self.calculator.add("//,,%#@$]\n1,23"), 24)
    
    def test_custom_delimiter_with_newlines(self):
        self.assertEqual(self.calculator.add("//;\n30;\n\n20"), 50)

    def test_pipe_separator(self):
        self.assertEqual(self.calculator.add("//|25|25"),50)
        
if __name__ == '__main__':
    unittest.main()