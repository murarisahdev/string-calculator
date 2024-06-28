# String Calculator

This repository contains a Python implementation of the String Calculator, developed using a test-driven development (TDD) approach. The String Calculator handles various scenarios such as different delimiters, newline handling between numbers, and exceptions for negative numbers.

## Features

- **Handling of Different Delimiters**: The calculator supports multiple delimiters including commas, newlines, and custom delimiters specified at the beginning of the input string.
  
- **Newline Handling**: Numbers in the input string can be separated by either commas or newlines, and the calculator correctly sums them.
  
- **Custom Delimiters**: Custom delimiters can be specified using a special syntax (`//[delimiter]\n[numbers…]`), allowing flexibility in input formats.
  
- **Exception Handling**: When negative numbers are provided, the calculator raises an exception indicating "negative numbers not allowed" followed by the negative numbers themselves.

- **Ignoring Large Numbers**: Numbers larger than 1000 are ignored in the summation process.

### Running Tests

To run the tests, ensure you have Python installed and execute:

```sh
python -m unittest discover
