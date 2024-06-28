import re

class StringCalculator:
    def add(self, num):
        if num == "":
            return 0

        delimiters = [",", "\n"]
        custom_delimiters = []

        # Check for custom delimiter syntax
        if num.startswith("//"):
            # Extract custom delimiter part and numbers part
            custom_delimiter_part, num = num[2:].split('\n', 1)
            
            # Custom delimiters without brackets
            if custom_delimiter_part and "[" not in custom_delimiter_part:
                custom_delimiters = list(custom_delimiter_part)
            else:
                # Custom delimiters with brackets
                custom_delimiters = re.findall(r"\[(.*?)\]", custom_delimiter_part)
            
            delimiters.extend(custom_delimiters)

        # Create a regular expression pattern to match all delimiters
        delimiter_pattern = "|".join(re.escape(delim) for delim in delimiters)
        numbers = re.split(delimiter_pattern, num)

        negatives = [int(num) for num in numbers if num and int(num) < 0]

        if negatives:
            raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")

        return sum(int(num) for num in numbers if num and num.lstrip('-').isdigit())